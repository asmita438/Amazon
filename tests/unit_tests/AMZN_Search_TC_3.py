import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class AddToCart(unittest.TestCase):
    base_url = "https://www.amazon.in"
    search_term="Aloevera gel"

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="/home/asmita/Desktop/Amazon/drivers/geckodriver")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    
    def test_add_to_cart(self):
        self.driver.get(self.base_url)
        searchTextBox = self.driver.find_element_by_id("twotabsearchtextbox")
        searchTextBox.clear()
        searchTextBox.send_keys(self.search_term)
        searchTextBox.send_keys(Keys.RETURN)
        # to click on the first search result's link
        self.driver.find_element_by_xpath(
            "(//div[@class='sg-col-inner']//img[contains(@data-image-latency,'s-product-image')])[2]").click()
        #to switch to the tab in which the product has opened
        self.driver.switch_to.window(self.driver.window_handles[1])
        # to add the product to cart by clicking the add to cart button
        self.driver.find_element_by_id("add-to-cart-button").click()
        # to verify that sub cart page has loaded
        self.assertTrue(self.driver.find_element_by_id(
            "hlb-subcart").is_enabled())
        # to verify that the product was added to the cart successfully
        self.assertTrue(self.driver.find_element_by_id(
            "hlb-ptc-btn-native").is_displayed())
        
    def tearDown(self):
        #to close the browser
        self.driver.quit()
    
if __name__ == "__main__":
    unittest.main()

        
