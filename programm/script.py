

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


browser = webdriver.Firefox()


browser.get("http://adminold.itland.enes.tech/index.php/map")

username = browser.find_element_by_id('enter_login')
username.send_keys("")
passw = browser.find_element_by_id('enter_password')
passw.send_keys("")

m = browser.find_element_by_class_name('but_m')
print(m)
m.click()


# elem = driver.find_element_by_name("q")
# elem.send_keys("news")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()


