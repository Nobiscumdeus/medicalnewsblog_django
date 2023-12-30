import requests

def obtain_token(username, password):
    token_url = 'http://localhost:8000/api/token/'
    token_data = {'username': username, 'password': password}

    try:
        response = requests.post(token_url, data=token_data)

        # Check if the request was successful (status code 200)
        response.raise_for_status()

        # Parse the JSON response to get the token
        token = response.json().get('token')
        return token

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")

    return None

def make_authenticated_request(token):
    if token:
        headers = {'Authorization': f'Token {token}'}
        posts_url = 'http://localhost:8000/api/posts/'

        try:
            response = requests.get(posts_url, headers=headers)

            # Check if the request was successful (status code 200)
            response.raise_for_status()

            # Print the response content
            print(response.json())

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")
    else:
        print("Token is not available. Request not sent.")

if __name__ == "__main__":
    # Replace these with your actual credentials
    username = 'admin'
    password = 'oyindamola'

    # Step 1: Obtain Token
    token = obtain_token(username, password)

    # Step 2: Make Authenticated Request
    make_authenticated_request(token)
