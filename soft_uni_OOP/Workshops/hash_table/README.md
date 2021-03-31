# Workshop HashTable
In computing, a hash table (hash map) is a data structure that implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index, also called a hash code, into an array of buckets or slots, from which the desired value can be found. During lookup, the key is hashed and the resulting hash indicates where the corresponding value is stored.
##    1. Overview - [Solution](https://github.com/borislavstoychev/Soft_Uni/blob/master/soft_uni_OOP/Workshops/hash_table/hash_table.py)
### Create a HashTable class that should have the needed functionality for a hash table, such as:
    • hash(key: str) - a function that should figure out where to store the key-value pair
    • add(key: str, value: any) - adds a new key-value pair usign the hash function
    • get(key: str) - returns the value corresponding to the given key
    • additional "magic" methods, that will make the code in the example work correctrly
The HashTable should have an attribute called array of type: list, where all the values will be stored. Upon initialization the default length of the array should be 4. After each addition of an element if the HashTable gets too populated, double the length of the array and re-add the existing data.
You are not allowed to inherit any classes. Feel free to implement your own functionality ([and unit tests-link](https://github.com/borislavstoychev/Soft_Uni/blob/master/soft_uni_OOP/Workshops/hash_table/test_hash_table.py)) or to write the methods by yourself.
##    2. Examples
Test Code | Result
----------| ------
table = HashTable()<br>table["name"] = "Peter"<br>table["age"] = 25 <br>print(table)<br>print(table.get("name"))<br>print(table["age"])<br>print(len(table)) | <hash_table.HashTable object at 0x00000185F4F08580><br>Peter<br>25<br>4
