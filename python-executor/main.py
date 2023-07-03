from flask import Flask, request
import subprocess

PORT = 8002

app = Flask(__name__)


@app.route('/execute', methods=['POST'])
def execute_code():
    # Get the code from the request
    code = request.form.get('code')

    # Execute the Python code
    execution_process = subprocess.run(['python3', '-c', code], capture_output=True)

    # Return the output of the Python code execution
    return execution_process.stdout.decode(), 200


if __name__ == '__main__':
    app.run(port=PORT)
