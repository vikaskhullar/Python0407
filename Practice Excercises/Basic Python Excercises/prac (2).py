"""Define a function is_palindrome() that recognizes 
palindromes (i.e. words that look the same written backwards). 
For example, is_palindrome("radar") should return True."""

def is_palindrome(st):
  return (st == st[::-1])

#test
print (is_palindrome("radae"))
print (is_palindrome("IzitizI"))
print (is_palindrome("Definitely not a palindrome :)"))
print (is_palindrome("121"))

