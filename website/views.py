# -*- coding:utf-8 -*-

from django.views.generic import TemplateView
from django.shortcuts import redirect
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response


class IndexView(TemplateView):
    template_name = "website/index.html"


class MaterialView(APIView):
    """
    A generic view class that displays serial materials. i.e. lecture0, lecture1, etc.
    Used to display views for the lecture and homework materials.

    """
    renderer_classes = [TemplateHTMLRenderer]

    # the relative path to a template file
    template_name = None

    # the relative path to an actual material file imported inside the template
    _material_file_path = None

    # the display name for the material
    _material_display_name = None

    # used to make the navigation urls between previous / next materials
    _material_url_prefix = None

    # the corresponding model must have the 'is_visible' attribute
    _model = None

    def __init__(self):
        super(MaterialView, self).__init__()

    def _check_whether_implemented(self):
        if not (self.template_name and self._material_display_name and self._material_file_path and
                    self._material_url_prefix and self._model):
            raise NotImplemented("The sub class of MaterialView class must define all the required attributes")

    def get(self, request, **kwargs):

        self._check_whether_implemented()

        material_id = int(kwargs.get('material_id', 0))

        # if the lecture does not yet exist or is not set to be visible, kick back to the front page
        if not self._model.objects.filter(id=material_id).exists() or \
                self._model.objects.filter(id=material_id, is_visible=False):
            return redirect("/")

        previous_material = self._material_url_prefix.format(material_id - 1)

        if material_id == 0:
            previous_material = self._material_url_prefix.format(material_id)

        if self._model.objects.filter(id=material_id + 1, is_visible=True).exists():
            next_material = self._material_url_prefix.format(material_id + 1)
        else:
            # if the next lecture does not exist or is not set to visible, loop back to the current one.
            next_material = self._material_url_prefix.format(material_id)

        return Response(
            {
                'material_file_path': self._material_file_path.format(material_id),
                'material_display_name': self._material_display_name.format(material_id),
                'previous_material': previous_material,
                'next_material': next_material
            }
        )
