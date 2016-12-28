from django.shortcuts import redirect
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response

from lectures.models import Lectures


class LectureView(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'lectures/lecture_base_html.htm'
    jupyter_lecture_path = "jupyter_lectures/lecture{0}.html"
    jupyter_lecture_name = "Lecture {0}"
    lecture_url_prefix = "/lectures/{0}"

    def get(self, request, **kwargs):

        lecture_id = int(kwargs.get('lecture_id', 1))

        # if the lecture does not yet exist or is not set to be visible, kick back to the front page
        if not Lectures.objects.filter(id=lecture_id).exists() or \
                Lectures.objects.filter(id=lecture_id, is_visible=False):
            return redirect("/")

        previous_lecture = self.lecture_url_prefix.format(lecture_id - 1)

        if lecture_id == 1:
            previous_lecture = self.lecture_url_prefix.format(lecture_id)

        if Lectures.objects.filter(id=lecture_id + 1, is_visible=True).exists():
            next_lecture = self.lecture_url_prefix.format(lecture_id + 1)
        else:
            # if the next lecture does not exist or is not set to visible, loop back to the current one.
            next_lecture = self.lecture_url_prefix.format(lecture_id)

        return Response(
            {
                'lecture_path': self.jupyter_lecture_path.format(lecture_id),
                'lecture_name': self.jupyter_lecture_name.format(lecture_id),
                'previous_lecture': previous_lecture,
                'next_lecture': next_lecture
            }
        )
