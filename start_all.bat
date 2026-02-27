@echo off
echo ==============================================================
echo   To-Do App Application Startup
echo ==============================================================
echo This script will set up the database, install all requirements, 
echo and start both the backend and frontend servers automatically.
echo.

:: Start the Backend in a new window
echo Starting Backend...
start "To-Do Backend" cmd /c "cd backend && if not exist venv (python -m venv venv) && call venv\Scripts\activate && pip install -r requirements.txt && python run.py"

:: Start the Frontend in a new window
echo Starting Frontend...
start "To-Do Frontend" cmd /c "cd frontend && npm install && npm run dev"

echo Both services are starting up in separate windows!
echo Once they finish installing dependencies, the app will be live.
echo.
pause
