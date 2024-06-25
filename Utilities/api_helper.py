# api_helpers.py
import requests
# utilities/api_helper.py
from test.conftest import base_url
import requests

class APIHelper:

    def create_account(self, name, email, password, title, birth_date, birth_month, birth_year, firstname, lastname, company, address1, address2, country, zipcode, state, city, mobile_number):
        url = f"{base_url}/api/createAccount"
        headers = {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        data = {
            'name': name,
            'email': email,
            'password': password,
            'title': title,
            'birth_date': birth_date,
            'birth_month': birth_month,
            'birth_year': birth_year,
            'firstname': firstname,
            'lastname': lastname,
            'company': company,
            'address1': address1,
            'address2': address2,
            'country': country,
            'zipcode': zipcode,
            'state': state,
            'city': city,
            'mobile_number': mobile_number
            }

        print(f"Sending data to API: {data}")  # Log the data being sent
        response = requests.post(url, headers=headers, data=data)
        print(f"API response: {response.status_code}, {response.text}")  # Log the response


        json_response = None
        try:
            # Assert the status code
            assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

            # Extract and verify the JSON response
            json_response = response.json()
            assert json_response[
                       'responseCode'] == 201, f"Expected responseCode 201, but got {json_response['responseCode']}"
            assert json_response[
                       'message'] == "User created!", f"Expected message 'User created!', but got {json_response['message']}"

        except (AssertionError, ValueError) as e:
            print(f"Assertion or JSON parsing error: {e}")
        return response,json_response


    def get_user(email):
        url = f"{base_url}/api/users?email={email}"
        response = requests.get(url)
        return response

    def delete_user(self,email, password):
        url = f"{base_url}/api/deleteAccount"
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = {
            "email" : email,
            "password" : password
        }
        delete_response = requests.delete(url, headers=headers)
        json_delete_response = None
        try:
            assert delete_response.status_code == 200, f"Expected status code 200, but got {delete_response.status_code}"
            #extract value json and verify json response
            json_delete_response = delete_response.json()
            assert json_delete_response['responseCode'] == 200, f"Expected responseCode 200, but got {json_delete_response['responseCode']}"
            assert json_delete_response['message'] == "Account deleted!", f"Expectedt message 'Account deleted!, but got {delete_response['message']}"
        except (AssertionError, ValueError) as e:
            print(f"Assertion or JSON parsing error: {e}")
        return delete_response,json_delete_response
