import pytest

from Utilities.api_helper import APIHelper


class APITesting:
    @pytest.mark.parametrize(
        "name, email, password, title, birth_date, birth_month, birth_year, firstname, lastname, company, address1, address2, country, zipcode, state, city, mobile_number",
        [
            ("imam2", "imam14@gmail.com", "@123QWea", "Mr", "23", "December", "1978", "jambu1", "jambu2", "APM",
             "12 TUAS WEST ROAD", "#07-06 PARKWAY PARADE", "Singapore", "Woodlands", "Singapura", "638378",
             "01190998765"
             )
        ])

    def test_create_api(self, name, email, password, title, birth_date, birth_month, birth_year, firstname, lastname, company, address1, address2, country, zipcode, state, city, mobile_number):
        api_helper = APIHelper()
        api_response,json_response = APIHelper.create_account(self, name, email, password, title, birth_date, birth_month, birth_year, firstname, lastname, company, address1, address2, country, zipcode, state, city, mobile_number)

        assert api_response is not None, "Failed to connect to API"
        # Validate JSON response
        print(json_response)
        assert json_response.get(
            'responseCode') == 201, f"Expected responseCode 201, but got {json_response.get('responseCode')}"
        assert json_response.get(
            'message') == "User created!", f"Expected message 'User created!', but got {json_response.get('message')}"

        # Extract JSON response
        try:
            json_response = api_response.json()
            print(json_response)
        except ValueError:
            pytest.fail("Response is not in JSON format")

    @pytest.mark.parametrize(
        "email, password"[
            ("imam14@gmail.com", "@123QWea")
        ])
    def test_delete_api(self,email,password):
        api_helper = APIHelper()
        # delete user
        delete_response, json_delete_response = api_helper.delete_user(email, password)
        # Check if user creation via API was successful
        assert delete_response is not None, "Failed to connect to API"

        # Validate JSON response
        print(json_delete_response)
        assert json_delete_response.get(
            'responseCode') == 200, f"Expected responseCode 200, but got {json_delete_response.get('responseCode')}"
        assert json_delete_response.get(
            'message') == "User created!", f"Expected message 'User created!', but got {json_delete_response.get('message')}"

        # Extract JSON response
        try:
            json_delete_response = delete_response.json()
        except ValueError:
            pytest.fail("Response is not in JSON format")

