# find() : Find the first occurrence of a substring in a string, if substrig is not found then gives -1.
# index() : Find the first occurence of substring, if not found then gives ValueError.
# Find not crash the program by error.

# count() : Count no of substring in a string.
# replace() : Replace a substring with another substring in a string.
# replace only give replaced string as value it actually not change the variable value of that actual string.

# startswith() : If a string starts-with with mentioned substring then give True else False.
# startswith() : If a string ends-with with mentioned substring then give True else False.

# split() : Split the data and give list of data as output.Default by space but we can mention any character to split the data.
# join() : Join the list of data and give string as output. Default by space but we can mention any character to join the data.



# -----------------------------------------
# ---------------TASK-1--------------------
# -----------------------------------------
text = "Python Programming"
print('Position of \"Programming\" : ', text.find("Programming"))
print('Position of \"Java\" : ', text.find("Java"))
print('Count of \"m\" : ', text.count("m"))
print('Replace "Python" with "Java" : ', text.replace("Python", "Java"))

# -----------------------------------------
# ---------------TASK-2--------------------
# -----------------------------------------
email = "lakshayagarwal@gmail.com"
if(email.startswith("lakshay")):
    print("Yes email is starts with lakshay")
else:
    print("No email is not starts with lakshay")
    
# -----------------------------------------
# ---------------TASK-3--------------------
# -----------------------------------------
words = ["Germany", "AI", "Engineer"]
print("Join words with space : ", " ".join(words))
print("Join words with space : ", "-".join(words))
print("Join words with space : ", "->".join(words))



# -----------------------------------------
# ------------MINI CHALLENGE---------------
# -----------------------------------------
challenege_string = "   Python is amazing. Python is powerful.   "
cleaned_string = challenege_string.strip()
print("Removed extra space : ", cleaned_string)
print("Count of Python in given string : ", cleaned_string.count('Python'))
print("Replaced Python with AI", cleaned_string.replace('Python','AI'))
print("Is string sentence starts with Python : ", cleaned_string.startswith('Python'))
two_words_string = cleaned_string.split('. ')
print("String in two words : ", two_words_string)
print("Joined String of two words : ", ' | '.join(two_words_string))


print('9123 '.isdigit())