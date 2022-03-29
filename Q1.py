class Calculator:
    def __init__(self):
        val1 = int(input("Enter first value: "))
        val2 = int(input("Enter second value: "))
        self.adder(val1, val2)
        self.subtractor(val1, val2)
        self.multiplier(val1, val2)
        self.divider(val1, val2)
        self.clear()

    def adder(self, input1, input2):
        newVal = input1 + input2
        print("Adding " + str(input1) + " and " + str(input2) + ": "+ str(newVal))
        return

    def subtractor(self, input1, input2):
        newVal = input1 - input2
        print("Subtracting " + str(input1) + " and " + str(input2) + ": "+ str(newVal))
        return

    def multiplier(self, input1, input2):
        newVal = input1 * input2
        print("Multiplying " + str(input1) + " and " + str(input2) + ": "+ str(newVal))
        return

    def divider(self, input1, input2):
        newVal = input1 / input2
        print("Dividing " + str(input1) + " and " + str(input2) + ": "+ str(newVal))
        return

    def clear(self):
        print("Clearing calculator")
        return 0

calc = Calculator()