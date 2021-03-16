# Lab: Iterators and Generators
Problems for in-class lab for the Python OOP Course @SoftUni. Submit your solutions in the SoftUni judge system at [judge](https://judge.softuni.bg/Contests/1944)
## 1. Custom Range - [Solution](https://github.com/borislavstoychev/Soft_Uni/blob/master/soft_uni_OOP/Iterators%20and%20Generators/lab/custom_range_1.py)
Create a class called custom_range that receives start and end upon initialization. Implement the __iter__ and __next__ methods, so the iterator returns the numbers from the start to the end (inclusive).
Note: Submit only the class in the judge system
### *Examples*
|       Test Code       |      Output       |
|-----------------------|-------------------|
|one_to_ten = custom_range(1, 10)<br>for num in one_to_ten:<br>print(num) |  1<br>2<br>3<br>4<br>5<br>7<br>8<br>9<br>10
## 2. Reverse Iter - [Solution](https://github.com/borislavstoychev/Soft_Uni/blob/master/soft_uni_OOP/Iterators%20and%20Generators/lab/reverse_iter_2.py)
Create a class called reverse_iter which should receive an iterable upon initialization. Implement the __iter__ and __next__ methods, so the iterator returns the items of the iterable in reversed order.
Note: Submit only the class in the judge system
### Examples
|       Test Code       |      Output       |
|-----------------------|-------------------|
|reversed_list = reverse_iter([1, 2, 3, 4])<br>for item in reversed_list:<br>       print(item)          |4<br>3<br>2<br>1          |

## 3. Vowels - [Solution](https://github.com/borislavstoychev/Soft_Uni/blob/master/soft_uni_OOP/Iterators%20and%20Generators/lab/vowels_3.py)
Create a class called vowels which should receive a stirng. Implement the __iter__ and __next__ methods, so the iterator returns only the vowels from the string.
Note: Submit only the class in the judge system
### *Examples*
|       Test Code       |      Output       |
|-----------------------|-------------------|
my_string = vowels('Abcedifuty0o')<br>for char in my_string:<br> print(char)| A<br>e<br>i<br>u<br>y<br>o

## 4. Squares - [Solution](https://github.com/borislavstoychev/Soft_Uni/blob/master/soft_uni_OOP/Iterators%20and%20Generators/lab/squares_4.py)
Create a generator function called squares that should receive a number n. It should generate the squares of all numbers from 1 to n (inclusive).
Note: Submit only the function in the judge system
### *Examples*
Test Code| Output
---------| ------
print(list(squares(5)))| [1, 4, 9, 16, 25]

## 5. Generator Range - [Solution](https://github.com/borislavstoychev/Soft_Uni/blob/master/soft_uni_OOP/Iterators%20and%20Generators/lab/generato_range_5.py)
Create a generator function called genrange that receives a start and an end. It should generate all the numbers from the start to the end (inclusive).
Note: Submit only the function in the judge system
### *Examples*
Test Code | Output
----------| ------
print(list(genrange(1, 10)))| [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

## 6. Reverse string - [Solution](https://github.com/borislavstoychev/Soft_Uni/blob/master/soft_uni_OOP/Iterators%20and%20Generators/lab/reverse_string_6.py)
Create a generator function called reverse_text that receives a string and yield all string characters in reversed order.
Note: Submit only the function in the judge system
### *Examples*
Test Code | Output
----------| ------
for char in reverse_text("step"):<br>print(char, end='')| pets

