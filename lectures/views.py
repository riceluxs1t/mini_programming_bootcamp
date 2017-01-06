
from lectures.models import Lectures
from website.views import MaterialView


class LectureView(MaterialView):

    template_name = 'lectures/lecture_base_html.htm'
    _material_file_path = "jupyter_lectures/lecture{0}.html"
    _material_display_name = "Lecture {0}"
    _material_url_prefix = "/lectures/{0}"
    _model = Lectures
