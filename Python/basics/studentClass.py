class Student():
    def __init__(self,name, classroom, regNumber):
        self.name = name
        self.classroom = classroom
        self.regNumber = regNumber
        self.subject = {}
    
    def __str__(self):
        tempStr = {i:self.subject[i] for i in self.subject}
        return(f"{self.name} / {self.regNumber} / {self.classroom}: {tempStr}")
    
    def updateRollNumber(self,newRollNumber):
        self.regNumber = newRollNumber
    
    def updateScore(self, subject, score):
        self.subject[subject] = score 

class Classroom():
    studentDict = {}

    def addStudent(self,name, classroom, regNumber):
        self.studentDict[regNumber] = Student(name, classroom, regNumber)

    def addTestResult(self,regNumber, marksheet):
        for i in marksheet.keys():
            self.studentDict[regNumber].updateScore(i, marksheet[i])

    def __str__(self):
        res = ''
        for i in self.studentDict.keys():
            res += str(self.studentDict[i]) + '\n'
        return(res)
    

student1 = Student("Basil","MCA1",1)
student2 = Student("Ashmin","MCA1",2)
student3 = Student("Renjith","MCA2",3)

student1.updateScore("Math",100)
student1.updateScore("Sci",99)
student1.updateScore("Eng",80)

student2.updateScore("Math",99)
student3.updateScore("Sci",91)
student2.updateScore("Eng",89)

print(student1)
print(student2)
print(student3)

# classMCA = Classroom()

# print("Current Table")
# print(classMCA)

# classMCA.addStudent("Basil","MCA1",1)
# classMCA.addStudent("Ashwin","MCA1",2)
# classMCA.addStudent("Ashmin","MCA2",3)
# classMCA.addStudent("Renjith","MCA3",4)
# classMCA.addStudent("Aditya","MCA4",5)

# print("Current Table")
# print(classMCA)


# classMCA.addTestResult(1,{"Math":100,"Science":90,"Social":95})
# classMCA.addTestResult(4,{"Math":90,"Social":85})

# print("Current Table")
# print(classMCA)




# student1 = Student("Basil","MCA1",1)



# {
#     1: Student("Basil","MCA1",1),
#     2: Student("Ashwin","MCA1",2),
#     3: Student("Ashmin","MCA2",3),
#     4: Student("Renjith","MCA2",4)
# }