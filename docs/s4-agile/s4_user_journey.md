## 🧭 User Journey – US033: Manual Task Workflow (Sprint 4 – Final)

This user journey describes how a typical end user interacts with the **TaskTracker API and UI layer** to complete the full end-to-end task management workflow. This reflects the **final “as-is” state of the Group Project system in Sprint 4**.

This journey supports:
- **US039 – View Time Created in Task Summary**
- **US031 – Show Current Time via External API**
- **PR-7 – Full Regression Testing**
- **PR-8 – Robot Framework Acceptance Tests**

---

### 👤 User Role
**End User**

---

### 🎯 Goal
Create a task, verify its creation timestamp, complete it, and retrieve a task report while validating the current time.

---

```mermaid
journey
    title US033 – Manual Task Workflow (Sprint 4 – Final)

    section Create Task
      Send POST request to /api/tasks: 5: User
      System validates input & generates createdAt timestamp: 3: System
      System stores task in JSON repository: 3: System
      System returns created task with timestamp: 4: System

    section View Task List
      Send GET request to /api/tasks: 5: User
      System returns list of tasks with createdAt values: 4: System

    section Complete Task
      Send PUT request to /api/tasks/{id}: 4: User
      System marks task as completed: 3: System

    section View Current Time
      Send GET request to /api/time: 5: User
      System returns current time and timezone: 4: System

    section Delete Task
      Send DELETE request to /api/tasks/{id}: 4: User
      System removes task from repository: 3: System
