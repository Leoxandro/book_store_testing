#####Visibility_of_item's_page#####
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
# shop_btn = driver.find_element_by_xpath("//a[contains(text(),'Shop')]").click()
# book_page = driver.find_element_by_css_selector(".post-181 > a > h3").click()
# book_title = WebDriverWait(driver,20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".product_title"), "HTML5 Forms"))
# driver.quit()

#####Quantity_of_items_visible#####
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
# shop_btn = driver.find_element_by_xpath("//a[contains(text(),'Shop')]").click()
# html_filter = driver.find_element_by_css_selector(".cat-item-19 > a").click()
# counter = driver.find_element_by_css_selector(".product-categories > li:nth-child(2) > span")
# counter_text = counter.text
# if counter_text == "(3)":
#     print("True")
# else:
#     print("False")
# driver.quit()

#####item_sorting#####
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
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
# shop_btn = driver.find_element_by_xpath("//a[contains(text(),'Shop')]").click()
# sortingDefault = driver.find_element_by_css_selector("[value='menu_order']")
# if sortingDefault.get_attribute("value") == "menu_order":
#     print("True")
# else:
#     print("False")
# sortingHL = driver.find_element_by_css_selector(".orderby")
# select = Select(sortingHL)
# select.select_by_value("price-desc")
# sortingDefault = driver.find_element_by_css_selector("[value='menu_order']")
# if sortingDefault.get_attribute("value") == "price-desc":
#     print("True")
# else:
#     print("False")
# driver.quit()


#####visibility,item's discount#####
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
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
# shop_btn = driver.find_element_by_xpath("//a[contains(text(),'Shop')]").click()
# driver.find_element_by_css_selector(".post-169 > a > h3").click()
#
# old_price = driver.find_element_by_xpath("//span[contains(text(), '600.00')]")
# old_price_numbers = old_price.text
# assert old_price_numbers == "₹600.00"
#
# new_price = driver.find_element_by_xpath("//span[contains(text(), '450.00')]")
# new_price_numbers = new_price.text
# assert new_price_numbers == "₹450.00"
#
# WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".images > a"))).click()
# WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close"))).click()
# driver.quit()


#####Price_check_in_cart#####
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
#
# driver = webdriver.Chrome("C:/chromedriver.exe")
# driver.get("http://practice.automationtesting.in/")
# driver.implicitly_wait(5)
# driver.maximize_window()
#
# shop_btn = driver.find_element_by_xpath("//a[contains(text(),'Shop')]").click()
# addBtn = driver.find_element_by_css_selector(".post-182 > a:nth-child(2)").click()
#
# time.sleep(3)
# total_items = driver.find_element_by_class_name("cartcontents")
# total_items_text = total_items.text
# assert total_items_text == "1 Item"
#
# total_sum = driver.find_element_by_css_selector(".wpmenucart-contents > .amount")
# total_sum_text = total_sum.text
# assert total_sum_text == "₹180.00"
#
# cartBtn = driver.find_element_by_class_name("wpmenucart-contents").click()
# subtotal = WebDriverWait(driver,20).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-collaterals .cart_totals .cart-subtotal .amount"), "₹180.00"))
# total = WebDriverWait(driver,20).until(
#     EC.text_to_be_present_in_element((By.XPATH, "//span[contains(text(),'189')]"), "₹189.00"))
# driver.quit()


#####Work_in_a_cart#####

# import time
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
# shop_btn = driver.find_element_by_xpath("//a[contains(text(),'Shop')]").click()
# scroll = driver.execute_script("window.scrollBy(0,300);")
# add1 = driver.find_element_by_css_selector("[data-product_id='182']").click()
# time.sleep(3)
# add2 = driver.find_element_by_css_selector("[data-product_id='180']").click()
#
# time.sleep(3)
#
# cart = driver.find_element_by_css_selector(".cartcontents").click()
# remove1 = driver.find_element_by_css_selector("[data-product_id='182']").click()
# time.sleep(3)
# undo = driver.find_element_by_xpath("//a[contains(text(),'Undo')]").click()
# time.sleep(3)
#
# qt = driver.find_element_by_xpath("//input[@max='9686']").clear()
# qt_changed = driver.find_element_by_css_selector("[name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']").send_keys("3")
#
# update_cart = driver.find_element_by_css_selector("[name='update_cart']").click()
# qt_result = driver.find_element_by_css_selector("[name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']").get_attribute("value")
# assert qt_result == "3"
#
# time.sleep(3)
# apply_c = driver.find_element_by_css_selector("[name='apply_coupon']").click()
# WebDriverWait(driver,20).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-error > li"), "Please enter a coupon code."))
# driver.quit()


#####buying_an_item#####

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("C:/chromedriver.exe")
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()

shop_btn = driver.find_element_by_xpath("//a[contains(text(),'Shop')]").click()
scroll = driver.execute_script("window.scrollBy(0,300);")
add1 = driver.find_element_by_css_selector("[data-product_id='182']").click()
time.sleep(1)
cart = driver.find_element_by_class_name("cartcontents").click()
time.sleep(3)
proceedBtn = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Proceed to')]")))
proceedBtn_click = driver.find_element_by_xpath("//a[contains(text(),'Proceed to')]").click()

name_box = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#billing_first_name")))
name_box_click = driver.find_element_by_id("billing_first_name").send_keys("Alex")
time.sleep(1)
last_name_box = driver.find_element_by_id("billing_last_name").send_keys("Karpov")
time.sleep(1)
email_box = driver.find_element_by_css_selector("#billing_email").send_keys("Leoxandro@yandex.ru")
time.sleep(1)
phone_box = driver.find_element_by_id("billing_phone").send_keys("89112060365")
time.sleep(1)
country_selector = driver.find_element_by_id("select2-chosen-1").click()
time.sleep(1)
country_placeholder = driver.find_element_by_id("s2id_autogen1_search").send_keys("Russia")
time.sleep(1)
country_choice = driver.find_element_by_xpath("//span[@class='select2-match']").click()
time.sleep(1)
address_box = driver.find_element_by_id("billing_address_1").send_keys("Savushkina St, 31-13")
town_box = driver.find_element_by_id("billing_city").send_keys("Saint-Petersburg")
state_box = driver.find_element_by_id("billing_state").send_keys("SPB")
postcode_box = driver.find_element_by_id("billing_postcode").send_keys("197183")

scroll1 = driver.execute_script("window.scrollBy(0,600);")
time.sleep(2)
checkbox = driver.find_element_by_id("payment_method_cheque").click()
time.sleep(3)
place_orderBtn = driver.find_element_by_css_selector("#place_order").click()
time.sleep(1)
visible_text1 = WebDriverWait(driver,5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
visible_text2 = WebDriverWait(driver,5).until(EC.text_to_be_present_in_element((By.XPATH, "//td[contains(text(),'Check')]"), "Check Payments"))
driver.quit()