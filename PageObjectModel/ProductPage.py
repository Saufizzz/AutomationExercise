from selenium.webdriver.common.by import By


class ProductPage:

    ProductLink = (By.XPATH,"//a[@href='/products']")
    Search = (By.XPATH,"//input[@id='search_product']")
    Img = (By.XPATH,"//img[@id='sale_image']")
    SearchBtn = (By.XPATH,"//button[@id='submit_search']")
    womenLink = (By.XPATH,"//a[normalize-space()='Women']")
    ListWomenItem = (By.XPATH,"//div[@id='Women']//div[@class='panel-body']/ul/li")
    ViewProductItemImg = (By.XPATH,"//div[@class='view-product']//img[@alt='ecommerce website products']")

    def __init__(self,driver):
        self.driver = driver

    def NavToProductPage(self):
        self.driver.find_element(*ProductPage.ProductLink).click()

    def waitImageDisplay(self):
        self.driver.find_element(*ProductPage.Img)

    def DisplayListWomenItem(self):
        self.driver.find_element(*ProductPage.womenLink).click()
        return self.driver.find_elements(*ProductPage.ListWomenItem)

    def DisplayProductNames(self):
        product_names_xpath = "//div[@class='col-sm-4']/div[@class='product-image-wrapper']//p"
        product_elements = self.driver.find_elements(By.XPATH, product_names_xpath)
        return product_elements

    def clickViewProduct(self,i):
        ViewProductXpath = f"//div[{i}]//div[1]//div[2]//ul[1]//li[1]//a[1]//i[1]"
        ViewProduct = self.driver.find_element(By.XPATH,ViewProductXpath)
        return ViewProduct

    def DisplayViewProductImg(self):
        return self.driver.find_element(*ProductPage.ViewProductItemImg)

