from abc import ABC, abstractmethod


class Student:
    def __init__(self, student_id: int, name: str, email: str):
        self.student_id = student_id
        self.name = name
        self.email = email

    def view_marks(self) -> None:
        print(f"{self.name} is viewing marks.")

    def enroll_course(self, course_code: str) -> None:
        print(f"{self.name} enrolled in {course_code}")


class Enrollment:
    def __init__(self, enrollment_id: int, student_id: int, course_code: str):
        self.enrollment_id = enrollment_id
        self.student_id = student_id
        self.course_code = course_code

    def enroll(self) -> None:
        print("Enrollment successful.")

    def drop_course(self) -> None:
        print("Course dropped.")


class WaitlistedEnrollment(Enrollment):
    def enroll(self) -> None:
        print("Student added to waitlist.")


class EnrollmentRepository(ABC):

    @abstractmethod
    def save(self, enrollment: Enrollment):
        pass

    @abstractmethod
    def find_by_student(self, student_id: int):
        pass

    @abstractmethod
    def delete(self, enrollment_id: int):
        pass
