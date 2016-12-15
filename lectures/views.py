from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response


class LectureView(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'lectures/lecture_base_html.htm'
    jupyter_lecture_path = "jupyter_lectures/lecture{0}.html"
    jupyter_lecture_name = "Lecture {0}"

    def get(self, request, **kwargs):

        lecture_id = kwargs.get('lecture_id', 1)

        return Response(
            {
                'lecture_path': self.jupyter_lecture_path.format(lecture_id),
                'lecture_name': self.jupyter_lecture_name.format(lecture_id)
            }
        )
