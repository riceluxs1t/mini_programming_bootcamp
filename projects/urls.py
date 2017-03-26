from django.conf.urls import url

from views import upload_file, submit_image, analyze_image, call_face_api

urlpatterns = [
    url(r'^submit/uploadFile/', upload_file, name="uploadFile"),
    url(r'^submit/', submit_image, name="submit"),
    url(r'^analyze/callAPI/', call_face_api, name="call_api"),
    url(r'^analyze/', analyze_image, name="analyze"),
]
