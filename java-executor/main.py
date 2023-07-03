from flask import Flask, request
import subprocess

PORT = 8001

app = Flask(__name__)


@app.route('/execute', methods=['POST'])
def execute_code():
    # Get the code from the request
    code = request.form.get('code')

    # Create a Java source file with the code
    with open('Main.java', 'w') as file:
        file.write(code)

    # Compile the Java source file
    compile_process = subprocess.run(['javac', 'Main.java'], capture_output=True)

    if compile_process.returncode != 0:
        # Return the compilation error message
        return compile_process.stderr.decode(), 400

    # Execute the compiled Java code
    execution_process = subprocess.run(['java', 'Main'], capture_output=True)

    # Return the output of the Java code execution
    return execution_process.stdout.decode(), 200


if __name__ == '__main__':
    app.run(port=PORT)
