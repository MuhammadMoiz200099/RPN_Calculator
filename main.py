from rpm import RPNCalculator
import sys

def main():
    ## constructurng the calculator object to be used throughout the app
    rpn_calc = RPNCalculator()

    ## takes input from user until "q" is given
    input_line = input("> ")
    while input_line != "q":
        tokens = input_line.split()
        for t in tokens:
            try:
                rpn_calc.process_token(t)
            except ValueError:
                print(f"Operation {t} is not recognized, ignoring {t}", file=sys.stderr)
            except IndexError:
                print(f"Operation {t} is provoked without required operands in stack", file=sys.stderr)
            except ZeroDivisionError:
                print(f"Float division by zero, ignoring it", file=sys.stderr)
        
        ## after processing all tokens, print the last value in stack, if any
        result = rpn_calc.get_current_value()
        if result is not None:
            print(result)
        input_line = input("> ")
        

if __name__ == "__main__":
    ## the entry point of the app
    try:
        main()
    except EOFError:
        ## do nothing on EOF
        pass
    finally:
        print("Thank you for using our service")