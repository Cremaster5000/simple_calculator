class Calculator():
    def __init__(self):
        self.operand1 = ''
        self.operand2 = ''
        self.operator = ''
        self.last_operation = []

    def equals(self):
        operations = {'+':self.plus, '-':self.minus, '/':self.divide, 'x':self.multiply}
        if self.operator != ''and self.operand2 != '':
            return operations[self.operator]()


    def plus(self):
        result = int(self.operand1,base=10)+int(self.operand2,base=10)
        self.clear()
        print(result)
        return result  

    def minus(self):
        result = int(self.operand1,base=10)-int(self.operand2,base=10)
        self.clear()
        print(result)
        return result     

    def multiply(self):
        result = int(self.operand1,base=10)*int(self.operand2, base=10)
        self.clear()
        print(result)
        return result

    def divide(self):
        result = int(self.operand1,base=10)/int(self.operand2,base=10)
        self.clear()
        print(result)
        return result

    def lastOperation(self):
        return self.last_operation

    def showDigits(self):
        if self.operator == '':
            if self.operand1 == '':
                return 0  
            return int(self.operand1, base=10)
        else:
            if self.operand2 == '':
                return int(self.operand1, base=10)  
            else: 
                return int(self.operand2, base=10)

    def clear(self):
        self.operator = ''
        self.operand1 = ''
        self.operand2 = ''

    def addDigit(self, digit):
        if self.operator == '':
            self.operand1+=str(digit)
            print(self.operand1)
        else:
            self.operand2+=str(digit)
            print(self.operand2)

    def operatorSettled(self, operator):
        self.operator = operator
        print(self.operator)


if __name__ == '__main__':
    pass	