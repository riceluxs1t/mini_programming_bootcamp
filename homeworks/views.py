from website.views import MaterialView
from models import Homework


class HomeworkView(MaterialView):

    template_name = 'homeworks/homework_base_html.htm'
    _material_file_path = "jupyter_homeworks/homework{0}.html"
    _material_display_name = "Homework {0}"
    _material_url_prefix = "/homeworks/{0}"
    _model = Homework
