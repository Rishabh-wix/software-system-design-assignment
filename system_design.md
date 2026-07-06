# Software System Design

## Task 2.1 Requirements and Architecture Choice

### (a) Functional Requirements

1. User Authentication (Login/Logout)
2. Students can view marks and enroll in courses.
3. Admin can manage students, courses, and faculty.

### Non-Functional Requirements

| Requirement | Design Principle |
| Scalability | Supports 50,000 concurrent users |
| Availability | System remains available during peak traffic |
| Security | Protects user accounts and sensitive student data |

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

Receives user requests through browser or mobile application and sends responses to users.

### Business Layer

Processes business logic such as enrollment, authentication, and marks calculation.

### Data Access Layer

Reads and writes data from the database using SQL queries.

---

## (c) Scaling Strategy

Horizontal scaling should be used because multiple web servers can be added to handle heavy traffic.

A Load Balancer distributes requests among all servers.

**Load Balancing Algorithm:** Round Robin

Round Robin distributes requests evenly across available servers.

---

## (d) Elasticity

Elasticity automatically increases the number of servers during examination result publication and decreases servers during semester breaks, reducing infrastructure cost.

---

## (e) Session Problem

If Server A creates a session and the next request goes to Server B, the user session is unavailable.

### Solution 1

Sticky Sessions at the Load Balancer.

**Trade-off:** Poor load distribution.

### Solution 2

Use a Shared Session Store (Redis or Database).

**Trade-off:** Additional infrastructure cost but better scalability.
