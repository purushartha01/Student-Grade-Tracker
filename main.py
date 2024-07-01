class Student:
    def __init__(self,grades):
        self.grades=grades
        self.avgGrade=0


    def getGrades(self):
        return self.grades
    
    def calculateAvgGrade(self):
        total=0
        for g in self.grades:
            total+=g
        
        self.avgGrade=total/len(self.grades)

    def getAvgGrade(self):
        self.calculateAvgGrade()
        return self.avgGrade
    
    def getAlphabetGrade(self):
        finalGrade=self.getAvgGrade()
        if finalGrade>4 and finalGrade<=5:
            return 'A'
        elif finalGrade>3 and finalGrade<=4:
            return 'B'
        elif finalGrade>2 and finalGrade<=3:
            return 'C'
        elif finalGrade>1 and finalGrade<=2:
            return 'D'
        elif finalGrade>0 and finalGrade<=1:
            return 'E'
        elif finalGrade==0:
            return 'F'


if __name__=="__main__":

    subjects=int(input("Enter number of Subjects: "))

    grades=[]


    for i in range(subjects):
        grade=int(input("Enter grade(range: 0(for worst)-5(for best)): "))
        while(grade<0 or grade>5):
            print("Grade must be in range 0-5")
            grade=int(input("Enter grade(range: 0(for worst)-5(for best)): "))
        grades.append(grade)

    Student=Student(grades)

    print("Average Grade point: ",Student.getAvgGrade(),"\nGrade: ",Student.getAlphabetGrade())
    