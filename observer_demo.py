from abc import ABC, abstractmethod


class Observer(ABC):

    @abstractmethod
    def update(self, student_id, new_marks):
        pass


class EmailNotifier(Observer):

    def update(self, student_id, new_marks):
        print(f"Email sent for Student {student_id}: Marks = {new_marks}")


class AuditLogNotifier(Observer):

    def update(self, student_id, new_marks):
        print(f"Audit Log: Student {student_id} updated to {new_marks}")


class MarksUpdateNotifier:

    def __init__(self):
        self.observers = []

    def register(self, observer):
        self.observers.append(observer)

    def unregister(self, observer):
        self.observers.remove(observer)

    def notify(self, student_id, new_marks):
        for observer in self.observers:
            observer.update(student_id, new_marks)


if __name__ == "__main__":
    notifier = MarksUpdateNotifier()

    email = EmailNotifier()
    audit = AuditLogNotifier()

    notifier.register(email)
    notifier.register(audit)

    notifier.notify(101, 95)
