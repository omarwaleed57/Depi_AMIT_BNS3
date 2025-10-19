class System_manger:
    
    def __init__(self):
        self.student = {}
        self.courses = {}
       
       
    def add_student(self,name):
        student = student(name)
        self.student[student.student_id] = student
        print("Student added succesfully")
        
        return student.student_id
    
    
    def remove_student(self,student_id):
        if student_id in self.student:
            student = self.student(student_id)
            if not student.enrolled_courses:
                del self.student(student_id)
                print("student removed succesfuly")
            else:
                print("student has enrolled courses. cannot remove")
        else:
            print("Invalid Student Id")
            
    def enroll_course(self,student_id,course_id):
        if student_id in self.student and course_id in self.courses:
            student = self.student[student_id]
            course = self.courses[course_id]
            
            if course.name not in student.enrolled_courses:
                student.enroll_in_course(course.name)
                course.enroll_student(student.name)
                print("student enrolled in course succesful")
            else:
                print("Student is already enrolled in the courses")
        else:
            print("Invalid Student or Course Id")
            
            
            
    def record_grade(self,studnt_id,course_id,grade):
        if studnt_id in self.student and course_id in self.courses:
            student = self.student[studnt_id]
            course = self.courses[course_id]
            student.add_grade(course.name,grade)
            print("Grade recorded succesful")
        else:
            print("Invalid student Id or course Id")
            
            
    def get_all_student(self):
        return list(self.student.values)
    
    
    def get_all_courses(self):
        return list(self.courses.values)
    
    