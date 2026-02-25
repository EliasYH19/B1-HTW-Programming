class Person:
    """Base class representing a person"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

class Student(Person):
    """Student class inheriting from Person"""
    def __init__(self, name, age, student_id):
        super().__init__(name, age) # Call parent constructor
        self.student_id = student_id
        
    def introduce(self):
        # Override parent method with student-specific info
        return f"Hi, I'm {self.name}, a student. My ID is {self.student_id} and I'm {self.age} years old."

class Teacher(Person):
    """Teacher class inheriting from Person"""
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        
    def introduce(self):
        # Override parent method with teacher-specific info
        return f"Hello, I'm {self.name}, a teacher. I teach {self.subject} and I'm {self.age} years old."

# Testing the classes
student = Student("Alice", 16, "S001")
teacher = Teacher("Mr. Smith", 35, "Mathematics")

print("=== School Management System ===")
print(student.introduce())
print(teacher.introduce())
print(f"\nStudent age: {student.age}")
print(f"Teacher subject: {teacher.subject}")