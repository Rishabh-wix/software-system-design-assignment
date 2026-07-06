import threading


class DatabaseConnection:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def get_connection(self):
        return "Shared Database Connection"


if __name__ == "__main__":
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()

    print(db1.get_connection())
    print(db1 is db2)

# Double-checked locking ensures only one instance is created.
# Without locking, multiple threads could create multiple instances.
