from selenium import webdriver
base_url="https://www.amazon.in"
# declare and initialize driver variable
driver=webdriver.Firefox(executable_path="/home/asmita/Desktop/Amazon/drivers/geckodriver")
driver.maximize_window()
driver.implicitly_wait(10) #10 is in seconds
# to load a given URL in browser window
driver.get(base_url)
# test whether correct URL/ Web Site has been loaded or not
assert "Amazon" in driver.title
driver.fin
# to close the browser
driver.close()
