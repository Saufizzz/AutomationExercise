# test pagination
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# # what this method do is to extract the number of maximum pages in a pagination.
# driver = webdriver.Chrome()
# pages_text = driver.find_element(By.XPATH, "//div[contains(text(),'Showing 1 to 6')]").text
# # this method will extract the first index of the text starting with (+1 which is number
# start_index = pages_text.index("(") + 1
# # this method will extract the last index of the text starting with the Pages)-1 which when combine will provde number of maximum pages.
# end_index = pages_text.index("Pages)") - 1
# pages = int(pages_text[start_index:end_index])
#
# expected_program = "dsafa"
# xpath_text = "//td[5][normalize-space()='" + expected_program + "']"
# program_names = driver.find_elements(By.XPATH, "//td[5][normalize-space()='" + expected_program + "']")
#
# for i, page in enumerate(pages, start=1):
#     try:
#         if driver.find_element(By.XPATH, xpath_text).is_displayed():
#             button = driver.find_element(By.XPATH, xpath_text + "/following-sibling::td[3]")
#             button.click()
#             break
#     except NoSuchElementException:
#         pass
#
#     driver.find_element(By.XPATH, "//li[contains(@class,'active')]/following::a[1]").click()