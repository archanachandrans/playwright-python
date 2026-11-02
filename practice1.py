#Fist largest number

nums = [12, 5, 8, 20, 15]
largest = nums[0]
for num in nums:
    if num > largest:
        largest = num
print("Largest: ", largest)


#Character frequency
word = ['programming']
letter_count = {}
for letter in word:
    letter_count



#Student marks analysis 
students = {'john': 66, 'Phil': 32, 'Smith': 45}
passed ={ name: score for name, score in students.items() if score>= 40}
failed ={ name: score for name, score in students.items() if score< 40}
for name, score in passed.items():
    print({name} , {score} , "PASS")
for name, score in failed.items():
    print({name} , {score} , "FAILED")

#Function with return value
def calculate(price, quantity):
    return price * quantity
total= calculate(460, 3)
print("Total amount:", total)
if total > 2000:
    discount = total - (total*10)/100
    print("Total after discount: ",discount)

#Lambda function
numbers = [12, 5, 18, 7, 24, 9, 30]
for num in numbers:
    multiply = lambda x : x * 3
    print(multiply(num))

#factorial
def fact(n):
    #Base case
    if n == 0 or n == 1:
        return 1
    #Recursive case
    return n * fact(n-1)
print(fact(5))

#File handling text file
file = open("notes.txt", "w")
file.write("This is a sample document\n")
file.write("For python playwright\n")
file.write("Writing to a new document\n")
file.write("Then reading it\n")
file = open("notes.txt", "r")
content = file.read()
print(content)
file = open("notes.txt", "a")
content = file.write("Finally append a new line\n")
file = open("notes.txt", "r")
content = file.read()
print(content)
file.close()

#writing data into csv file
import csv 
with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["id", "name", "salary"])
    writer.writerow(["001", "Jacob", "230000"])
    writer.writerow(["002", "Mickel", "400000"])
    writer.writerow(["003", "Joe", "543000"])
    writer.writerow(["004", "Daniel", "904000"])
print("csv file created")

#Student class
class Students:
    def __init__(self, name, rollnum, marks):
        self.name = name
        self.rollnum = rollnum
        self.marks = marks
    def display_details(self):
        print(self.name, self.rollnum, self.marks)
    def check_result(self):
        if self.marks > 40:
            print("PASS")
        else:
            print("FAIL")
student1 = Students("Antony", 1, 54)
student2 = Students("Benny", 2, 35)
student3 = Students("Henry", 3, 78)
student1.display_details()
student2.display_details()
student3.display_details()
student1.check_result()
student2.check_result()
student3.check_result()