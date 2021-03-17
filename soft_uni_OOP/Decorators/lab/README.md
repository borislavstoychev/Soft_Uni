# Lab: Decorators
Problems for in-class lab for the Python OOP Course @SoftUni. Submit your solutions in the SoftUni judge system at [judge](https://judge.softuni.bg/Contests/1946)
##    1. Number Increment - [Solution](https://github.com/borislavstoychev/Soft_Uni/blob/master/soft_uni_OOP/Decorators/lab/number_increment_1.py)
*Having the following code:*
```
def number_increment(numbers):

    def increase():

        # TODO ...

    return increase()
```
*Complete the code so it works as expected*
### *Examples*
Test Code | Output
----------| ------
print(number_increment([1, 2, 3])) | [2, 3, 4]
##    2. Vowel Filter - [Solution](https://github.com/borislavstoychev/Soft_Uni/blob/master/soft_uni_OOP/Decorators/lab/vowel_filter_2.py)
*Having the following code:*
```
def vowel_filter(function):

    def wrapper(*args, **kwargs):
        #TODO ...
        
    return wrapper
```
*Complete the code so it works as expected*
### *Examples*
Test Code | Output
----------| ------
@vowel_filter <br>def get_letters():<br> return ["a", "b", "c", "d", "e"]<br>print(get_letters()) | ["a", "e"]
##    3. Even Numbers - [Solution](https://github.com/borislavstoychev/Soft_Uni/blob/master/soft_uni_OOP/Decorators/lab/even_numbers_3.py)
*Having the following code:*
```
ef even_numbers(function):
    def wrapper(numbers):
        #TODO...

    return wrapper
```
*Complete the code so it works as expected*

### *Examples*
Test Code | Output
----------| ------
@even_numbers <br>def get_numbers(numbers):<br> return numbers<br>print(get_numbers([1, 2, 3, 4, 5]))| [2, 4]
##    4. Multiply - [Solution](https://github.com/borislavstoychev/Soft_Uni/blob/master/soft_uni_OOP/Decorators/lab/multiply_4.py)
*Having the following code:*
```
def multiply(times):

    def decorator(func):
    
        #TODO...
        
    return decorator
```
*Complete the code so it works as expected*
### *Examples*
Test Code | Output
----------| -----
@multiply(3)<br>def add_ten(number):<br>return number + 10<br>print(add_ten(3)) | 39<br>First we add 3 to 10 = 13 and then we multiply the result by 3: 13 * 3 = 39
@multiply(5)<br>def add_ten(number):<br>return number + 10 <br>print(add_ten(6)) | 80<br>(6 + 10) * 5 = 80
