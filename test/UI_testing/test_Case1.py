import time

import requests

import pytest

from PageObjectModel.HomePage import HomePage
from PageObjectModel.ProductPage import ProductPage
from PageObjectModel.CaseTest import CaseTestPage
from PageObjectModel.SignUpLoginPage import SignUpLoginPage
from Utilities.BaseClass import BaseClass
from Utilities.api_helper import APIHelper

#This testcase is about registering new user id to the website, login and delete the account
class TestCase1(BaseClass):

    @pytest.mark.parametrize("name, email, password, title, birth_date, birth_month, birth_year, firstname, lastname, company, address1, address2, country, zipcode, state, city, mobile_number",
    [
        ("imam2", "imam14@gmail.com", "@123QWea","Mr", "23", "December", "1978", "jambu1", "jambu2", "APM", "12 TUAS WEST ROAD", "#07-06 PARKWAY PARADE", "Singapore", "Woodlands", "Singapura", "638378", "01190998765"
         )
    ])
    def test_register(self, name, email, password, title, birth_date, birth_month, birth_year, firstname, lastname, company, address1, address2, country, zipcode, state, city, mobile_number):
        # # Call the API to create the user first
        # api_helper = APIHelper()
        # api_response, json_response = api_helper.create_account(name, email, password, title, birth_date, birth_month,
        #                                                         birth_year, firstname, lastname, company, address1,
        #                                                         address2, country, zipcode, state, city, mobile_number)
        #
        # # Check if user creation via API was successful
        # assert api_response is not None, "Failed to connect to API"
        #
        # # Validate JSON response
        # print(json_response)
        # assert json_response.get(
        #     'responseCode') == 201, f"Expected responseCode 201, but got {json_response.get('responseCode')}"
        # assert json_response.get(
        #     'message') == "User created!", f"Expected message 'User created!', but got {json_response.get('message')}"
        #
        # # Extract JSON response
        # try:
        #     json_response = api_response.json()
        # except ValueError:
        #     pytest.fail("Response is not in JSON format")
        #
        #
        # #delete user
        # delete_response,json_delete_response = api_helper.delete_user(email, password)
        # # Check if user creation via API was successful
        # assert delete_response is not None, "Failed to connect to API"
        #
        # # Validate JSON response
        # print(json_delete_response)
        # assert json_delete_response.get(
        #     'responseCode') == 200, f"Expected responseCode 200, but got {json_delete_response.get('responseCode')}"
        # assert json_delete_response.get(
        #     'message') == "User created!", f"Expected message 'User created!', but got {json_delete_response.get('message')}"
        #
        # # Extract JSON response
        # try:
        #     json_delete_response = delete_response.json()
        # except ValueError:
        #     pytest.fail("Response is not in JSON format")



        # Proceed with UI_testing
        homepage = HomePage(self.driver)
        SignUp = SignUpLoginPage(self.driver)
        assert homepage.Image().is_displayed(), "Wrong URL"
        homepage.NavSignUP_Login().click()
        self.WaitElementPresent(SignUp.NewUserSignUp)

        assert SignUp.SignUpTxt().is_displayed(), "Wrong Page"
        SignUp.SignUpInsName().send_keys(name)
        SignUp.SignUpInsEmail().send_keys(email)
        SignUp.ClickSignUp()
        self.wait()
        if title == "Mr":
            SignUp.selectMrtitle().click()
        elif title == "Mrs":
            SignUp.selectMrstitle().click()

        SignUp.InsPassword().send_keys(password)
        SignUp.DateDays().send_keys(birth_date)
        SignUp.DateMonth().send_keys(birth_month)
        SignUp.DateYear().send_keys(birth_year)
        SignUp.ClickNews().click()
        SignUp.ClickOffer().click()
        SignUp.InsFirstName().send_keys(firstname)
        SignUp.InsLastName().send_keys(lastname)
        SignUp.InsCompanyName().send_keys(company)
        SignUp.InsAddress1().send_keys(address1)
        SignUp.InsAddress2().send_keys(address2)
        self.selectByText(SignUp.SelCountry(), country)
        SignUp.InsState().send_keys(state)
        SignUp.InsCity().send_keys(city)
        SignUp.InsZipCode().send_keys(zipcode)
        SignUp.InsMobileNum().send_keys(mobile_number)
        SignUp.ClickCreateAcc().click()
        assert SignUp.AccCreatedText().is_displayed(), "Account has not been created"
        SignUp.ClickContinue().click()
        assert homepage.ClickDelAcc().is_displayed(), "Not returning to homepage"
        homepage.ClickDelAcc().click()
        assert homepage.AccDeleted().is_displayed(), "Wrong click"
        SignUp.ClickContinue().click()
    @pytest.mark.parametrize(
        "email ,password,is_valid", [
        ("NurSyu@gmail.com", "@123QWea", True),
        ("MurSyu@gmail.com", "@123QWea", False)
            ]
    )
    def test_login_credentials(self, email, password, is_valid):
        self.getLogger().info("THis message is to notify that the test has just been started")
        self.getLogger().debug("Initializing HomePage and SignUpLoginPage objects with driver")
        homepage = HomePage(self.driver)
        SignUp = SignUpLoginPage(self.driver)
        self.getLogger().debug("Navigating to homepage")
        homepage.NavSignUP_Login().click()
        self.wait()

        SignUp.LogEmail().send_keys(email)
        SignUp.LogPassword().send_keys(password)
        SignUp.clickLogin().click()
        if is_valid:
            assert SignUp.SuccessfulLogin().is_displayed(), "Email is invalid"
        else:
            assert SignUp.ErrorLogin().is_displayed(), "Login should fail with invalid credentials"
        self.getLogger().info("THis message is to notify that the test has just been ended")

    """  
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
    """
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
        testcasepage = CaseTestPage(self.driver)
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

    @pytest.mark.flaky(reruns=3) #pip install pytest-rerunfailures
    def test_product(self):
        product = ProductPage(self.driver)
        product.NavToProductPage()
        self.wait()
        # self.WaitElement(product.waitImageDisplay()).is_displayed()
        self.ScrollPage()
        self.wait()

        # get all product elements
        product_item = []
        product_elements = product.DisplayProductNames()
        self.getLogger().info("this message to ensure the step occurred")

        if product_elements is not None:
            for i, product_element in enumerate(product_elements, start=1):
                product_name = product_element.text
                product_item.append(product_name)

                if i == 3:  # Only click if i is 3
                    view_product_element = self.page.clickViewProduct(i)
                    view_product_element.click()
                    break  # Exit the loop after clicking the third product

                print(f"Iteration {i}: No action needed")

            self.ScrollAndLoadAllProducts()
            print(product_item, flush=True)
        else:
            print("No element Found")

        # Reset scroll position
        self.driver.execute_script("window.scrollTo(0, 0);")

        # extract and print the text of each product
        # try:
        #     # product_elements = self.retry_action()
        # if product_elements is not None:
        #     for product_element in product_elements:
        #         product_name = product_element.text
        #
        #         #print(product_name)
        #         product_item.append(product_name)
        #         #self.getLogger().debug(f"to ensure all the item is printed {product_name}")
        #     self.ScrollAndLoadAllProducts()
        #     print(product_item, flush=True)
        # else:
        #     print("No element Found")
        # # except Exception as e:
        # #     print("All attempts failed")
        # self.driver.execute_script("window.scrollTo(0, 0);")
        #
        # # Iterate over a range of 1 to 34
        # for i in range(1, 35):
        #     # Ensure all products are loaded
        #     self.page.ScrollAndLoadAllProducts()
        #
        #     if i == 3:  # Only click if i is 3
        #         # Find and click the view product element
        #         view_product_element = self.page.clickViewProduct(i)
        #         view_product_element.click()
        #         break  # Exit the loop after clicking the third product
        #     else:
        #         print(f"Iteration {i}: No action needed")
        #
        # # Assert that the product image is displayed after the click
        # assert product.DisplayViewProductImg().is_displayed(), "Product image is not displayed"


    def test_searchProduct(self):
        product = ProductPage(self.driver)
        product.NavToProductPage()
        self.WaitElementPresent(product.Img)
        assert product.waitImageDisplay().is_displayed(), "wrong page"
        product.InputSearch().send_keys("Men")
        product.ClickSearchBtn()
        self.ScrollAndLoadAllProducts()

        # Add to cart all the search displayed.
        CartItem = []
        productCarts = product.DisplayProductCart()
        productnames = product.DisplayProductNames()
        if productCarts is not None:
            for productCart, productname in zip(productCarts, productnames):
                self.ActionMove(product.NavOverlayContent()).perform()
                self.WaitElementPresent(product.overlayContent)
                product_name = productname.text
                CartItem.append(product_name)
                print(f"Product Name: {product_name}")
                self.WaitElementClickable(product.AddtoCart)
                productCart.click()
                product.ClickContinueShoppingBtn()
                self.ScrollAndLoadAllProducts()

        else:
            print("No element was found")





































