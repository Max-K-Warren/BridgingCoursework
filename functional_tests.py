import unittest
from selenium import webdriver

class WebsiteTests(unittest.TestCase):

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    #testing that you can open the site, and check multiple blogs posts
    def test_can_view_posts(self):

        #User opens the site
        self.browser.get('http://localhost:8000')

        #User checks the title to make sure they're on the right site
        self.assertEqual('Blog', self.browser.title)

        #User can see one of the blog posts
        #This is really messy as it is based on a static post
        #TODO:Solution not based on Hello world post
        self.assertEqual('Hello world', self.browser.find_element_by_id("header11").text)


if __name__ == '__main__':
    unittest.main(warnings='ignore')