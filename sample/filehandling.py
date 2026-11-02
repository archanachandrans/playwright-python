#syntax
#file = open("filename.txt", "mode")
#Reading a file
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()

#read line by line
file = open("data.txt", "r")
print(file.readline())
file.close()

#read line by line
# file = open("data.txt", "r")
# lines = file.readlines()
# print(lines[1])
# file.close()

#writing to a file
file = open("data.txt", "w")
file.write("Hey there!")
file.close()

file = open("output.txt", "w")
file.write("This is a sample\n")
file.write("This is a sample\n")
file.write("This is a sample\n")
file.close()

#append

file = open("output.txt", "a")
file.write("This is the added info")
file.close()

file_path = r"C:\Users\314263\Repos\play-wright\tests\newtext.txt"
with open(file_path, "w") as file:
    file.write("Hey there ...")
print("file created successfully")

#writing data into csv file
import csv 
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age", "course"])
    writer.writerow(["A", "23", "Java"])
    writer.writerow(["B", "22", "Playwright"])
    writer.writerow(["C", "23", "C++"])
    writer.writerow(["D", "24", "Java"])
print("csv file created")