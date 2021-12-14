from personClass import Student, Teacher


studObject1 = Student("David","idn")
studObject1.addCourseGrade("maths", 100)
studObject1.addCourseGrade("english", 89)
studObject1.printGrades()
studObject1.getAverageGrade()

teacherObject1 = Teacher("Brian","idn")
teacherObject1.addCourse("MATH1123E")
teacherObject1.addCourse("MATH1123E")
teacherObject1.addCourse("SCI342R")

teacherObject1.printCourses()

teacherObject1.removeCourse("SCI342R")
teacherObject1.printCourses()