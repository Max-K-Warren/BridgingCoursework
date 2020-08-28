from django.test import TestCase
from cv.models import CV_Item, CV_Category
from cv.utils import CVStructureMaker

class CVViewTests(TestCase):

    def test_is_cv_page_accessable(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response, 'cv/show_cv.html')

class CVInfoModelTests(TestCase):

    def save_category(self, cat_name, cat_position):
        new_category = CV_Category()
        new_category.name = cat_name
        new_category.position = cat_position
        new_category.save()
        return new_category

    def save_item(self, item_name, item_description, item_position, item_category):
        new_item = CV_Item()
        new_item.name = item_name
        new_item.description = item_description
        new_item.position = item_position
        new_item.CV_Category = item_category
        new_item.save()
        return new_item


    def test_can_make_item_category_structure(self):
        first_category = self.save_category("Komi", 1)
        first_item = self.save_item("communication 1", "totally normal", 1, first_category)
        example_dict = CVStructureMaker()
        self.assertEqual(str(example_dict), "[['Komi', [<CV_Item: communication 1>]]]")

    

