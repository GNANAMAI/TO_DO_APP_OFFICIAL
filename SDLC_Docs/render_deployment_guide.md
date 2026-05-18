# Deployment Document - Render (Todo Planner)

This document provides a comprehensive guide for deploying and maintaining the Todo Planner application on Render. It covers both the FastAPI backend and the React frontend.

## 1. Deployment Strategy

### A. FastAPI Backend (Web Service)
- **Service Type**: Web Service
- **Runtime**: Python 3.10+
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
- **Root Directory**: `backend/`

### B. React Frontend (Static Site)
- **Service Type**: Static Site
- **Build Command**: `npm install && npm run build`
- **Publish Directory**: `dist`
- **Root Directory**: `frontend/`

---

## 2. Environment Configuration

### Backend Environment Variables
| Variable | Value | Description |
|----------|-------|-------------|
| `DATABASE_URL` | `sqlite:///./todos.db` | Path to the production database file. |
| `ALLOWED_ORIGINS` | `https://your-frontend-url.onrender.com` | The public URL of your static site. |

> [!CAUTION]
> If using SQLite on Render, you **MUST** attach a **Persistent Disk** to the `/opt/render/project/src/backend/` directory to prevent data loss on service restarts. Alternatively, use a managed Render PostgreSQL.

### Frontend Environment Variables
| Variable | Value | Description |
|----------|-------|-------------|
| `VITE_API_URL` | `https://your-backend-url.onrender.com` | The public URL of your backend service. |

---

## 3. Docker Setup
While Render can deploy directly from the source code using the commands above, a basic `Dockerfile` for the backend is recommended for local-production parity:

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## 4. CI/CD Pipeline Steps

Render's built-in Git integration handles the CI/CD pipeline:
1.  **Commit**: Push changes to the `main` branch.
2.  **Trigger**: Render detects the push and triggers a new build.
3.  **Build**: Runs the `Build Command` specified for each service.
4.  **Health Check**: Render waits for the backend to pass a health check on the assigned port.
5.  **Traffic Switch**: If healthy, Render routes traffic to the new version.

---

## 5. Maintenance Operations

### 🔄 Pulling Latest Changes
- Render automatically pulls the latest changes from your connected GitHub/GitLab repository whenever you push to your tracked branch.

### 🛠 Applying Migrations
To apply database migrations to your production SQLite database:
1.  Navigate to your **Backend Service** in the Render Dashboard.
2.  Click on the **Shell** tab (requires instance to be running).
3.  Execute the migration script:
    ```bash
    python migrate_db.py
    ```

### 🔑 Updating Environment Variables
1.  Go to the **Environment** tab of your service.
2.  Add/Update the variables listed in Section 2.
3.  Render will automatically trigger a redeploy to apply the new values.

### 🚀 Restarting Services
If the service hangs or needs a refresh:
1.  Click the **Manual Deploy** button in the top right.
2.  Select **Restart Service** or **Clear Cache and Deploy** for a fresh build.

---

## 6. Monitoring Setup
- **Log Streams**: Use the **Logs** tab in the Render dashboard to view real-time `uvicorn` and application logs.
- **Downtime Alerts**: Use an external service like **UptimeRobot** or Render's built-in service monitoring (for paid tiers) to receive alerts if the API endpoints become unreachable.

---

## 7. Rollback Strategy
If a deployment fails:
1.  Identify the last successful build in the **Events** or **Deploys** tab.
2.  Select **Rollback to this version** from the build options.
3.  Verify the service stabilizes.
