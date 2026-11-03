# 🤖 AI Management Agent

A bilingual (Persian/English) AI-powered system that generates comprehensive management reports based on the four fundamental functions of management: **Planning, Organizing, Leading, and Controlling**.

![Version](https://img.shields.io/badge/version-2.0.0-blue)
![Python](https://img.shields.io/badge/python-3.12-blue)
![React](https://img.shields.io/badge/react-18-61dafb)
![License](https://img.shields.io/badge/license-Academic-green)

---

## 🎯 Overview

This project is a complete, production-ready management analysis tool that:

- 🌐 **Accepts topics in Persian or English** with seamless language switching.
- 🧠 **Analyzes using AI** (Llama 3 via OpenRouter) to generate academically sound insights.
- 📊 **Generates structured 12-section reports** with clean Markdown formatting.
- 💰 **Handles Iranian Toman (تومان) and USD** intelligently based on the selected language.
- 📚 **Archives reports** in a local SQLite database with full CRUD operations.
- 🎨 **Features a stunning ocean-themed UI** with glassmorphism effects and full RTL support.

Built for the **Management Principles** university course, this project demonstrates the intersection of classical management theory and modern AI software engineering.

---

## 🏗️ Architecture

```text
┌─────────────────────────────────────────────────────┐
│               Frontend (React + Vite)               │
│   Tailwind CSS v4 • Ocean Dark Theme • Bilingual    │
└──────────────────────────┬──────────────────────────┘
                           │ REST API (JSON)
                           ▼
┌─────────────────────────────────────────────────────┐
│              Backend (FastAPI + Python)             │
│      Pydantic • Tenacity • OpenAI SDK • SQLite      │
└──────────────────────────┬──────────────────────────┘
                           │
            ┌──────────────┴──────────────┐
            ▼                             ▼
    ┌──────────────┐              ┌──────────────┐
    │  OpenRouter  │              │   SQLite     │
    │   (Llama 3)  │              │  Database    │
    └──────────────┘              └──────────────┘
```

---

## 📁 Project Structure

This is a monorepo containing both the backend and frontend applications.

```text
management_agent/
├── backend/                 # FastAPI Backend Application
│   ├── api/                 # Serverless entry point (for Vercel)
│   ├── prompts/             # LLM prompt templates (Markdown)
│   ├── services/            # Business logic and orchestration
│   ├── tests/               # Unit and integration tests
│   ├── app.py               # Main FastAPI application & endpoints
│   ├── config.py            # Pydantic settings management
│   ├── database.py          # SQLite CRUD operations
│   ├── models.py            # Pydantic data models
│   ├── requirements.txt     # Python dependencies
│   └── README.md            # Detailed backend API documentation
│
├── frontend/                # React Frontend Application
│   ├── src/
│   │   ├── components/      # Reusable React components
│   │   ├── contexts/        # Global state (Language context)
│   │   ├── i18n/            # Translation dictionaries
│   │   └── services/        # API client functions
│   ├── index.html
│   ├── package.json         # Node.js dependencies
│   └── README.md            # Frontend setup instructions
│
├── .gitignore               # Global ignore rules
└── README.md                # This file (Root documentation)
```

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.12+** installed on your system.
- **Node.js 18+** and `npm` installed.
- A free **OpenRouter API key** (get one at [openrouter.ai](https://openrouter.ai)).

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/management-agent.git
cd management-agent
```

### 2. Backend Setup

Open your terminal and navigate to the backend directory:

```bash
cd backend

# Create and activate a virtual environment
# Windows:
python -m venv venv
venv\Scripts\activate
# macOS/Linux:
# python3 -m venv venv
# source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Configure environment variables
# Create a .env file and add your OpenRouter API key:
# OPENROUTER_API_KEY=your_api_key_here
# LLM_MODEL=meta-llama/llama-3-8b-instruct:free
# LLM_TIMEOUT=60
# MAX_INPUT_CHARS=2000

# Run the development server
python app.py
```
*The backend will be available at `http://127.0.0.1:8000`*  
*Interactive API docs: `http://127.0.0.1:8000/docs`*

### 3. Frontend Setup

Open a **new terminal** window and navigate to the frontend directory:

```bash
cd frontend

# Install Node.js dependencies
npm install

# Run the development server
npm run dev
```
*The frontend will be available at `http://localhost:5173`*

---

## 🌟 Key Features

### 🧠 AI-Powered Management Analysis
Utilizes the classical **4 functions of management** framework (Henri Fayol):
1. **Planning**: SMART goals, objectives, milestones, and budget estimation.
2. **Organizing**: RACI matrix, resource allocation, and task distribution.
3. **Leading**: Leadership styles, motivation strategies, and communication plans.
4. **Controlling**: KPIs, monitoring frequencies, and corrective feedback loops.

### 🌐 Full Bilingual Support (i18n)
- **Persian (Farsi)**: Complete Right-to-Left (RTL) layout support, Vazirmatn font integration, and localized terminology.
- **English**: Professional formatting with automatic USD currency conversion.
- **Instant Switching**: Change languages on the fly without reloading the page.

### 💰 Smart Currency Handling
- Persian reports use **Iranian Toman (تومان)** with realistic 2024-2026 market estimates.
- English reports automatically convert financial figures to **USD ($)**.
- All financial figures are clearly marked as "illustrative estimates" for academic integrity.

### 🎨 Modern UI/UX Design
- **Ocean Dark Theme**: Deep navy backgrounds with cyan and champagne gold accents.
- **Glassmorphism**: Frosted glass card effects for a premium, modern look.
- **Fully Responsive**: Optimized for mobile, tablet, and desktop screens.

### 📚 Report Management & Archiving
- **Automatic Saving**: Every generated report is saved to a local SQLite database.
- **CRUD Operations**: View, edit titles, and delete past reports effortlessly.
- **Markdown Export**: Download any report as a `.md` file for offline use or Word conversion.

---

## 📚 API Documentation

The backend exposes a robust, RESTful API. For a complete list of endpoints, request/response models, and cURL examples, please refer to the detailed backend documentation:

👉 **[View Full Backend API Documentation](./backend/README.md)**

**Quick Summary of Core Endpoints:**

| Method | Endpoint | Description |
|:-------|:---------|:------------|
| `GET` | `/api/health` | Check API health and active model status. |
| `POST` | `/api/generate-report` | Generate a new management report (accepts `topic` and `language`). |
| `GET` | `/api/reports` | Retrieve a metadata list of all saved reports. |
| `GET` | `/api/reports/{id}` | Retrieve full details of a specific report by UUID. |
| `PUT` | `/api/reports/{id}/title` | Update the title of an existing saved report. |
| `DELETE` | `/api/reports/{id}` | Permanently delete a report from the database. |

---

## 🛠️ Tech Stack

### Backend
- **Python 3.12**: Core programming language.
- **FastAPI**: High-performance, modern web framework.
- **Pydantic v2**: Robust data validation and settings management.
- **OpenAI Python SDK**: Configured for seamless OpenRouter LLM integration.
- **SQLite**: Lightweight, serverless database for report archiving.
- **Tenacity**: Automatic retry logic for resilient API calls.
- **Uvicorn**: ASGI server for local development.

### Frontend
- **React 18**: Component-based UI library.
- **Vite**: Next-generation, blazing-fast frontend build tool.
- **Tailwind CSS v4**: Utility-first CSS framework for rapid styling.
- **React Markdown**: Secure rendering of LLM-generated Markdown content.
- **Vazirmatn**: Standard, highly legible Persian/Arabic font.

---

## 🧪 Testing

The backend includes a test suite to ensure data integrity and pipeline reliability without consuming API credits.

```bash
cd backend
pytest tests/ -v
```

**Test Coverage Includes:**
- ✅ Pydantic model validation (nested structures).
- ✅ Mocked pipeline execution order verification.
- ✅ Bilingual report generation logic.

---

## ☁️ Deployment

This project is structured and configured for easy cloud deployment.

### Frontend (Vercel)
The frontend is optimized for Vercel. Simply connect your GitHub repository to Vercel, set the `VITE_API_URL` environment variable to your backend's production URL, and deploy.

### Backend (Render / Vercel)
The backend includes:
- `api/index.py`: Entry point for Vercel serverless functions.
- `runtime.txt`: Specifies Python 3.12 for build environments.
- `requirements.txt`: Standardized dependency list.

*Note: For production environments, it is recommended to migrate the local `reports.db` to a cloud-hosted database like Turso or PostgreSQL to ensure persistent storage across serverless instances.*

---

## 🎓 Academic Context

This project was developed as a comprehensive university assignment for a **Management Principles** course. It successfully demonstrates:

1. **Classical Management Theory**: Practical application of Fayol's 4 functions of management.
2. **Modern AI Engineering**: Effective LLM integration with strict structured output (JSON) enforcement.
3. **Software Architecture**: Clean separation of concerns (Services, Models, API routes, Prompts).
4. **Internationalization (i18n)**: Full bilingual support with dynamic RTL/LTR layout switching.
5. **Database Design**: Implementation of CRUD operations with local SQLite.
6. **API Design**: RESTful principles with comprehensive error handling and auto-generated documentation.

---

## 📄 License

This project is created strictly for **academic and educational purposes**.

---

## 🙏 Acknowledgments

- **OpenRouter** for providing accessible and free LLM API tiers for development.
- **FastAPI** and **React** communities for their outstanding documentation and developer experience.
- **Henri Fayol & Peter Drucker** for the foundational management theories that power this agent's logic.

---

<div align="center">
 
*Combining classical management wisdom with modern AI engineering*

</div>