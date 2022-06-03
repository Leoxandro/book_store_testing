#####AccountRegistration#####
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome("C:/chromedriver.exe")
# driver.get("http://practice.automationtesting.in/")
# driver.implicitly_wait(5)
# driver.maximize_window()
#
# driver.find_element(By.XPATH, "//a[contains(text(),'My Account')]").click()
# driver.find_element(By.CSS_SELECTOR, "#reg_username").send_keys("leoxandro@yandex.ru")
# driver.find_element(By.CSS_SELECTOR, "#reg_password").send_keys("SlM2h23267274_")
# driver.find_element(By.CSS_SELECTOR, "[value='Register']").click()
# driver.quit()


#####LogIn#####
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome("C:/chromedriver.exe")
# driver.get("http://practice.automationtesting.in/")
# driver.implicitly_wait(5)
# driver.maximize_window()
#
# driver.find_element(By.XPATH, "//a[contains(text(),'My Account')]").click()
# driver.find_element(By.CSS_SELECTOR, "#username").send_keys("leoxandro@yandex.ru")
# driver.find_element(By.CSS_SELECTOR, "#password").send_keys("SlM2h23267274_")
# driver.find_element(By.CSS_SELECTOR, "[value='Login']").click()
#
# WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Logout')]")))
# driver.quit()