is_it_palindrome = input().split()
searched_palindrome = input()

founded_palindrome = list(palindrome for palindrome in is_it_palindrome if palindrome == palindrome[::-1])

print(founded_palindrome)
print(f"Found palindrome {founded_palindrome.count(searched_palindrome)} times")

