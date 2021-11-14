class RPNCalculator:
    # not using a single string "+-*/" to avoid matching strings like "*/" etc
    all_ops = ['-', '+', '*', '/']

    def __init__(self):
        ## initializing the class
        self.stack = []

    def process_token(self, t):
        ## performs necessary steps on a given token if operator, else pushes it to the stack
        if t.isdigit():
            self.stack.append(int(t))
        else:
            if t not in RPNCalculator.all_ops:
                raise ValueError("Unknown operator provided")
            if len(self.stack) < 2:
                raise IndexError("Not enough operands in stack")
            b = self.stack.pop()
            a = self.stack.pop()
            if t == "/" and b == 0:
                self.stack.extend([a, b])
                raise ZeroDivisionError("Float division by zero")
            res = self.__perform_calculation(a, b, t)
            self.stack.append(res)

    def get_current_value(self):
        ## Returns the last value in stack, none if the stack is empty
        if self.stack:
            return self.stack[-1]

    def __perform_calculation(self, a, b, op):
        ## private method to perform the current calculation
        ## Note: Not using eval here because of the security concerns
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        else:
            return a / b
        

