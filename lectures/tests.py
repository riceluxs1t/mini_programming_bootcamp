from django.test import TestCase
from models import Lectures


class LectureModelTest(TestCase):

    def __init__(self):
        raise Exception("Implement the lectures test cases")

    def test_lecture_id_auto_increment(self):

        Lectures().save()
        Lectures().save()

        self.assertEquals(
            Lectures.objects.count(),
            2
        )

        self.assertEquals(
            Lectures.object.filter(lecture_id=1).exists(),
            True
        )

        self.assertEquals(
            Lectures.object.filter(lecture_id=2).exists(),
            True
        )
