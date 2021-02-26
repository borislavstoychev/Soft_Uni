class Integer:

    def __init__(self, value: int):
        self.value = value

    @staticmethod
    def from_float(value):
        if not isinstance(value, float):
            return "value is not a float"
        return Integer(int(value))

    @staticmethod
    def from_roman(value):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(value)):
            if i > 0 and rom_val[value[i]] > rom_val[value[i - 1]]:
                int_val += rom_val[value[i]] - 2 * rom_val[value[i - 1]]
            else:
                int_val += rom_val[value[i]]
        return Integer(int_val)

    @staticmethod
    def from_string(value):
        if not isinstance(value, str):
            return "wrong type"
        return Integer(int(value))

    def add(self, integer):
        if not isinstance(integer, Integer):
            return "number should be an Integer instance"
        return self.value + integer.value

    def __str__(self):
        return f"{self.value}"


first_num = Integer(10)
second_num = Integer.from_roman("IV")
x = Integer.from_float(3.5)
print(x)
y = Integer.from_string("2")
print(y)
print(first_num.add(second_num))