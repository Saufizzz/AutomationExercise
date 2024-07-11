from selenium.webdriver.common.by import By

class CartPage:
    QuantityOfProduct = (By.XPATH,"//button[normalize-space()='5']")




    def __init__(self,driver):
        self.driver = driver

    def VerifyQuantity(self):
        return self.driver.find_element(*CartPage.QuantityOfProduct)