from django.test import TestCase

class CVTests(TestCase):

    def test_is_cv_page_accessable(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response, 'cv/show_cv.html')
        
