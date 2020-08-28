from django.test import TestCase
from cv.models import CV_Item, CV_Category
from cv.utils import CVStructureMaker

class CVViewTests(TestCase):

    def test_is_cv_page_accessable(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response, 'cv/show_cv.html')

class CVInfoModelTests(TestCase):

    def test_do_database_tables_exist(self):
        CV_Category()
        CV_Item()

    def test_can_make_item_category_structure(self):
        first_category = CV_Category()
        first_category.name = "Komi"
        first_category.position = 1
        first_category.save()
        first_item = CV_Item()
        first_item.name = "communication 1"
        first_item.description = "totally normal"
        first_item.position = 1
        first_item.CV_Category = first_category
        first_item.save()
        example_dict = CVStructureMaker()
        self.assertEqual(str(example_dict), "[['Komi', [<CV_Item: communication 1>]]]")

