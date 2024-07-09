#Usage of API request response

# Introduction to pytest: Learn the basics of writing and running tests using pytest.
# Assertions: Use assertions to validate API responses.
# Fixtures: Understand and use fixtures for setup and teardown of test environments.
# Parametrization: Use parameterized tests to run the same test with different data.
# Mocking: Mock external services and dependencies using libraries like pytest-mock or unittest.mock


# Attributes
# .status_code: HTTP status code of the response (e.g., 200, 404).
#
# .headers: Dictionary of response headers.
#
# .text: Content of the response, in Unicode.
#
# .content: Raw content of the response, in bytes.
#
# .json(): Method to parse JSON response content into a Python dictionary.
#
# .url: Final URL after any redirects.
#
# .encoding: Encoding of the response content.
#
# .cookies: CookieJar object holding cookies sent back by the server.
#
# .history: List of Response objects for the history of request redirects.
#
# Methods
# .raise_for_status(): Raise an exception based on the status code if the request was unsuccessful.
#
# .close(): Close the underlying network connection.


#
# import requests
#
# # Example GET request
# response = requests.get('https://api.example.com/data')
#
# # Accessing attributes
# print(response.status_code)   # HTTP status code
# print(response.headers)       # Response headers
# print(response.text)          # Response content as a string (Unicode)
# print(response.content)       # Response content as bytes
#
# # Parsing JSON response
# data = response.json()
# print(data)
#
# # Accessing cookies
# print(response.cookies)
#
# # Accessing final URL
# print(response.url)
#
# # Checking for redirects history
# print(response.history)



# Additional Response Attributes and Methods
# Timeouts and Retries:
#
# requests.exceptions.RequestException: Exception raised for all requests-related exceptions.
# .elapsed: Time taken for the server to respond, as a timedelta object.
# Response Headers:
#
# .headers: Returns a dictionary of HTTP headers sent by the server.
# Response Encoding:
#
# .encoding: Character encoding of the response content.
# Redirection and History:
#
# .history: List of response objects for all previous requests if redirection occurred.
# .is_redirect: Checks if the response is a redirect.
# Cookies:
#
# .cookies: CookieJar object containing cookies sent by the server.
# .cookie.items(): Returns a list of all cookies, in name-value tuple format.
# Error Handling:
#
# .raise_for_status(): Raises an HTTPError for an unsuccessful response (i.e., a response with an error status code).
# .ok: Boolean indicating if the response was successful (status code < 400).


# import requests
#
# # Example GET request
# response = requests.get('https://api.example.com/data', timeout=5)
#
# # Accessing additional attributes
# print(response.elapsed)       # Time taken for the server to respond
# print(response.headers)       # Response headers
# print(response.is_redirect)   # Check if the response is a redirect
#
# # Accessing cookies
# print(response.cookies.items())   # List of cookies sent by the server
#
# # Error handling
# try:
#     response.raise_for_status()
# except requests.exceptions.HTTPError as err:
#     print(f"HTTP error occurred: {err}")
