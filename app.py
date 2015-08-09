import logging
from flask import *
from compilers import java

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)

@app.route("/")
def hello():
    print(request)
    return "Hello Worlds!"

# This handles the code to be executed. It takes a json object with four attributes, language, code, filename, and input
# The language specified which compiler to use on the code, and the filename is what the file is saved as
# Filename doesn't include an extension
@app.route('/execute', methods=['POST'])
def execute():
    data = request.get_json(force=True)
    language = data['language']
    code = data['code']
    filename = data['filename']
    inputs = data['input']

    if language == 'java':
        return java.execute(filename, code, inputs)
    elif language == 'python2.7':
        pass


if __name__ == "__main__":
    app.run(use_debugger=False, debug=True)