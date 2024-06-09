# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# import time
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
#
# This is for clicking the sidebar menu
# driver.find_element(By.XPATH,"//body/div[@class='sidebar clearfix']/ul[@class='sidebar-panel nav']/li[12]/a[1]").click()
# sidebar_element = driver.find_element(By.XPATH,"//div[@class='sidebar clearfix']")
# driver.execute_script("arguments[0].scrollBy(0,500)", sidebar_element)
# driver.implicitly_wait(5)
#
# driver.find_element(By.XPATH,"//a[@href='webexample']").click()
# driver.implicitly_wait(5)
# driver.execute_script("window.scrollBy(0,1000)")
#
#
#
# Assign example name to search inside the datatable
# expected_name = "name"
# xpath_text = "//td[2][normalize-space()='"+expected_name+"']"
#
# while True:
#     try:
#         # Check if the expected name exists on the current page
#         name_element = driver.find_element(By.XPATH, xpath_text)
#         if name_element.is_displayed():
#             print("Name found:", name_element.text)
#             break
#     except NoSuchElementException:
#         # If the name element is not found on the current page, scroll down to reveal more content
#         driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
#         # If the name element is not found on the current page, click on the next page
#         #actions = ActionChains(driver)
#         next_page_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//li[contains(@class,'active')]/following::a[1]")))
#         next_page_link.click()
#         driver.find_element(By.XPATH, "//li[contains(@class,'active')]/following::a[1]")
#         print("Next page link:", next_page_link)  # Add this line for debugging
#         # Wait for the page to load
#         time.sleep(5)