#List Comprehension 

#usual way 
nums = [1,2,3,4,5]
squares = []
for num in nums:
    squares.append(num * num)
print(squares)

#by using list comprehension
numb = [1,2,3,4,5]
squares = [number * number for number in numb]
print(squares)

#Filter
even_num = [n for n in numb if n % 2 == 0]
print(even_num)

odd_num = [n for n in numb if n % 2 == 1]
print(odd_num)

#tuple unpacking

user = ("John", 23)
name, age = ("Don", 25)
print(name)
print(age)
print(user)

 