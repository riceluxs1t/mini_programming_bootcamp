# -*- coding:utf-8 -*-
import boto3
import json

from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import *
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from hashlib import sha256
from pbkdf2 import pbkdf2


from website.forms import UploadFileForm
from settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, S3_SUBMISSION_BUCKET_NAME
from homeworks.models import Homework, Student


class IndexView(TemplateView):
    template_name = "website/index.html"


class MaterialView(APIView):
    """
    A generic view class that displays serial materials. i.e. lecture0, lecture1, etc.
    Used to display views for the lecture and homework materials.

    """
    renderer_classes = [TemplateHTMLRenderer]

    # the relative path to a template file
    template_name = None

    # the relative path to an actual material file imported inside the template
    _material_file_path = None

    # the display name for the material
    _material_display_name = None

    # used to make the navigation urls between previous / next materials
    _material_url_prefix = None

    # the corresponding model must have the 'is_visible' attribute
    _model = None

    def __init__(self):
        super(MaterialView, self).__init__()

    def _check_whether_implemented(self):
        if not (self.template_name and self._material_display_name and self._material_file_path and
                    self._material_url_prefix and self._model):
            raise NotImplemented("The sub class of MaterialView class must define all the required attributes")

    def get(self, request, **kwargs):

        self._check_whether_implemented()

        material_id = int(kwargs.get('material_id', 0))

        # if the lecture does not yet exist or is not set to be visible, kick back to the front page
        if not self._model.objects.filter(id=material_id).exists() or \
                self._model.objects.filter(id=material_id, is_visible=False):
            return redirect("/")

        previous_material = self._material_url_prefix.format(material_id - 1)

        if material_id == 0:
            previous_material = self._material_url_prefix.format(material_id)

        if self._model.objects.filter(id=material_id + 1, is_visible=True).exists():
            next_material = self._material_url_prefix.format(material_id + 1)
        else:
            # if the next lecture does not exist or is not set to visible, loop back to the current one.
            next_material = self._material_url_prefix.format(material_id)

        return Response(
            {
                'material_file_path': self._material_file_path.format(material_id),
                'material_display_name': self._material_display_name.format(material_id),
                'previous_material': previous_material,
                'next_material': next_material
            }
        )


# generate submit template method-based
def submitTemplate(request):
    homeworks = Homework.objects.filter(is_visible=True)
    return render(request, "website/submit.html", {"homeworks": homeworks})


# file upload method
def uploadFile(request):
    try:
        # get relevant info
        file = request.FILES['file']
        netId = request.POST.get('netId')
        hw_type = request.POST.get('homework_type')
        submission_key = request.POST.get("submissionKey")

        if not Student.objects.filter(student_id=netId).exists():
            return HttpResponse(
                json.dumps({"result": False, "msg": "Not a registered student"}),
                content_type="application/json"
            )

        student = Student.objects.get(student_id=netId)
        if not Student.check_password(student, sha256(str(submission_key)).hexdigest()):
            return HttpResponse(
                json.dumps({"result": False, "msg": "submission key matching failed"}),
                content_type="application/json"
            )

        # create upload form
        form = UploadFileForm(request.POST, request.FILES)

        # file path should be homework/{HOMEWORKTYPE}/{NETID}/{FILENAME}
        filepath = "/homework/" + hw_type + "/" + netId + "/" + file.name
        s3 = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY
        )

        # upload object
        s3.upload_fileobj(Fileobj=file, Bucket=S3_SUBMISSION_BUCKET_NAME, Key=filepath)

        return HttpResponse(json.dumps({"result": True}), content_type="application/json")
    except:
        return HttpResponse(json.dumps({"result": False, "msg": "unknown error"}), content_type="application/json")


# user sign up
def signUp(request):
    try:
        # get user info
        netId = request.POST.get('netId')
        password = request.POST.get('password')
        if Student.objects.filter(student_id=netId).exists():
            return HttpResponse(
                json.dumps({"result": False, "msg": "duplicate netId exists!"}),
                content_type="application/json"
            )

        password_hashed = pbkdf2(sha256(str(password)).hexdigest())

        newUser = User(username=netId, password=password_hashed)

        # the postSave signal auto creates the corresponding student object.
        newUser.save()

        # update the other fields in the corresponding Student object
        Student.objects.filter(user=newUser).update(student_id=netId, submission_key=password_hashed)

        return HttpResponse(json.dumps({"result": True}), content_type="application/json")
    except:
        return HttpResponse(
            json.dumps({"result": False, "msg": "unknown error happened"}),
            content_type="application/json"
        )

