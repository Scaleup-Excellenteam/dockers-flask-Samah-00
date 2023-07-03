from flask import request
import requests

# from app import *
from flask import Flask
import os

app = Flask(__name__)


# Directory to store code files temporarily
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CODE_LANGUAGE = 1
PORT = 8000


outputs = {
    'error-no-code': 'No code file found',
    'msg-upload-successful': 'Code file uploaded successfully',
    'error-no-filename': 'No filename provided',
    'error-file-not-found': 'Code file not found',
    'msg-code-execute': 'Code execution request received',
    'error-unsupported-language': 'Unsupported language',
    'error-executor-connection-failure': 'Failed to connect to the language executor',
    'error-executor-failure': 'Failed to execute the code',
    'error-executor-not-available': 'Language executor is not available',
}

request_values = {
    'bad-request': 400,
    'ok': 200,
    'not-found': 404,
    'internal-server-error': 500
}


def get_language_from_extension(extension):
    mapping = {
        '.java': 'java',
        '.py': 'python',
        '.dart': 'dart'
    }
    return mapping.get(extension)


#  MAKE SURE TO CHANGE THE URLs TO THE NAMEs OF THE DOCKER CONTAINERS IN WHICH THE EXECUTORS ARE RUNNING!!!
def get_executor_url(language):
    mapping = {
        'java': 'http://java-executor:8001',
        'python': 'http://python-executor:8002',
        'dart': 'http://dart-executor:8003'
    }
    return mapping.get(language)


@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if the 'code' file is present in the request
    if 'code' not in request.files:
        return outputs['error-no-code'], request_values['bad-request']

    code_file = request.files['code']

    # Save the code file to the uploads directory
    code_file.save(os.path.join(app.config['UPLOAD_FOLDER'], code_file.filename))

    return outputs['msg-upload-successful'], request_values['ok']


@app.route('/execute', methods=['GET'])
def execute_code():
    # Get the filename from the query parameters
    filename = request.args.get('filename')

    # Check if the filename is provided
    if not filename:
        return outputs['error-no-filename'], request_values['bad-request']

    # Read the code file from the uploads directory
    code_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    # Check if the code file exists
    if not os.path.isfile(code_path):
        return outputs['error-file-not-found'], request_values['not-found']

    # Forward the code file to the appropriate language executor
    result, status = forward_code_to_executor(code_path)

    return result, status


def forward_code_to_executor(code_path):
    # Determine the language based on the file extension
    extension = os.path.splitext(code_path)[CODE_LANGUAGE]
    language = get_language_from_extension(extension)

    if language is None:
        return outputs['error-unsupported-language'], request_values['bad-request']

    # Prepare the data to send in the POST request
    with open(code_path, 'r') as file:
        code = file.read()

    data = {'code': code}

    # Forward the code file to the appropriate language executor
    executor_url = get_executor_url(language)
    if executor_url is None:
        return outputs['error-executor-not-available'], request_values['internal-server-error']

    try:
        response = requests.post(executor_url + '/execute', data=data)
        if response.status_code == request_values['ok']:
            return response.text, request_values['ok']
        else:
            return outputs['error-executor-failure'], request_values['internal-server-error']
    except requests.exceptions.RequestException:
        return outputs['error-executor-connection-failure'], request_values['internal-server-error']


if __name__ == '__main__':
    app.run(port=PORT)
