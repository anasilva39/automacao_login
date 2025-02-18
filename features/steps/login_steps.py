from behave import given, when, then
import requests

BASE_URL = "https://petstore.swagger.io/v2/user"

@given('que eu crio um novo usuário com nome "{username}" e senha "{password}"')
def step_create_user(context, username, password):
    print(f"Creating user: {username}")
    context.username = username
    context.password = password
    payload = {
        "id": 0,
        "username": username,
        "firstName": "Test",
        "lastName": "User",
        "email": "testuser@example.com",
        "password": password,
        "phone": "1234567890",
        "userStatus": 0
    }
    context.response = requests.post(BASE_URL, json=payload)

@when('eu envio uma requisição POST para "/user"')
def step_send_post_request(context):
    print(f"Sending POST request for user: {context.username}")
    payload = {
        "id": 0,
        "username": context.username,
        "firstName": "Test",
        "lastName": "User",
        "email": "testuser@example.com",
        "password": context.password,
        "phone": "1234567890",
        "userStatus": 0
    }
    context.response = requests.post(BASE_URL, json=payload)

@given('que tenho um usuário existente com nome "{username}"')
def step_have_existing_user(context, username):
    print(f"Ensuring user exists: {username}")
    context.username = username
    context.password = "senha123"
    payload = {
        "id": 0,
        "username": username,
        "firstName": "Test",
        "lastName": "User",
        "email": "testuser@example.com",
        "password": context.password,
        "phone": "1234567890",
        "userStatus": 0
    }
    requests.post(BASE_URL, json=payload)

@when('eu envio uma requisição GET para "/user/{username}"')
def step_send_get_request(context, username):
    print(f"Sending GET request for user: {username}")
    context.response = requests.get(f"{BASE_URL}/{username}")

@when('eu envio uma requisição PUT para "/user/{username}" com nova senha "{new_password}"')
def step_send_put_request(context, username, new_password):
    print(f"Sending PUT request for user: {username}")
    payload = {
        "password": new_password
    }
    context.response = requests.put(f"{BASE_URL}/{username}", json=payload)

@when('eu envio uma requisição DELETE para "/user/{username}"')
def step_send_delete_request(context, username):
    print(f"Sending DELETE request for user: {username}")
    context.response = requests.delete(f"{BASE_URL}/{username}")

@then('devo receber uma resposta {status_code}')
def step_check_response(context, status_code):
    print(f"Checking response, expected: {status_code}, got: {context.response.status_code}")
    assert context.response.status_code == int(status_code), f"Esperado {status_code}, mas recebeu {context.response.status_code}"
