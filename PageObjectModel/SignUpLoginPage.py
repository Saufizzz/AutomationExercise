
from selenium.webdriver.common.by import By


class SignUpLoginPage:
    name = "NurSyuda"
    email = "NurSyuda@gmail.com"
    password = "@123QWea"



    SignUpName = (By.XPATH,"//input[@placeholder='Name']")
    SignUpEmail = (By.XPATH,"//input[@data-qa='signup-email']")
    SignUp =(By.XPATH,"//button[normalize-space()='Signup']")
    LoginEmail = (By.XPATH,"//input[@data-qa='login-email']")
    LoginPassword = (By.XPATH,"//input[@placeholder='Password']")
    Login = (By.XPATH,"//button[normalize-space()='Login']")
    MrTitle = (By.XPATH,"//input[@id='id_gender1']")
    MrsTitle = (By.XPATH, "//input[@id='id_gender2']")
    AccountName = (By.XPATH,"//input[@id='name']")
    AccountEmail = (By.XPATH,"//input[@id='email']")
    AccountPassword = (By.XPATH,"//input[@id='password']")
    DOBDays = (By.XPATH,"//select[@id='days']")
    DOBMonth = (By.XPATH,"//select[@id='months']")
    DOBYear = (By.XPATH,"//select[@id='years']")
    AddressFirstName = (By.XPATH,"//input[@id='first_name']")
    AddressLastName = (By.XPATH,"//input[@id='last_name']")
    Company = (By.XPATH,"//input[@id='company']")
    Address1 = (By.XPATH,"//input[@id='address1']")
    Address2 = (By.XPATH,"//input[@id='address2']")
    Country = (By.XPATH,"//select[@id='country']")
    State = (By.XPATH,"//input[@id='state']")
    City = (By.XPATH,"//input[@id='city']")
    Zipcode = (By.XPATH,"//input[@id='zipcode']")
    MobileNumber = (By.XPATH,"//input[@id='mobile_number']")
    CreateAccount = (By.XPATH,"//button[normalize-space()='Create Account']")
    AccountCreatedNoti = (By.XPATH,"//b[normalize-space()='Account Created!']")
    AccountPara1 = (By.XPATH,"//p[contains(text(),'Congratulations! Your new account has been success')]")
    AccountPara2 = (By.XPATH,"//p[contains(text(),'You can now take advantage of member privileges to')]")
    Continue = (By.XPATH,"//a[normalize-space()='Continue']")
    NewUserSignUp = (By.XPATH,"//h2[normalize-space()='New User Signup!']")
    AccountText = (By.XPATH,"//b[normalize-space()='Enter Account Information']")
    NewsCheckBox = (By.XPATH,"//input[@id='newsletter']")
    OffersCheckBox = (By.XPATH,"//input[@id='optin']")
    CredentialError = (By.XPATH,"//p[normalize-space()='Your email or password is incorrect!']")
    CredentialValid = (By.XPATH,"//b[normalize-space()='NurSyu']")
    ExistingEmailNoti = (By.XPATH,"//p[normalize-space()='Email Address already exist!']")

    def __init__(self,driver):
        self.driver = driver
    def SignUpInsName(self):
        return self.driver.find_element(*SignUpLoginPage.SignUpName)

    def SignUpInsEmail(self):
        return self.driver.find_element(*SignUpLoginPage.SignUpEmail)

    def ClickSignUp(self):
        self.driver.find_element(*SignUpLoginPage.SignUp).click()

    def SignUpTxt(self):
        return self.driver.find_element(*SignUpLoginPage.NewUserSignUp)

    def selectMrtitle(self):
        return self.driver.find_element(*SignUpLoginPage.MrTitle)

    def selectMrstitle(self):
        return self.driver.find_element(*SignUpLoginPage.MrsTitle)
    # def SelectTitle(self):
    #     if "Muhammad" in SignUpLoginPage.name:
    #          return self.driver.find_element(*SignUpLoginPage.MrTitle)
    #     elif "Nur" in SignUpLoginPage.name:
    #          return self.driver.find_element(*SignUpLoginPage.MrsTitle)
    #     else:
    #         return self.driver.find_element(*SignUpLoginPage.MrTitle)

    def AccText(self):
        return self.driver.find_element(*SignUpLoginPage.AccountText)

    def AccName(self):
        return self.driver.find_element(*SignUpLoginPage.AccountName)

    def InsPassword(self):
        return self.driver.find_element(*SignUpLoginPage.AccountPassword)

    def DateDays(self):
        return self.driver.find_element(*SignUpLoginPage.DOBDays)

    def DateMonth(self):
        return self.driver.find_element(*SignUpLoginPage.DOBMonth)

    def DateYear(self):
        return self.driver.find_element(*SignUpLoginPage.DOBYear)

    def ClickNews(self):
        return self.driver.find_element(*SignUpLoginPage.NewsCheckBox)

    def ClickOffer(self):
        return self.driver.find_element(*SignUpLoginPage.OffersCheckBox)

    def InsFirstName(self):
        return self.driver.find_element(*SignUpLoginPage.AddressFirstName)

    def InsLastName(self):
        return self.driver.find_element(*SignUpLoginPage.AddressLastName)

    def InsCompanyName(self):
        return self.driver.find_element(*SignUpLoginPage.Company)

    def InsAddress1(self):
        return self.driver.find_element(*SignUpLoginPage.Address1)

    def InsAddress2(self):
        return self.driver.find_element(*SignUpLoginPage.Address2)

    def SelCountry(self):
        return self.driver.find_element(*SignUpLoginPage.Country)

    def InsState(self):
        return self.driver.find_element(*SignUpLoginPage.State)

    def InsCity(self):
        return self.driver.find_element(*SignUpLoginPage.City)

    def InsZipCode(self):
        return self.driver.find_element(*SignUpLoginPage.Zipcode)

    def InsMobileNum(self):
        return self.driver.find_element(*SignUpLoginPage.MobileNumber)

    def ClickCreateAcc(self):
        return self.driver.find_element(*SignUpLoginPage.CreateAccount)

    def AccCreatedText(self):
        return self.driver.find_element(*SignUpLoginPage.AccountCreatedNoti)

    def ClickContinue(self):
        return self.driver.find_element(*SignUpLoginPage.Continue)

    def LogEmail(self):
        return self.driver.find_element(*SignUpLoginPage.LoginEmail)

    def LogPassword(self):
        return  self.driver.find_element(*SignUpLoginPage.LoginPassword)

    def clickLogin(self):
        return self.driver.find_element(*SignUpLoginPage.Login)

    def ErrorLogin(self):
        return self.driver.find_element(*SignUpLoginPage.CredentialError)

    def SuccessfulLogin(self):
        return self.driver.find_element(*SignUpLoginPage.CredentialValid)

    def NotiEmailExisted(self):
        return self.driver.find_element(*SignUpLoginPage.ExistingEmailNoti)


