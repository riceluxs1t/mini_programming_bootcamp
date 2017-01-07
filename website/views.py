# -*- coding:utf-8 -*-

import os
from django.views.generic import TemplateView
from website.forms import UploadFileForm
from django.shortcuts import render
from django.http import *
from settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, S3_SUBMISSION_BUCKET_NAME
import boto3
import json

class IndexView(TemplateView):
    template_name = "website/index.html"

#class SubmitView(TemplateView):
	#template_name = "website/submit.html"

#generate submit template method-based
def submitTemplate(request):
	return render(request, "website/submit.html")

#file upload method
def uploadFile(request):
	try:
		#get relevant info
		file = request.FILES['file']
		netId = request.POST.get('netId')
		
		#create upload form
		form = UploadFileForm(request.POST, request.FILES)
		
		
		#file path should be homework/netId/filename
		filepath = "/homework/" + netId + "/" + file.name
		s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, 
			aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
		
		#upload object
		s3.upload_fileobj(Fileobj=file, Bucket=S3_SUBMISSION_BUCKET_NAME, Key=filepath)


		return HttpResponse(json.dumps({"result": True}), content_type="application/json")
	except:
		return HttpResponse(json.dumps({"result": False}), content_type="application/json")

