import javalang  # assuming you're using javalang for parsing Java code

class JavaCodeParser:
    def __init__(self):
        # This constructor might not be needed for basic use, but could be expanded for configuration
        self.java_code = None
        self.ast = None

    def parse_code(self, java_code: str):
        """
        Method to parse Java code and validate its syntax.
        If the code is valid, it generates an AST (Abstract Syntax Tree).
        If invalid, it raises a SyntaxError.

        Parameters:
            java_code (str): The Java source code as a string.

        Returns:
            AST (javalang.tree): Abstract Syntax Tree of the parsed code.
        
        Raises:
            SyntaxError: If the code has syntax errors.
        """
        self.java_code = java_code  # Store the provided Java code
        
        try:
            # Parse the Java code using javalang and generate the AST
            self.ast = javalang.parse.parse(self.java_code)
            return self.ast  # Return the AST if parsing is successful
        except javalang.parser.JavaSyntaxError as e:
            # Handle syntax errors and raise a descriptive error
            raise SyntaxError(f"Invalid Java code: {e}") from e

    def get_ast(self):
        """ Returns the generated AST if parsing was successful. """
        if self.ast:
            return self.ast
        else:
            raise ValueError("No AST generated. Please parse the code first.")
