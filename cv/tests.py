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
        self.assertEqual(str(example_dict), "[[<CV_Category: Komi>, [<CV_Item: communication 1>]]]")


    #Items with be reordered  and outputted according to their position values not
    def test_can_use_position_to_order_output(self):
        second_category = self.save_category("Volume 2", 2)
        first_category = self.save_category("Volume 1", 1)
        fourth_item = self.save_item("communication 21", "fitness test", 2, second_category)
        third_item = self.save_item("communication 20", "the physical", 1, second_category)
        first_item = self.save_item("communication 1", "totally normal", 1, first_category)
        second_item = self.save_item("communication 2", "peaceful", 2, first_category)
        reordered_dict = CVStructureMaker()
        self.assertEqual(str(reordered_dict), "[[<CV_Category: Volume 1>, [<CV_Item: communication 1>, <CV_Item: communication 2>]], [<CV_Category: Volume 2>, [<CV_Item: communication 20>, <CV_Item: communication 21>]]]")

    

