import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class AmazonSearch(unittest.TestCase):
    base_url = "https://www.amazon.in"
    search_term = "Aloevera gel"

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="/home/asmita/Desktop/Amazon/drivers/geckodriver")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    
    def test_search_for_a_term(self):
        self.driver.get(self.base_url)
        searchTextBox = self.driver.find_element_by_id("twotabsearchtextbox")
        searchTextBox.clear()
        searchTextBox.send_keys(self.search_term)
        searchTextBox.send_keys(Keys.RETURN)

        self.assertIN(self.search_term, self.driver.title)
        self.assertNotIn("No results found", self.driver.page_source)

    def tearDown(self):
        self.driver.close()
    
if __name__ == "__main__":
        unittest.main()
