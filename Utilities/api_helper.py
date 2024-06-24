# api_helpers.py
import requests

def create_user(name, email, password):
    url = "https://example.com/api/register"
    payload = {
        "name": name,
        "email": email,
        "password": password
    }
    response = requests.post(url, json=payload)
    return response

def get_user(email):
    url = f"https://example.com/api/users?email={email}"
    response = requests.get(url)
    return response

def delete_user(user_id):
    url = f"https://example.com/api/users/{user_id}"
    response = requests.delete(url)
    return response
