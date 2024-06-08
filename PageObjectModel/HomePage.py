from selenium.webdriver.common.by import By


class HomePage:
    HomeImage = (By.XPATH,"//img[@alt='Website for automation practice']")
    Home = (By.XPATH,"//a[normalize-space()='Home']")
    Product = (By.XPATH,"//a[@href='/products']")
    Cart = (By.XPATH,"//a[normalize-space()='Cart']")
    SignUp_Login = (By.XPATH,"//a[normalize-space()='Signup / Login']")
    DeleteAccount = (By.XPATH,"//a[normalize-space()='Delete Account']")
    AccDeletedText = (By.XPATH,"//b[normalize-space()='Account Deleted!']")
    LogoutLink = (By.XPATH,"//a[normalize-space()='Logout']")
    TestCaseLink = (By.XPATH,"//a[normalize-space()='Test Cases']")






    def __init__(self,driver):
        self.driver = driver

    def Image(self):
        return self.driver.find_element(*HomePage.HomeImage)

    def NavHome(self):
        return self.driver.find_element(*HomePage.Home)

    def NavProduct(self):
        return self.driver.find_element(*HomePage.Product)

    def NavCart(self):
        return self.driver.find_element(*HomePage.Cart)

    def NavSignUP_Login(self):
        return self.driver.find_element(*HomePage.SignUp_Login)

    def ClickDelAcc(self):
        return self.driver.find_element(*HomePage.DeleteAccount)

    def AccDeleted(self):
        return self.driver.find_element(*HomePage.AccDeletedText)

    def ClickLogout(self):
        return self.driver.find_element(*HomePage.LogoutLink)

    def ClickTestCase(self):
        return self.driver.find_element(*HomePage.TestCaseLink)

