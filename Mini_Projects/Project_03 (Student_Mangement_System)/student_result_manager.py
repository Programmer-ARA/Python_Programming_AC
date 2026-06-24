class Student:
    def __init__(self, name, std, marks):
        self.name =  [name]
        self.std = std
        self.marks = marks

    def get_data(self):
        print("Name: ", str(self.name ))
        print("Class: ", self.std )
        print("Marks: ", self.marks)
        print("\n")
    
    def get_result(self):
        if(self.marks >= 50):
            return "Pass"
        else:
            return "Fail"
        
student = {}

print("\n------- Welcome to Student Management Window ------")

while True:
    
    print("1. Add Student")
    print("2. View Student Details")
    print("3. Check Results")
    print("4. Exit")

    option = input("Please Choose from Above Options: \t")


    # add student
    if (option == "1"):
        print("\n------ Add Student ------\n")

        name = input("Enter Student's Name:\t").strip()
        std = int(input("Enter Student's Class:\t"))
        marks = int(input("Enter Student's Marks:\t"))
        
        print(name,"added successfully.")

        student[name] = Student(name, std, marks) # Storing data


    # view student
    elif (option == "2"):
        print("\n------ Student Detail ------\n")

        view = input("Enter the Student's Name: \t").strip()

        if view not in student:
            print("Student is not in the database")
            continue
        else:
            student[view].get_data()

    # check result
    elif (option == "3"):
        print("\n------ Check Results ------\n")

        result = input("Enter Name:\t").strip()

        if result not in student:
            print("Student is not in the database")
            continue

        print(student[result].get_result())
        
    # exit
    elif (option == "4"):
        break

    else:
        print("Please Choose Correct Option")