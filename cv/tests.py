from django.test import TestCase
from cv.models import CV_Item, CV_Category

class CVViewTests(TestCase):

    def test_is_cv_page_accessable(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response, 'cv/show_cv.html')

class CVInfoModelTests(TestCase):

    def test_do_database_tables_exist(self):
        new_categroy = CV_Category()
        new_item = CV_Item()

