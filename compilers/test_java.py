from unittest import TestCase
from compilers import java
import json

__author__ = 'Tom'


class TestJava(TestCase):
    def test_compilation_error(self):
        # Pass in code with a filename / class name difference
        result = java.execute('HellWorld', 'public class HelloWorld {' +
                                           ' public static void main(String[] args) {' +
                                           '     System.out.println("Hello World!");' +
                                           ' }' +
                                           '}', ['Input 1', 'Input 2'])
        result = json.loads(result)
        self.assertEquals(result['result'], 'Compilation Error', "There was a compilation error")
        self.assertTrue(len(result['message']) > 0, "The error message was returned")

    def test_runtime_error(self):
        # Pass in code with a divide by zero error
        result = java.execute('HelloWorld', 'public class HelloWorld {' +
                                            ' public static void main(String[] args) {' +
                                            '     System.out.println(5 / 0);' +
                                            ' }' +
                                            '}', ['Input 1', 'Input 2'])
        result = json.loads(result)
        self.assertEquals(result['result'], 'Runtime Error')
        self.assertTrue(len(result['output']) > 0)
        self.assertTrue(len(result['message']) > 0, "The error message was returned")

    def test_no_input_return_stdout(self):
        # Pass in code with a divide by zero error
        result = java.execute('HelloWorld', 'public class HelloWorld {' +
                                            ' public static void main(String[] args) {' +
                                            '     System.out.println("Hello world!");' +
                                            ' }' +
                                            '}', ['Input 1', 'Input 2'])
        result = json.loads(result)
        self.assertEquals(result['result'], 'Ran Successfully')
        self.assertTrue(len(result['output']) > 0)

        # Two inputs, identical output
        self.assertEquals('Hello world!', result['output'][0])
        self.assertEquals('Hello world!', result['output'][1])
        self.assertTrue(len(result['message']) == 0)

    def test_stdin_echo(self):
        # Pass in code with a divide by zero error
        result = java.execute('HelloWorld', 'import java.util.*;' +
                                            'public class HelloWorld {' +
                                            ' public static void main(String[] args) {' +
                                            '     System.out.println(new Scanner(System.in).nextLine());' +
                                            ' }' +
                                            '}', ['Input 1', 'Input 2'])
        result = json.loads(result)
        self.assertEquals(result['result'], 'Ran Successfully')
        self.assertTrue(len(result['output']) > 0)

        # Just output the input
        self.assertEquals('Input 1', result['output'][0])
        self.assertEquals('Input 2', result['output'][1])
        self.assertTrue(len(result['message']) == 0)

