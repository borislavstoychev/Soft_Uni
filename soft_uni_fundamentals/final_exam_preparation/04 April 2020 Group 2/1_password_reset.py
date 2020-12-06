class Password:
    def __init__(self):
        self.raw_password = ""

    def take_odd(self, l):
        for i in range(1, len(l), 2):
            self.raw_password += l[i]
        print(self.raw_password)
        return self.raw_password

    def cut(self, l, i, length):
        self.raw_password = l[:i] + l[i + length:]
        print(self.raw_password)
        return self.raw_password

    def substitutes(self, l, substring, substitute):
        self.raw_password = l.replace(substring, substitute)
        if self.raw_password == l:
            print("Nothing to replace!")
        else:
            print(self.raw_password)
        return self.raw_password


line = input()
p = Password()
while True:
    commands = input()
    if commands == "Done":
        print(f"Your password is: {line}")
        exit()
    elif commands == "TakeOdd":
        line = p.take_odd(line)
    else:
        command, token1, token2 = commands.split()[::]
        if command == "Cut":
            index = int(token1)
            length = int(token2)
            line = p.cut(line, index, length)
        elif command == "Substitute":
            substr, subst = token1, token2
            line = p.substitutes(line, substr, subst)
