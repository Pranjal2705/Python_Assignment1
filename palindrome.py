# Print palindrome string taking input as string

string=input(("Enter a string:"))
if(string==string[::-1]):
      print("The given string is a palindrome")
else:
      print("The given string is not a palindrome")