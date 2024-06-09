from selenium.webdriver.common.by import By


class CaseTestPage:
    TestCaseImage = (By.XPATH,"//b[normalize-space()='Test Cases']")
    """f"//section[@id='form']//div[@class='container']//u[@xpath='{i}']"""


    def __init__(self,driver):
        self.driver = driver

    def TCImagePresent(self):
        return self.driver.find_element(*CaseTestPage.TestCaseImage)

    def TestList(self):
        xpath_expression = f"//section[@id='form']//h4[@class='panel-title']"
        return self.driver.find_elements(By.XPATH, xpath_expression)
