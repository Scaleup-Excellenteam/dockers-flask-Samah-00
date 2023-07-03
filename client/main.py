from flask import Flask, request
import requests

app = Flask(__name__)

#  MAKE SURE TO CHANGE THE URL TO THE NAME OF THE DOCKER CONTAINER IN WHICH THE ROUTER IS RUNNING!!!
router_url = 'http://server:8000'


@app.route('/upload', methods=['POST'])
def upload_file():
    # Read the code from a file
    with open('code.py', 'r') as file:
        code = file.read()

    # Prepare the data to send in the request
    data = {'code': code}

    # Make a POST request to the router's upload endpoint
    response = requests.post(f"{router_url}/upload", data=data)

    return response.text


@app.route('/execute', methods=['GET'])
def execute_code():
    filename = 'code.py'

    # Prepare the query parameter for the request
    params = {'filename': filename}

    # Make a GET request to the router's execute endpoint
    response = requests.get(f"{router_url}/execute", params=params)

    return response.text


def main():
    # Test the upload_file() function
    upload_result = upload_file()
    print("Upload Result:", upload_result)

    # Test the execute_code() function
    execute_result = execute_code()
    print("Execution Result:", execute_result)


if __name__ == '__main__':
    main()
