class Person:
    def __init__(self, name, address):
        self.__name = name
        self.__address = address

    def setName(self, name):
        self.__name = name 
    def setAddress(self, address):
        self.__address = address
    
    def getName(self):
        return self.__name
    def getAddress(self):
        return self.__address
    
    def __str__(self):
        return "Name: {} Address: {}".format(self.getName(), self.getAddress())
        
class Student(Person):
    def __init__(self, name, address):
        super().__init__(name, address)
        self.__numCourses = 0
        self.__courses = []
        self.__grades = []
        
    def addCourseGrade(self,course,grade):
        self.__courses.append(course)
        self.__grades.append(grade)
        self.__numCourses+=1

    def printGrades(self):
        for i in range(self.__numCourses):
            print(self.__courses[i], end=" ")
            print(self.__grades[i])

    def getAverageGrade(self):
        return sum(self.__grades)/len(self.__grades)

    
    def __str__(self):
        return "Student: name(address)".format(self.__name,self.__address)


class Teacher(Person):
    def __init__(self, name, address):
        super().__init__(name, address)
        self.__numCourses = 0
        self.__courses = []
    
    def addCourse(self, course):
        if course in self.__courses:
            return False
        else:
            self.__courses.append(course)
            self.__numCourses +=1
        
    def removeCourse(self, course):
        if course not in self.__courses:
            return False
        else:
            self.__courses.remove(course)
            self.__numCourses -=1
    def printCourses(self):
        print(self.__courses)

    def __str__(self):
        return "Teacher: name(address)".format(self.__name, self.__address)
    

        

# the object 
studObject1 = Student("Jess","jkt")
studObject1.addCourseGrade("maths", 100)
studObject1.addCourseGrade("english", 89)
studObject1.printGrades()
studObject1.getAverageGrade()