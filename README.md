## Architecture

The system is designed using a layered architecture with Authentication, Student Portal, and Admin Panel modules. The application is suitable for high concurrency using horizontal scaling and load balancing.

## SOLID Principles

- Student class follows Single Responsibility Principle.
- Enrollment class is open for extension using inheritance.
- EnrollmentRepository demonstrates Dependency Inversion Principle.

## Singleton Pattern

DatabaseConnection is implemented as a thread-safe Singleton using double-checked locking to ensure only one shared database connection exists.

## Observer Pattern

MarksUpdateNotifier notifies EmailNotifier and AuditLogNotifier whenever a student's marks are updated. This keeps the Admin Panel loosely coupled with notification services.

## Fault Tolerance

The system uses primary-replica replication for database redundancy. If the primary server fails, the replica can be promoted to continue serving requests with minimal downtime.
