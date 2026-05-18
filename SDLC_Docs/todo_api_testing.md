# Todo Planner - API Testing & Validation Document

This document outlines the testing strategy, validation steps, and tools used for the Todo-related APIs in the Minimalist To-Do Application.

## 1. API Testing Strategy

The testing strategy focuses on ensuring that all CRUD operations for tasks are functional, performant, and secure. The approach combines manual verification for UI interaction and automated testing for API integrity.

- **Objective**: Validate correctness of data persistence, state transitions (Active -> Completed), and search/filter logic.
- **Environment**: Local development (`http://localhost:8000` for Backend, `http://localhost:5173` for Frontend).
- **Scope**: Exclusive to Todo-specific endpoints.

---

## 2. Validation Steps

### A. Task Creation (`POST /todos/`)
- **Step 1**: Send a POST request to `/todos/` with a JSON body containing `title`, `description`, `category`, `priority`, and `due_date`.
- **Validation**:
    - Status code `201` (Created) or `200` (OK) depending on backend implementation.
    - Response body should contain the generated task `id` and all submitted fields.
    - **Edge Case**: Verify behavior when sending an empty `title` (should fail with `422`).

### B. Task Listing (`GET /todos/`)
- **Step 1**: Send a GET request to `/todos/`.
- **Validation**:
    - Status code `200`.
    - Response should be a list of todo objects.
- **Step 2**: Apply `category` query parameter (e.g., `/todos/?category=Work`).
- **Validation**:
    - Returned list should only contain tasks matching the specified category.

### C. Task Update & Completion (`PUT /todos/{todo_id}`)
- **Step 1**: Send a PUT request with `completed=true` to an existing task ID.
- **Validation**:
    - Status code `200`.
    - Field `completed` in response must be `true`.
- **Step 2**: Submit updates to `title` or `priority`.
- **Validation**:
    - Verify the specific updated field reflects the new value.

### D. Task Deletion (`DELETE /todos/{todo_id}`)
- **Step 1**: Send a DELETE request to a valid task ID.
- **Validation**:
    - Status code `200` (or `204`).
    - Attempting to GET or DELETE the same ID again should return `404` (Not Found).

---

## 3. Tools and Approach

### 🛠 Manual Testing
- **Swagger UI**: Accessible at `http://localhost:8000/docs`. Used for interactive API exploration and quick validation of schema requirements.
- **Browser Developer Tools**: Used to monitor network requests initiated by the React frontend via Axios.

### 🤖 Automated Testing (Recommended)
- **Pytest**: Used for backend unit and integration tests.
- **Postman/Newman**: For automated API collection runs and regression testing.
- **Cypress/Playwright**: For end-to-end testing of the full API-to-UI flow.

---

## 4. Requirement Coverage
| Feature | API Endpoint | Coverage |
|---------|--------------|-----------|
| Create Task | `POST /todos/` | ✅ |
| List All Tasks | `GET /todos/` | ✅ |
| Category Filtering | `GET /todos/?category=...` | ✅ |
| Toggle Completion | `PUT /todos/{id}` | ✅ |
| Delete Task | `DELETE /todos/{id}` | ✅ |
