import unittest
from selenium import webdriver
import time

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

        #User can see the title and text of a blog post
        #This is really messy as it is based on a static post
        #TODO:Solution not based on Hello world post
        self.assertEqual('Hello world', self.browser.find_element_by_id("header11").text)
        self.assertEqual('I made a blog. I can edit the text', self.browser.find_element_by_id("text11").text)

        #User tries to view the detail of the blog post
        self.browser.find_element_by_id("link11").click()
        time.sleep(1)
        assert(self.browser.current_url.endswith("/post/11/"))

    def test_can_view_cv(self):

        #User open the site
        self.browser.get('http://localhost:8000')

        #user clicks on the link to the cv page
        self.browser.find_element_by_id("cv link").click()
        time.sleep(1)

        #checks the github link
        self.browser.find_element_by_id("git-hub-link").click()
        time.sleep(1)
        self.assertEqual(self.browser.current_url, "https://github.com/Max-K-Warren")
        self.browser.back()

        #checks the linkedin link
        self.browser.find_element_by_id("linked-in-link").click()
        time.sleep(1)
        self.assertIn("linkedin.com", self.browser.current_url)
        self.browser.back()

        #user can read the heading
        try:
            self.browser.find_element_by_id("fixed-info")
        except:
            self.fail("fixed-info not on page")



if __name__ == '__main__':
    unittest.main(warnings='ignore')