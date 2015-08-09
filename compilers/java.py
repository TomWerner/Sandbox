from subprocess import Popen, PIPE
import os
import json

def execute(filename, code, inputs):
    """
    :param filename: The name of the file to compile and run
    :param code: The contents of the file
    :param inputs: The list of STDIN inputs to test this program on
    :return: JSON object with the result, error status, message, and outputs
    """
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    os.chdir("../code")
    with open(filename + '.java', mode='w+') as writer:
        writer.write(code)

    p = Popen(['javac', filename + '.java'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()
    os.remove(filename + '.java')

    if len(err) > 0:
        return json.dumps({'result': 'Compilation Error', 'error': True, 'message': err, 'output': []})

    outputs = []

    for input_ in inputs:
        p = Popen(['java', filename], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate(input_)
        outputs.append(output.strip())
        if len(err) > 0:
            os.remove(filename + '.class')
            return json.dumps({'result': 'Runtime Error', 'error': True, 'message': err, 'output': outputs})

    os.remove(filename + '.class')
    return json.dumps({'result': 'Ran Successfully', 'error': False, 'message': '', 'output': outputs})