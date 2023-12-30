import json
from django.test import Client
from django.test.client import RequestFactory
from rest_framework_simplejwt.tokens import RefreshToken

# Replace with your Django superuser credentials
SUPERUSER_USERNAME = "admin"
SUPERUSER_PASSWORD = "oyindamola"

# Replace with the appropriate endpoint URL
TOKEN_URL = "/api/token/"
API_URL = "/api/physicians/"  # Change this to the actual endpoint you want to access

# Create a Django test client
client = Client()

# Obtain a JWT token
token_response = client.post(
    TOKEN_URL,
    data={"username": SUPERUSER_USERNAME, "password": SUPERUSER_PASSWORD},
    content_type="application/json",
)

if token_response.status_code == 200:
    token_data = json.loads(token_response.content)
    access_token = token_data.get("access")
    print("JWT Token obtained:", access_token)

    # Use the obtained token to make an authenticated request
    request_factory = RequestFactory()
    request = request_factory.get(API_URL)
    request.META["HTTP_AUTHORIZATION"] = f"Bearer {access_token}"

    # Make an authenticated request using the Django test client
    authenticated_response = client.get(API_URL, **request.META)
    print("Authenticated API Response:", authenticated_response.status_code)
    print(authenticated_response.content.decode("utf-8"))
else:
    print("Failed to obtain JWT Token. Status code:", token_response.status_code)
