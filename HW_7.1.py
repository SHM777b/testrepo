'''Write a program that prompts for a file name, then opens that file and reads through the file,
and print the contents of the file in upper case. Use the file words.txt to produce the output below.'''

file_name = input('Please enter the file name: ')
file = open(file_name, 'r')

for line in file:
    line = line.rstrip()
    line = line.upper()
    print (line)
