"""
doc.................

"""
class Student :
    _id_counter = 1
    
    def __init__(self,name):
        self.name = name
        student._id_counter += 1
        self.student_id = student._id_counter
        self.grade = {}
        self.enrolled_courses = []
    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Grades : {self.grade}"    
    
    def __repr__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Grades : {self.grade}"    
    
    def info(self) :
        return s1.name
    
    def add_grade(self,course_id,grade) :
        self.grade[course_id] = grade
    def enrolled_in_course(self,course_name) :
        self.enrolled_courses.append(course_name)