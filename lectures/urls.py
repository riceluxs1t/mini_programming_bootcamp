from django.conf.urls import url

from views import LectureView

urlpatterns = [
    url(r'^(?P<lecture_id>\d+)', LectureView.as_view())
]
