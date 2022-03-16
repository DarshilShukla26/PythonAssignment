# 20CE137 Darshil Shukla

class Student:
    def __init__(self):  
        self.name = ""
        self.rollNo = 0

    def takeStudentData(self):  
        self.name = input("Enter the name of student : ")
        print("Enter the roll number of", self.name, ": ", end="")
        self.rollNo = input()

    def StudentData(self): 
        print("\nStudent name is", self.name)
        print("Roll number of", self.name, "is", self.rollNo)


class Exam(Student):  
    def __init__(self):  
        Student.__init__(self)
        self.arr = []

    def takeInput(self):  
        for i in range(0, 6):
            print("Enter the marks of subject", i + 1, ":", end=" ")
            n = int(input())
            self.arr.append(n)

    def printData(self):  
        print(self.name, "Your marks is ", end="")
        print(self.arr)


class Result(Exam):  
    def __init__(self):  
        Exam.__init__(self)
        self.total_marks = 0

    def calculateAvg(self):  
        self.check = True
        for i in range(0, 6):
            if (self.arr[i] < 33):  
                print(self.name, "you are fail in subject:", i + 1)
                self.check = False
                break
            self.total_marks = self.total_marks + self.arr[i]

        if (self.check):
            print("Total marks is", self.total_marks)
            print(self.name, "You get", self.total_marks / 6, "%")


st = Student()
exam = Exam()
result = Result()

result.takeStudentData()
result.takeInput()

result.StudentData()
result.printData()
result.calculateAvg()