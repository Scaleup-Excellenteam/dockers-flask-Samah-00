from flask import Flask
import os

app = Flask(__name__)


# Directory to store code files temporarily
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CODE_LANGUAGE = 1


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
