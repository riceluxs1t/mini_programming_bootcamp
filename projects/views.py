# -*- coding:utf-8 -*-
import boto3
import json

from django.http import *
from django.shortcuts import render
from website.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, S3_PROJECT_IMAGE_BUCKET_NAME


def analyze_image(request):

    s3_client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID,
                             aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    s3_response = s3_client.list_objects(Bucket=S3_PROJECT_IMAGE_BUCKET_NAME)
    image_names = [content['Key'] for content in s3_response['Contents']]

    return render(
        request,
        "projects/find_face/analyze.html",
        {
            "image_names":
                image_names
        }
    )


def submit_image(request):
    return render(request, "projects/find_face/submit.html")


def call_face_api(request):

    try:
        image_name_selected = request.POST['image_name']

        rekognition = boto3.client(
            'rekognition',
            region_name='us-east-1',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY
        )

        face_api_response = rekognition.detect_faces(
            Image={
                'S3Object': {
                    'Bucket': S3_PROJECT_IMAGE_BUCKET_NAME,
                    'Name': image_name_selected
                },
            },
            Attributes=[
                'ALL',
            ]
        )

        return HttpResponse(json.dumps({"status": True, "body": face_api_response}), content_type="application/json")
    except:
        raise


def upload_file(request):
    try:
        image_uploaded = request.FILES['file']

        # file path should be examples/FILE_NAME
        filepath = "examples/" + image_uploaded.name

        s3 = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY
        )

        # upload object
        s3.upload_fileobj(Fileobj=image_uploaded, Bucket=S3_PROJECT_IMAGE_BUCKET_NAME, Key=filepath)
        return HttpResponse(json.dumps({"result": True}), content_type="application/json")
    except:
        raise
