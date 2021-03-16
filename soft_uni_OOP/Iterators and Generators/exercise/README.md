# Exercise: Iterators and Generators
Problems for exercise and homework for the Python OOP Course @SoftUni. Submit your solutions in the SoftUni judge system at [judge](https://judge.softuni.bg/Contests/1945)
##    1. Take Skip - [Solution](https://github.com/borislavstoychev/Soft_Uni/blob/master/soft_uni_OOP/Iterators%20and%20Generators/exercise/take_skip_1.py)
Create a class called take_skip. Upon initialization it should receive a step (number) and a count (number). Implement the __iter__ and __next__ functions. The iterator should return the count numbers (starting from 0) with the given step. For more clarification, see the examples:
###### *Note: Submit only the class in the judge system*
### *Examples*

| Test Code | Output  |
|---------- | ------  |
numbers = take_skip(2, 6)<br>for number in numbers:<br> print(number) | 0<br>2<br>4<br>6<br>8<br>10
numbers = take_skip(10, 5)<br>for number in numbers:<br> print(number)| 0<br>10<br>20<br>30<br>40

##    2. Dictionary Iterator - [Solution](https://github.com/borislavstoychev/Soft_Uni/blob/master/soft_uni_OOP/Iterators%20and%20Generators/exercise/dictionary_iterator_2.py)
Create a class called dictionary_iter. Upon initialization it should receive a dictionary object. Implement the iterator, so it returns each key-value pair of the dictionary as a tuple of two elements (the key and the value).
###### *Note: Submit only the class in the judge system*
### *Examples*
Test Code | Output
----------| ------
result = dictionary_iter({1: "1", 2: "2"})<br>for x in result:<br> print(x) | (1, '1')<br>(2, '2')
##    3. Countdown Iterator - [Solution](https://github.com/borislavstoychev/Soft_Uni/blob/master/soft_uni_OOP/Iterators%20and%20Generators/exercise/countdown_iterator_3.py)
Create a class called countdown_iterator. Upon initialization it should receive a count. Implement the iterator, so it returns each number of the countdown (from count to 0 inclusive).
###### *Note: Submit only the class in the judge system*

### *Examples*
Test Code | Output
----------| ------
iterator = countdown_iterator(10)<br>for item in iterator:<br> print(item, end=" ") | 10 9 8 7 6 5 4 3 2 1 0

##    4. Sequence Repeat - [Solution](https://github.com/borislavstoychev/Soft_Uni/blob/master/soft_uni_OOP/Iterators%20and%20Generators/exercise/sequence-repeat_4.py)
Create a class called sequence_repeat which should receive a sequence and a number upon initialization. Implement an iterator to return the given elements the defined number of times. If the number is greater than the number of elements, then the sequence repeats as necessary.
### *Examples*
Test Code | Output
----------| ------
result = sequence_repeat('abc', 5)<br>for item in result: <br>print(item, end ='') | abcab
##    5. Take Halves - [Solution](https://github.com/borislavstoychev/Soft_Uni/blob/master/soft_uni_OOP/Iterators%20and%20Generators/exercise/take_halves_5.py)
You are given a skeleton with the following code:
```
def solution():

    def integers():
        ...

    def halves():
        for i in integers():
            ...

    def take():
        ...


    return (take, halves, integers)
```
##### Implement the three generator functions:
    • integers() - generates an infinite amount of integers (starting from 1)
    • halves() - generates the halves of those integers (each integer / 2)
    • take(n, seq) - takes the first n halves of those integers
###### *Note: Complete the functionality in the skeleton and submit it in the judge system*
### *Examples*
Test Code | Output
----------| ------
take = solution()[0]<br>halves = solution()[1]<br>print(take(5, halves())) | [0.5, 1.0, 1.5, 2.0, 2.5]
##    6. Fibonacci Generator - [Solution](https://github.com/borislavstoychev/Soft_Uni/blob/master/soft_uni_OOP/Iterators%20and%20Generators/exercise/fibonacci_generator_6.py)
Create a generator function called fibonacci() that generates the Fibonacci numbers infinitely (starting from 0). Each Fibonacci number is created by the sum of the current number with the previous.
###### *Note: Submit only the function in the judge system*
### *Examples*
Test Code | Output
----------| ------
generator = fibonacci()<br>for i in range(5):<br> print(next(generator)) | 0<br>1<br>1<br>2<br>3
##    7. Reader - [Solution](https://github.com/borislavstoychev/Soft_Uni/blob/master/soft_uni_OOP/Iterators%20and%20Generators/exercise/reader_7.py)
Create a generator function called read_next() which should receive different number of arguments (all iterable). On each iteration it should return the next element from the current iterable, or the first element from the subsequent iterable.
###### *Note: Submit only the function in the judge system*
### *Examples*
Test Code | Output
----------| ------
for item in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}):<br> print(item, end='') | string2dict
##    8. Prime Numbers - [Solution](https://github.com/borislavstoychev/Soft_Uni/blob/master/soft_uni_OOP/Iterators%20and%20Generators/exercise/prime_numbers_8.py)
Create a generator function called get_primes() which should receive a list of integer numbers and return a list containing only the prime numbers from the initial list. You can learn more about prime numbers from here:
###### *Note: Submit only the function in the judge system*
### *Examples*
Test Code | Output
----------| ------
print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0]))) | [2, 3, 5]
##    9. Possible permutations - [Solution](https://github.com/borislavstoychev/Soft_Uni/blob/master/soft_uni_OOP/Iterators%20and%20Generators/exercise/possible_permutations_9.py)
Create a generator function called possible_permutations() which should receive a list and return lists with all possible permutations between it's elements.
###### *Note: Submit only the function in the judge system*
### *Examples*
Test Code | Output
----------| ------
[print(n) for n in possible_permutations([1, 2, 3])] | [1, 2, 3]<br>[1, 3, 2]<br>[2, 1, 3]<br>[2, 3, 1]<br>[3, 1, 2]<br>[3, 2, 1]
