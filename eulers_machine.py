class EulersMachine:
    def __init__(self, input_number):
        self.input_number = input_number
        self.output_number = 1

    def subtracting_five(self):
        for i in range(self.input_number):
            if ((i%5 == 0) and (i!= 0) and (self.input_number - i != 1)):
                self.iterate_output_number()

    def subtracting_four(self):
        for i in range(self.input_number):
            if ((i%4 == 0) and (i!= 0) and (self.input_number - i != 1)):
                #print("Entered subtracting four")
                self.iterate_output_number()

    def subtracting_three(self):
        for i in range(self.input_number):
            if ((i%3 == 0) and (i!= 0) and (self.input_number - i != 1)):
                # print(i)
                #print("Entered subtracting three")
                self.iterate_output_number()
                if (self.input_number - i > 4):
                    #print("Entered subtracting three")
                    self.iterate_output_number()
    
    def subtracting_two(self):
        for i in range(self.input_number):
            if ((i%2 == 0) and (i!= 0) and (self.input_number - i != 1)):
                # print(i)
                # print("Entered subtracting two")
                self.iterate_output_number()
                if (self.input_number - i > 3):
                    # print("Entered subtracting two")
                    self.iterate_output_number()

    def subtracting_one(self):
        for i in range(self.input_number - 1):
            self.iterate_output_number()

    def iterate_output_number(self):
        self.output_number += 1

    def print_output_number(self):
        print("Input->Output number for this case is: {} -> {} ".format(self.input_number, self.output_number))

    def eulers_main_function(self):
        self.subtracting_one()
        self.subtracting_two()
        self.subtracting_three()
        self.subtracting_four()
        self.subtracting_five()
        self.print_output_number()

if __name__ == '__main__':

    print("Welcome to Eulers Machine calculator!")
    # range_test = 10
    # for i in range(range_test):
    my_eulers_machine = EulersMachine(7)
    my_eulers_machine.eulers_main_function()


    