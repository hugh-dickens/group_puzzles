class EulersMachine:
    def __init__(self, input_number):
        self.input_number = input_number
        self.output_number = 0

    def calculate_output_number(self):
        self.output_number = self.input_number - 1

    def print_output_number(self):
        print("Output number for this case is: {} ".format(self.output_number))

if __name__ == '__main__':

    print("Welcome to Eulers Machine calculator. Input a number: ")
    my_eulers_machine = EulersMachine(5)

    