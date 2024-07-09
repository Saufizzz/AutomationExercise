from selenium.webdriver.common.by import By


class ProductPage:

    ProductLink = (By.XPATH,"//a[@href='/products']")
    Search = (By.XPATH,"//input[@id='search_product']")
    Img = (By.XPATH,"//img[@id='sale_image']")
    SearchBtn = (By.XPATH,"//button[@id='submit_search']")
    womenLink = (By.XPATH,"//a[normalize-space()='Women']")
    ListWomenItem = (By.XPATH,"//div[@id='Women']//div[@class='panel-body']/ul/li")
    ViewProductItemImg = (By.XPATH,"//div[@class='view-product']//img[@alt='ecommerce website products']")
    AddtoCart = (By.XPATH,"//div[@class='col-sm-9 padding-right']//div//div[1]//div[1]//div[2]//div[1]//a[1]")
    TextAfterAddtoCart = (By.XPATH,"//p[normalize-space()='Your product has been added to cart.']")
    ContinueShoppingbtn = (By.XPATH,"//button[normalize-space()='Continue Shopping']")
    overlayContent = (By.XPATH,"//div[@class='product-overlay']")

    def __init__(self,driver):
        self.driver = driver

    def NavToProductPage(self):
        self.driver.find_element(*ProductPage.ProductLink).click()

    def waitImageDisplay(self):
        return self.driver.find_element(*ProductPage.Img)

    def DisplayListWomenItem(self):
        self.driver.find_element(*ProductPage.womenLink).click()
        return self.driver.find_elements(*ProductPage.ListWomenItem)

    def DisplayProductNames(self):
        product_names_xpath = "//div[@class='productinfo text-center']/p"
        product_elements = self.driver.find_elements(By.XPATH, product_names_xpath)
        return product_elements

    def DisplayProductCart(self):
        product_CartBtn_XPATH = "//div[@class='productinfo text-center']/a"
        product_CartBtn = self.driver.find_elements(By.XPATH, product_CartBtn_XPATH)
        return product_CartBtn

    def clickViewProduct(self,i):
        ViewProductXpath = f"//div[{i}]//div[1]//div[2]//ul[1]//li[1]//a[1]//i[1]"
        ViewProduct = self.driver.find_elements(By.XPATH,ViewProductXpath)
        return ViewProduct


    def DisplayViewProductImg(self):
        return self.driver.find_element(*ProductPage.ViewProductItemImg)

    def InputSearch(self):
        return self.driver.find_element(*ProductPage.Search)

    def ClickSearchBtn(self):
        self.driver.find_element(*ProductPage.SearchBtn).click()

    def ClickAddtoCart(self):
        self.driver.find_element(*ProductPage.AddtoCart).click()

    def DisplayTextAfterAddtoCart(self):
        return self.driver.find_element(*ProductPage.TextAfterAddtoCart)

    def ClickContinueShoppingBtn(self):
        self.driver.find_element(*ProductPage.ContinueShoppingbtn).click()

    def NavOverlayContent(self):
        return self.driver.find_element(*ProductPage.overlayContent)


