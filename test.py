from student import Student

print("Testing the Stiudent class")
s1 = Student()

s1.FirstName = input("First Name: ")
s1.LastName = input("Last Name: ")

print(s1.getFullName())
