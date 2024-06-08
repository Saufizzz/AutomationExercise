from selenium.webdriver.common.by import By


class ProductPage:

    ProductLink = (By.XPATH,"//a[@href='/products']")
    Search = (By.XPATH,"//input[@id='search_product']")
    Img = (By.XPATH,"//img[@id='sale_image']")
    SearchBtn = (By.XPATH,"//button[@id='submit_search']")
    womenLink = (By.XPATH,"//a[normalize-space()='Women']")

    def __init__(self,driver):
        self.driver = driver

