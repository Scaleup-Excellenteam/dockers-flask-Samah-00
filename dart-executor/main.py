from flask import Flask, request
import subprocess

PORT = 8003

app = Flask(__name__)


@app.route('/execute', methods=['POST'])
def execute_code():
    # Get the code from the request
    code = request.form.get('code')

    # Create a Dart source file with the code
    with open('main.dart', 'w') as file:
        file.write(code)

    # Execute the Dart code using the Dart SDK
    execution_process = subprocess.run(['dart', 'main.dart'], capture_output=True)

    # Return the output of the Dart code execution
    return execution_process.stdout.decode(), 200


if __name__ == '__main__':
    app.run(port=PORT)
