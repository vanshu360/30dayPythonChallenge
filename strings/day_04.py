# letter = "v"
# print(letter)
# print(len(letter))
# greeting = "Hello, World!"
# print(greeting)
# print(len(greeting))
# print("hi, I am Vanshu")
# print("hi, I'm Vanshu")

# print("I hope everyone is enjoying the Python Challenge.\nDo you think you are enjoying it?")
# print("Days\tTopics\tExercises")
# print('Day 1\t3\t5')
# print('Day 2\t6\t20')

first_name = "Vanshika"
last_name = "Sahore"
language = "Python"
formated_string ='I\'m {} {}.I am learning {}'.format(first_name, last_name, language)
print(formated_string)

a = 11
b = 4
print('{} + {} = {}'.format(a,b,a+b))
print('{} - {} = {}'.format(a,b,a-b))
print('{} * {} = {}'.format(a,b,a*b))
print('{} // {} = {}'.format(a,b,a//b))
print('{} / {} = {}'.format(a,b,a/b))
print('{} ** {} = {}'.format(a,b,a**b))
print('{} % {} = {}'.format(a,b,a%b))

print(f'{a} + {b} = {a+b}') # no need of using .format 
print('{a} + {b} = {a+b}') # print the string as text format 


sentence = ['Thirty' , 'Days' , 'Of' , 'Python']
print(' '.join(sentence)) # using .join() method to convert list into string text

w1='Coding'
w2='For'
w3='All'
words = (f'{w1} {w2} {w3}')
print(words) # use f-string 

company = "Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize()) # Coding for all 
print(company.title()) # Coding For All
print(company.swapcase()) #cODING fOR aLL uppercase -> <- lowercase
pto = company[0:6]
print(pto)
new_word = company[:6]
print(new_word)
print(company.find('Coding')) # return 0 - coding index 
print(company.index('Coding')) # Coding index - 0
print('Coding' in 'Coding For All') # true
print(company.replace('Coding For All','Python'))

word = 'Python for Everyone'
#print(word.replace(word,'Python to All'))
left_part = word[0:19]
print(f'{left_part} python to All')

words = 'Coding for All'
print(words.split(' '))
list = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(list.split())
print(list.split(' '))
print(list.split(', '))

print(words[0])
print(words[len(words)-1])
print(words[10])

title ='Python For Everyone'
new = title.split()
print(f'{new[0][0]}{new[1][0]}{new[2][0]}') #acronym
part1 = new[0][0:2].upper()
part2 = "4"
part3 = new[2][0].upper()
print(f"{part1}{part2}{part3}")

name = 'Coding For All People'
words = name.split()
print(f'{words[0][0]}{words[1][0]}{words[2][0]}') #CFA
print(name.index('C'))
print(name.index('F'))
print(name.rfind('l'))

sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))
print(sentence.find('because'))
print(sentence.rindex('because'))
s = sentence.split('because because because')
result = "".join(s)
print(result)

text = "Coding for All"
result = text.startswith('Coding')
print(result)

r = text.endswith('Coding')
print(r)
print(text.strip())
a = '30DaysOfPython'
b = 'thirty_days_of_python'
print(a.isidentifier())
print(b.isidentifier())

list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('#'.join(list))

print('I am enjoying this challenge \nI just wonder what is next')

print('Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')

radius = 10
area = int(3.14*radius**2)
print(f'The area of circle with radius{radius} is {area} meters squares')

a = 8
b = 6
print(f'{a}+{b}={a+b}')
print('{}+{}={}'.format(a,b,a+b))
print(f'{a}-{b}={a-b}')
print(f'{a}*{b}={a*b}')
print(f'{a}/{b}={a/b}')
print(f'{a}%{b}={a%b}')
print(f'{a}//{b}={a//b}')
print(f'{a}**{b}={a**b}')