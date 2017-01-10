from django.conf.urls import url

from views import HomeworkView

urlpatterns = [
    url(r'^(?P<material_id>\d+)', HomeworkView.as_view())
]
