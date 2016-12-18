from django.test import TestCase
from apps import GraderConfig


class TestConfig(TestCase):

    def test_config(self):

        self.assertEquals(
            GraderConfig.grader_name,
            "nk15"
        )
