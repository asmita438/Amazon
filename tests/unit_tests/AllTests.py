import unittest
import time
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ViewProductDetails(unittest.TestCase):
    base_url = "http://www.amazon.in"
    search_term="WD My Passport 4TB"

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="/home/asmita/Desktop/Amazon/drivers/geckodriver")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    
    def test_AMZN_Search_TC_001_load_home_page(self):
        """User should be able to load Amazon’s Home Page"""
        driver = self.driver
        driver.get(self.base_url)
        self.assertIn("Amazon", driver.title)

    def test_AMZN_Search_TC_002_search_for_a_term(self):
        """User should be able to search products."""
        # to load a given URL in browser window
        self.driver.get(self.base_url)         
        searchTextBox=self.driver.find_element_by_id("twotabsearchtextbox")
        searchTextBox.clear()
        searchTextBox.send_keys(self.search_term)
        searchTextBox.send_keys(Keys.RETURN)
        self.assertIn(self.search_term,self.driver.title)
        self.assertNotIn("No results found.",self.driver.page_source)    

    def test_AMZN_Search_TC_003_add_item_to_cart(self):    
        """User should be able to add product to cart."""
        self.driver.get(self.base_url)        
        searchTextBox=self.driver.find_element_by_id("twotabsearchtextbox")
        searchTextBox.clear()
        searchTextBox.send_keys(self.search_term)
        searchTextBox.send_keys(Keys.RETURN)
        self.driver.find_element_by_xpath("(//div[@class='sg-col-inner']//img[contains(@data-image-latency,'s-product-image')])[2]").click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        # to add the product to cart by clicking the add to cart button        
        self.driver.find_element_by_id("add-to-cart-button").click()
        # to verify that sub cart page has loaded
        self.assertTrue(self.driver.find_element_by_id("hlb-subcart").is_enabled())
        # to verify that the product was added to the cart successfully
        self.assertTrue(self.driver.find_element_by_id("hlb-ptc-btn-native").is_displayed())

    def test_AMZN_Search_TC_004_delete_item_from_cart(self):
        """User should be able to delete an item from cart"""  
        self.driver.get(self.base_url)        
        searchTextBox=self.driver.find_element_by_id("twotabsearchtextbox")
        searchTextBox.clear()
        searchTextBox.send_keys(self.search_term)
        searchTextBox.send_keys(Keys.RETURN)

        # to click on the first search result's link
        self.driver.find_element_by_xpath("(//div[@class='sg-col-inner']//img[contains(@data-image-latency,'s-product-image')])[2]").click()
        # to switch tabs we will use window_handles()
        self.driver.switch_to.window(self.driver.window_handles[1])
        # to add the product to cart by clicking the add to cart button        
        self.driver.find_element_by_id("add-to-cart-button").click()

        # to confirm if the cart is empty
        #  print (self.driver.find_element_by_id('nav-cart-count').text)
       
        cartCount=int(self.driver.find_element_by_id('nav-cart-count').text)        
        if(cartCount<1):
            print("Cart is empty")
            exit()
        # to click on the Cart link
        self.driver.find_element_by_id("nav-cart").click()
        # to confirm Cart page has loaded and if yes then delete item              
        if(self.driver.title.startswith("Amazon.in Shopping Cart")):
            # to delete an item from the Cart
            self.driver.find_element_by_xpath("//div[contains(@class,'a-row sc-action-links')]//span[contains(@class,'sc-action-delete')]").click()
            time.sleep(2)        
        # to confirm the item was delete successfully
        self.assertTrue(int(self.driver.find_element_by_id('nav-cart-count').text) < cartCount)        

    def test_AMZN_Search_TC_005_test_signin_to_checkout(self):
        """User must sign in to checkout"""
        self.driver.get(self.base_url)
        searchTextBox = self.driver.find_element_by_id("twotabsearchtextbox")
        searchTextBox.clear()
        searchTextBox.send_keys(self.search_term)
        searchTextBox.send_keys(Keys.RETURN)

        self.driver.find_element_by_xpath("(//div[@class='sg-col-inner']//img[contains(@data-image-latency,'s-product-image')])[2]").click()
        self.driver.switch_to.windows(self.driver.window_handles[1])
        self.driver.find_element_by_id("add-to-cart-button").click()
        # to click on the 'Proceed to Buy' button
        self.driver.find_element_by_id('hlb-ptc-btn-native').click()
        # to confirm if SignIn page has loaded
        self.assertTrue(self.driver.title.startswith("Amazon Sign In"))
        # to confirm if the email or mobile number textbox is visible or not
        self.assertTrue(self.driver.find_element_by_id('ap_email').is_displayed()) 

    def tearDown(self):
        # to close the browser
        self.driver.quit()
        
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/asmita/Desktop/Amazon/Reports'))
