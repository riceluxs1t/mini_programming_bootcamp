# -*- coding:utf-8 -*-

import os
from django.views.generic import TemplateView
from website.forms import UploadFileForm
from django.shortcuts import render
from django.http import *
from website.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, S3_SUBMISSION_BUCKET_NAME
import boto3

class IndexView(TemplateView):
    template_name = "website/index.html"

#class SubmitView(TemplateView):
	#template_name = "website/submit.html"

#generate submit template method-based
def submitTemplate(request):
	return render(request, "website/submit.html")

#file upload method
def uploadFile(request):
	#get relevant info
	file = request.FILES['file']
	netId = request.POST.get('netId')
	
	print file
	#create upload form
	form = UploadFileForm(request.POST, request.FILES)
	#netId = request.netId
	
	#file path should be homework/netId/filename
	filepath = "homework/" + netId + "/" + file.name
	print AWS_ACCESS_KEY_ID
	s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, 
		aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

	#s3 = boto3.resource('s3')
	s3.upload_fileobj(Fileobj=file, Bucket=S3_SUBMISSION_BUCKET_NAME, Key=filepath)

	#bucket = s3.Bucket("rice-python-web-class")

	#bucket.put_object(Key=filepath, Body=file)
	#print bucket
	#print(form)
	return render(request, "website/submit.html")

