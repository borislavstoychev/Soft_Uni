# сума = депозирана сума + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)
deposit = float(input())
term_of_the_depost = int(input())
yearly_precent = float(input())
result = deposit + term_of_the_depost * ((deposit * yearly_precent / 100) / 12)
print(result)