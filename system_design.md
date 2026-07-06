# Software System Design

## Task 2.1 Requirements and Architecture Choice

### (a) Functional Requirements

1. User Authentication (Login/Logout)
2. Students can view marks and enroll in courses.
3. Admin can manage students, courses, and faculty.

### Non-Functional Requirements

| Non-Functional Requirement | Design Principle |
| Supports 50,000 concurrent users | Scalability |
| System remains available during peak traffic | Availability |
| Protects user accounts and sensitive student data | Security |

---

### (b) Monolithic vs Microservices

| Feature | Monolithic | Microservices |
| Deployment | Entire application deployed together | Independent deployment of services |
| Fault Isolation | Failure affects whole application | Failure isolated to one service |
| Complexity | Simple | Higher |

**Recommendation**

Microservices architecture is recommended because it supports independent scaling, better fault isolation, and easier deployment for a system handling 50,000 concurrent users.

---

# Task 2.2 High-Level Design

## (a) Main Components

| Component | Responsibility | Interface |
| Authentication Service | Login and authentication | REST API |
| Student Portal | View marks and enroll courses | REST API |
| Admin Panel | Manage students, faculty and courses | REST API |
| Database | Store application data | SQL Queries |

---

## (b) Layered Architecture

### Presentation Layer

**Receives:**
- Login requests
- Course enrollment requests
- Marks viewing requests

**Passes:**
- User input to the Business Layer

---

### Business Layer

**Receives:**
- Requests from the Presentation Layer

**Processes:**
- Authentication
- Course enrollment
- Marks calculation
- Business rules

**Passes:**
- Database operations to the Data Access Layer

---

### Data Access Layer

**Receives:**
- SQL operations from the Business Layer

**Processes:**
- Reads and writes data in the database

**Passes:**
- Query results back to the Business Layer

---

## (c) Scaling Strategy

Horizontal scaling should be used because multiple web servers can be added to handle heavy traffic.

A Load Balancer distributes requests among all servers.

**Load Balancing Algorithm:** Round Robin

Round Robin distributes requests evenly across available servers.

---

## (d) Elasticity

Elasticity automatically increases the number of servers during examination result publication and decreases the number of servers during semester breaks, reducing infrastructure cost while maintaining application performance.

---

## (e) Session Problem

If Server A creates a session and the next request goes to Server B, the user session is unavailable because the session exists only on Server A.

### Solution 1

Use **Sticky Sessions** at the Load Balancer.

**Trade-off:** Poor load distribution and reduced fault tolerance if a server fails.

### Solution 2

Use a **Shared Session Store** (Redis or Database).

**Trade-off:** Additional infrastructure cost but provides better scalability, reliability, and session availability.
