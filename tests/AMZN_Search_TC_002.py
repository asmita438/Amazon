from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# declare variable to store the URL to be visited
base_url="https://www.amazon.in"
# declare variable to store search term
search_term="Foundation of Software Testing by Dorothy Graham and Rex Black"
driver=webdriver.Chrome(executable_path="/home/asmita/Desktop/Amazon/drivers/geckodriver")
driver.maximize_window()
driver.implicitly_wait(10) 
driver.get(base_url)
# test whether correct URL/ Web Site has been loaded or not
assert "Amazon" in driver.title
