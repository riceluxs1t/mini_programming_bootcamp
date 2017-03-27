# -*- coding:utf-8 -*-
import boto3
import json
import requests
import cStringIO

from PIL import Image, ImageDraw
from io import BytesIO

from django.http import *
from django.shortcuts import render
from website.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, S3_PROJECT_IMAGE_BUCKET_NAME


def analyze_image(request):

    s3_client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID,
                             aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    s3_response = s3_client.list_objects(Bucket=S3_PROJECT_IMAGE_BUCKET_NAME)
    image_names = [content['Key'] for content in s3_response['Contents'] if 'examples' in content['Key']]

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
        print face_api_response
        # TODO: replace the hard coding
        response = requests.get(
            "https://s3.amazonaws.com/rice-python-project-images/" + image_name_selected
        )
        img = Image.open(BytesIO(response.content))
        width, height = img.size

        for faceDetail in face_api_response["FaceDetails"]:

            bounding_rectangle = faceDetail["BoundingBox"]
            bounding_width = bounding_rectangle["Width"]
            bounding_height = bounding_rectangle["Height"]
            bounding_top = bounding_rectangle["Top"]
            bounding_left = bounding_rectangle["Left"]

            draw = ImageDraw.Draw(img)
            draw.rectangle(
                (
                    width*bounding_left,
                    height*bounding_top,
                    width*(bounding_left + bounding_width),
                    height*(bounding_top+bounding_height)

                ), outline=(173, 255, 47))

        s3 = boto3.resource('s3')
        output_image = cStringIO.StringIO()
        img.save(output_image, "jpeg")

        filepath = "processed/" + image_name_selected[10:]
        s3.Bucket(S3_PROJECT_IMAGE_BUCKET_NAME).put_object(
            Key=filepath,
            Body=output_image.getvalue(),
            ACL="public-read"
        )

        return HttpResponse(
            json.dumps({"status": True, "body": face_api_response, "link": "https://s3.amazonaws.com/rice-python-project-images/" + filepath}),
            content_type="application/json"
        )
    except:
        raise


def upload_file(request):
    try:
        image_uploaded = request.FILES['file']

        # file path should be examples/FILE_NAME
        filepath = "examples/" + image_uploaded.name

        s3 = boto3.resource('s3')
        # upload object
        s3.Bucket(S3_PROJECT_IMAGE_BUCKET_NAME).put_object(
            Key=filepath,
            Body=image_uploaded.read(),
            ACL="public-read"
        )

        return HttpResponse(json.dumps({"result": True}), content_type="application/json")
    except:
        raise
