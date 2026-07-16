# TASK-1
single_quotes = 'Lakshay'
double_quotes = "Agarwal"
triple_quotes = """Piprali
Sikar"""
num_as_string = "123"
spec_as_string = "@^&"
empty_string = ""
print(triple_quotes)

# Escape Characters
print("Hello\nLakshay") #New Line
print("Hello\tLakshay") #Tab Space

print("Hello\\Lakshay") #Backslash
print("Hello\"Lakshay\"") #Backslash

win_path = "C:\new\test.txt"
print(win_path) #This will not work as expected because \n and \t are escape characters

# Raw String r
win_path = r"C:\new\test.txt"
print(win_path) #r tells python to treat the string as raw string and ignore escape characters


print(type(single_quotes))
print(type('123'))
