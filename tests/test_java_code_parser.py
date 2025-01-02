import sys
import os
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../code_parser')))

from java_code_parser import JavaCodeParser  

class TestJavaCodeParser(unittest.TestCase):

    def setUp(self):
        """Set up the parser before each test case."""
        self.parser = JavaCodeParser()

    def test_valid_code(self):
        """Test with valid Java code."""
        java_code = """
        public class HelloWorld {
            public static void main(String[] args) {
                System.out.println("Hello, World!");
            }
        }
        """
        try:
            ast = self.parser.parse_code(java_code)
            self.assertIsNotNone(ast, "AST should be generated for valid code.")
        except SyntaxError as e:
            self.fail(f"Unexpected error: {e}")

    def test_invalid_code(self):
        """Test with invalid Java code."""
        java_code = """
        public class HelloWorld {
            public static void main(String[] args) {
                System.out.println("Hello, World!"
            }
        }
        """
        with self.assertRaises(SyntaxError):
            self.parser.parse_code(java_code)

    def test_empty_code(self):
        """Test with an empty Java code string."""
        java_code = ""
        with self.assertRaises(SyntaxError):
            self.parser.parse_code(java_code)

    def test_complex_code(self):
        """Test with more complex Java code."""
        java_code = """
        public class ComplexCode {
            public void methodOne() {
                // some code here
            }
            public void methodTwo() {
                // some other code here
            }
        }
        """
        try:
            ast = self.parser.parse_code(java_code)
            self.assertIsNotNone(ast, "AST should be generated for complex code.")
        except SyntaxError as e:
            self.fail(f"Unexpected error: {e}")

    def test_special_characters(self):
        """Test with special characters in the Java code."""
        java_code = """
        public class SpecialCharacters {
            public static void main(String[] args) {
                System.out.println("Hello, World! €");
            }
        }
        """
        try:
            ast = self.parser.parse_code(java_code)
            self.assertIsNotNone(ast, "AST should be generated even with special characters.")
        except SyntaxError as e:
            self.fail(f"Unexpected error: {e}")

if __name__ == '__main__':
    unittest.main()
