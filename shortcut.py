from Programs import Operation

class Greeting(Operation):
    def greet(self):
        print('HI')

summation = Greeting()
summation.greet()
summation.no5()