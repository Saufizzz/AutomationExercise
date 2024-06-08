import email

from PageObjectModel.HomePage import HomePage
from PageObjectModel.TestCase import TestCasePage
from PageObjectModel.SignUpLoginPage import SignUpLoginPage
from Utilities.BaseClass import BaseClass

#This testcase is about registering new user id to the website, login and delete the account
class TestCase1(BaseClass):
    def test_register(self):
        homepage = HomePage(self.driver)
        assert homepage.Image().is_displayed,"Wrong URl"
        homepage.NavSignUP_Login().click()
        self.wait()
        SignUp = SignUpLoginPage(self.driver)
        assert SignUp.SignUpTxt().is_displayed(), "Wrong Page"
        SignUp.SignUpInsName().send_keys(SignUp.name)
        SignUp.SignUpInsEmail().send_keys(SignUp.email)
        SignUp.ClickSignUp()
        self.wait()
        SignUp.SelectTitle().click()
        SignUp.InsPassword().send_keys(SignUp.password)
        SignUp.DateDays().send_keys("21")
        SignUp.DateMonth().send_keys("December")
        SignUp.DateYear().send_keys("1978")
        SignUp.ClickNews().click()
        SignUp.ClickOffer().click()
        SignUp.InsFirstName().send_keys(SignUp.name)
        SignUp.InsLastName().send_keys("Shawarma")
        SignUp.InsCompanyName().send_keys("Zanko")
        SignUp.InsAddress1().send_keys("12 TUAS WEST ROAD")
        SignUp.InsAddress2().send_keys("#07-06 PARKWAY PARADE")
        self.selectByText(SignUp.SelCountry(), "Singapore")
        SignUp.InsState().send_keys("Woodlands")
        SignUp.InsCity().send_keys("Singapura")
        SignUp.InsZipCode().send_keys("638378")
        SignUp.InsMobileNum().send_keys("01190998765")
        SignUp.ClickCreateAcc().click()
        assert SignUp.AccCreatedText().is_displayed(), "Account Has not been created"
        SignUp.ClickContinue().click()
        assert homepage.ClickDelAcc().is_displayed(),"not returning to homepage"
        homepage.ClickDelAcc().click()
        assert homepage.AccDeleted().is_displayed(), "Wrong click"
        SignUp.ClickContinue().click()


    def test_login_valid_credentials(self):
        self.getLogger().info("THis message is to notify that the test has just been started")
        self.getLogger().debug("Initializing HomePage and SignUpLoginPage objects with driver")
        homepage = HomePage(self.driver)
        SignUp = SignUpLoginPage(self.driver)

        self.getLogger().debug("Navigating to homepage")
        homepage.NavSignUP_Login().click()
        self.wait()

        SignUp.LogEmail().send_keys("NurSyu@gmail.com")
        SignUp.LogPassword().send_keys("@123QWea")
        SignUp.clickLogin().click()
        self.getLogger().debug("Check if the loginPage has name visible")
        assert SignUp.SuccessfulLogin().is_displayed(), "Email is invalid"
        self.getLogger().info("THis message is to notify that the test has just been ended")

    def test_login_invalid_credentials(self):
        self.getLogger().info("THis message is to notify that the test has just been started")
        self.getLogger().debug("Initializing HomePage and SignUpLoginPage objects with driver")
        homepage = HomePage(self.driver)
        SignUp = SignUpLoginPage(self.driver)

        self.getLogger().debug("Navigating to homepage")
        homepage.NavSignUP_Login().click()
        self.wait()
        SignUp.LogEmail().send_keys("MurSyu@gmail.com")
        SignUp.LogPassword().send_keys("@123QWea")
        SignUp.clickLogin().click()

        self.getLogger().debug("Check if the error message is displayed")
        assert SignUp.ErrorLogin().is_displayed(), "Email is invalid"
        self.getLogger().info("THis message is to notify that the test has just been ended")

    def test_existing_email_register(self):
        homepage = HomePage(self.driver)
        SignUp = SignUpLoginPage(self.driver)
        homepage.NavSignUP_Login().click()
        self.wait()
        SignUp.SignUpInsName().send_keys(SignUp.name)
        SignUp.SignUpInsEmail().send_keys(SignUp.email)
        SignUp.ClickSignUp().click()
        assert SignUp.NotiEmailExisted().is_displayed(), "Email can be register"

    def test_verify_test_case_visible(self):
        SignUp = SignUpLoginPage(self.driver)
        homepage = HomePage(self.driver)
        testcasepage = TestCasePage(self.driver)
        homepage.NavSignUP_Login().click()
        self.wait()
        SignUp.LogEmail().send_keys("NurSyu@gmail.com")
        SignUp.LogPassword().send_keys("@123QWea")
        SignUp.clickLogin().click()
        assert homepage.ClickTestCase().is_displayed(),"System not navigated to homepage"
        self.getLogger().debug("Check if the testcase link is clickable")
        homepage.ClickTestCase().click()
        assert testcasepage.TCImagePresent().is_displayed(), "Wrong page navigated"

        elements = testcasepage.TestList()
        for i, element in enumerate(elements, start=1):
            print(f"Element {i} content: {element.text}")






















