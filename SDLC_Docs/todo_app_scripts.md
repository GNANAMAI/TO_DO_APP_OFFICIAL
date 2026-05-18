# Todo App – Agent Prompt Scripts

---

## Script 1 – BRD Creation
**Skill:** `Business_analyst_agent.md`

I will provide you with a requirement:

The client wants a simple web-based Todo Planner that allows users to manage their daily tasks.
Users can create, update, prioritize, complete, and delete tasks through a clean and responsive web interface.

Task:
Generate a comprehensive Business Requirement Document (BRD) for the Todo Planner web application.

Output Requirement:
- Provide only the Business Requirement Document
- Do NOT create tasks, implementation files, or code
- Just directly create the BRD file in the referenced folder

---

## Script 2 – UI/UX Wireframes
**Skill:** `BRD file + design_agent.md`

I will provide you with a Business Requirement Document (BRD).

Task:
Based on the BRD, create a clear and simple UI/UX Wireframes Document for the Todo Planner web application.

Guidelines:
- Keep the language simple and clear
- Understandable for both technical and non-technical stakeholders
- Use bullet points where possible
- Provide sample wireframes in ASCII format only

---

## Script 3 – Architecture Design
**Skill:** `Architecture_agent.md`

I will provide you with:
1. Business Requirement Document (BRD)
2. UI/UX Wireframes Document

Task:
Create a complete Architectural Design Document for the Todo Planner web application.

The document must include:
1. Introduction – Purpose and high-level description
2. Architecture Overview – System architecture with ASCII diagram
3. Application Architecture:
   - Frontend: React.js
   - Backend: FastAPI (REST APIs)
   - Python Version: 3.10 or 3.11 only
   - Database: PostgreSQL (Neon DB)

Guidelines:
- Clear, structured, and easy to understand
- Suitable for developers, testers, and stakeholders
- Directly generate the Architecture Design Document

---

## Script 4 – Coding
**Skill:** `Coding_agent.md`

I will provide you with:
1. Business Requirement Document (BRD)
2. UI/UX Wireframes Document
3. Architectural Design Document

Task:
Build a complete, production-ready Todo Planner web application (backend + frontend).

Requirements:
1. Tech Stack – Follow the Architecture Design Document strictly
2. Backend:
   - FastAPI-based REST APIs
   - Python 3.10 / 3.11
   - Clean, modular, well-commented code
   - Full CRUD operations: create, read, update, delete, complete tasks
   - Database models and migrations included
3. Frontend:
   - React.js with modern responsive UI
   - Tailwind CSS or equivalent
   - Follow provided wireframes strictly
4. Database:
   - Use existing PostgreSQL Neon DB
   - Provide migration commands
5. Setup:
   - README with backend setup, frontend setup, .env templates
   - No Docker
   - Use .env files for frontend-backend connectivity

IMPORTANT:
- No dependency-related runtime errors
- List all dependencies clearly
- Do not install anything automatically
- Do not ask for confirmations

---

## Script 5 – Render Deployment Guide
**Skill:** `Deployment_agent.md`

Give me a deployment guide for Render explaining:
- How to deploy the Todo Planner (backend + frontend)
- Steps to: pull latest changes, apply migrations, update environment variables, restart services safely

Create this as a deployment guide document.

---

## Script 6 – API Testing
**Skill:** `testing_agent.md`

Create a separate testing and validation document (`todo_api_testing.md`) that explains:
- API testing strategy for the Todo Planner
- Validation steps for: task creation, task listing, task update, task deletion, task completion
- Tools and approach (manual + automated testing)
- Only include Todo-related APIs
