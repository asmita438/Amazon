import unittest
from selenium import webdriver

class AmazonHomePage(unittest.TestCase):
    # define base url
    base_url = "https://www.amazon.in"

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="/home/asmita/Desktop/Amazon/drivers/geckodriver")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    
    def test_load_home_page(self):
        # to initialize a variable to hold reference of webdriver instance being passed
        driver = self.driver
        self.assertIn("Amazon", driver.title)

    def tearDown(self):
        #closes the current tab
        self.driver.close()
    
    if __name__ == "__main__":
        unittest.main()



