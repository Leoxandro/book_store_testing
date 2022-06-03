#####AddingComment#####
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome("C:/chromedriver.exe")
# driver.get("http://practice.automationtesting.in/")
# driver.implicitly_wait(5)
# driver.maximize_window()
# driver.execute_script("window.scrollBy(0,600);")
# driver.find_element_by_css_selector("[title='Selenium Ruby']").click()
# driver.find_element_by_xpath("//a[contains(text(), 'Reviews')]").click()
# star = driver.find_element_by_class_name("star-5").click()
# review = driver.find_element_by_id("comment").send_keys("Nice book!")
# name = driver.find_element_by_id("author").send_keys("Alex")
# email = driver.find_element_by_id("email").send_keys("leoxandro@yandex.ru")
# submit_btn = driver.find_element_by_id("submit").click()
# driver.quit()