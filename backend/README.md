# 🤖 AI Management Agent - Backend

A robust, bilingual (Persian/English) FastAPI backend that generates comprehensive, structured management reports using Large Language Models (LLMs). It analyzes topics based on the four fundamental functions of management: Planning, Organizing, Leading, and Controlling.

## 🌟 Key Features

- 🌐 **Bilingual Support**: Seamlessly processes and generates reports in both Persian (Farsi) and English with dynamic prompt selection.
- 🧠 **AI-Powered Analysis**: Utilizes the OpenRouter API (Llama 3 models) to generate structured, academically sound management analyses.
- 💰 **Smart Currency Handling**: Automatically formats financial estimates in Iranian Toman (تومان) for Persian reports and USD ($) for English reports.
- 📊 **Structured Output**: Generates detailed, multi-section reports with clean Markdown formatting.
- 📚 **Report Archiving**: Built-in SQLite database for saving, retrieving, updating, and deleting generated reports (CRUD operations).
- 🛡️ **Robust & Resilient**: Implements automatic retry logic (via `tenacity`) and strict Pydantic validation to handle LLM hallucinations and API rate limits gracefully.
- 📖 **Auto-Documentation**: Fully documented RESTful API with interactive Swagger UI.

## 🛠️ Tech Stack

- **Language**: Python 3.12
- **Framework**: FastAPI
- **Data Validation**: Pydantic v2 & Pydantic-Settings
- **LLM Integration**: OpenAI Python SDK (configured for OpenRouter)
- **Database**: SQLite (Local, ready for Turso/PostgreSQL migration)
- **Utilities**: `tenacity` (retries), `python-dotenv` (environment management)

## 📁 Project Structure

```text
backend/
├── api/
│   └── index.py              # Vercel serverless function entry point
├── prompts/
│   ├── management_analysis.md       # Persian analysis prompt
│   ├── management_analysis_en.md    # English analysis prompt
│   ├── translate_fa_en.md           # Topic translation prompt
│   └── translate_report_en_fa.md    # Report translation prompt
├── services/
│   ├── llm_service.py               # OpenRouter API client with retry logic
│   ├── management_service.py        # Core analysis orchestration
│   ├── report_service.py            # Full pipeline coordination & formatting
│   └── translation_service.py       # Bilingual translation handling
├── tests/
│   ├── test_models.py               # Pydantic model validation tests
│   └── test_pipeline.py             # Mocked pipeline execution tests
├── app.py                    # FastAPI application & endpoints
├── config.py                 # Environment configuration
├── database.py               # SQLite CRUD operations
├── exceptions.py             # Custom error classes
├── models.py                 # Pydantic data models
├── prompt_loader.py          # Utility to load markdown prompts
├── requirements.txt          # Python dependencies
├── runtime.txt               # Python version specification for deployment
└── .gitignore
```

## 🚀 Local Setup

1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/management-agent.git
cd management-agent/backend
```

2. Create a Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install Dependencies

```bash
pip install -r requirements.txt
```

4. Configure Environment Variables

- Create a .env file in the root directory and add your credentials:
```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
LLM_MODEL=your_oprnrouter_model_name_here
LLM_TIMEOUT=60
MAX_INPUT_CHARS=2000
```
**(Get a free API key from [OpenRouter](https://openrouter.ai/))**

5. Run the Development Server

```bash
python app.py
```
**The server will start at http://127.0.0.1:8000.**

## 📚 API Documentation
**Once the server is running, you can explore the interactive API documentation:**
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## 📚 Core API Endpoints

The backend exposes a RESTful API for generating and managing management reports. All endpoints are prefixed with `/api`.

### 1. Health Check
Verify that the backend server is running and check the active LLM model.

- **Method**: `GET`
- **Endpoint**: `/api/health`
- **Response**:
  ```json
  {
    "status": "ok",
    "model": "meta-llama/llama-3-8b-instruct:free",
    "version": "2.0.0"
  }
  ```

### 2. Generate Management Report
The core endpoint. Analyzes a given management topic using the 4 fundamental functions of management and returns a structured, formatted report in the requested language.
- **Method**: `POST`
- **Endpoint***: `/api/generate-report`
- **Headers**: `Content-Type: application/json`
- **Request Body**:
  ```json
  {
  "topic": "برنامه‌ریزی برای راه‌اندازی یک کافی‌شاپ دانشجویی در دانشگاه",
  "language": "fa"
  }
  ```
- **Response (200 OK)**:
  ```json
  {
  "final_report": {
    "project_title": "طرح کسب‌وکار کافی‌شاپ دانشجویی",
    "executive_summary": "این گزارش به تحلیل جامع...",
    "problem_definition": "نیاز به فضای مطالعاتی و تفریحی...",
    "assumptions_and_constraints": [
      "بودجه محدود دانشجویی",
      "مقررات دانشگاه"
    ],
    "planning": "**اهداف:**\n- جذب ۱۰۰ دانشجو در ماه اول...",
    "organizing": "**نقش‌ها:**\n- مدیر کافی‌شاپ\n- باریستا...",
    "leading": "**سبک رهبری:** رهبری خدمتگزار...",
    "controlling": "**تناوب پایش:** هفتگی...",
    "kpis": "- **درآمد ماهانه**: هدف ۱۵۰ میلیون تومان...",
    "risks": "- **ریسک**: کاهش مراجعه در ایام امتحانات\n  - **راهکار**: ارائه تخفیف ویژه...",
    "final_recommendations": "با توجه به تحلیل فوق، توصیه می‌شود...",
    "conclusion": "این طرح چارچوب جامعی برای مدیریت موفق..."
  },
  "topic_en": "Planning to launch a student café at the university",
  "analysis_en": {
    "project_title": "Student Café Business Plan",
    "planning": {
      "objectives": ["Attract 100 students in the first month"],
      "resources_and_budget": "Initial capital: $16,000 (illustrative estimate)"
    }
  },
  "report_id": "550e8400-e29b-41d4-a716-446655440000"
  }
  ```

### 3. List All Reports
Retrieve a metadata list of all previously generated and saved reports, sorted by creation date (newest first). Ideal for populating the "Archive" view in the frontend.
- **Method**: `GET`
- **Endpoint**: `/api/reports`
- **Response (200 OK)**:
  ```json
  [
  {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "topic_fa": "برنامه‌ریزی برای راه‌اندازی یک کافی‌شاپ دانشجویی در دانشگاه",
    "created_at": "2024-10-25T14:30:00.000Z",
    "updated_at": "2024-10-25T14:30:00.000Z"
  },
  {
    "id": "660f9511-f30c-52e5-b827-557766551111",
    "topic_fa": "مدیریت یک تیم نرم‌افزاری دورکار",
    "created_at": "2024-10-24T10:15:00.000Z",
    "updated_at": "2024-10-24T10:15:00.000Z"
  }
  ]
  ```

### 4. Get Specific Report
Retrieve the full details of a single report using its unique UUID.
- **Method**: `GET`
- **Endpoint**: `/api/reports/{report_id}`
- **Path Parameter**: `report_id` (string)
- **Response (200 OK)**:
  ```json
  {
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "topic_fa": "برنامه‌ریزی برای راه‌اندازی یک کافی‌شاپ دانشجویی در دانشگاه",
  "topic_en": "Planning to launch a student café at the university",
  "analysis_en": { ... },
  "final_report": { ... },
  "created_at": "2024-10-25T14:30:00.000Z",
  "updated_at": "2024-10-25T14:30:00.000Z"
  }
  ```

### 5. Update Report Title
Modify the project_title of an existing saved report without regenerating the entire analysis.
- **Method**: `PUT`
- **Endpoint**: `/api/reports/{report_id}/title`
- **Path Parameter**: `report_id` (string)
- **Headers**: `Content-Type: application/json`
- **Request Body**:
  ```json
  {
  "title": "طرح به‌روزشده و نهایی کسب‌وکار کافی‌شاپ"
  }
  ```
- **Response (200 OK)**: Returns the updated full report object with the new title and updated `updated_at` timestamp.

### 6. Delete Report
Permanently remove a report and its associated data from the database.
- **Method**: `DELETE`
- **Endpoint**: `/api/reports/{report_id}`
- **Path Parameter**: `report_id` (string)
- **Response (200 OK)**:
  ```json
  {
  "status": "deleted",
  "id": "550e8400-e29b-41d4-a716-446655440000"
  }
  ```

## ⚠️ Error Handling
The API uses standard HTTP status codes to communicate the result of requests. All error responses return a JSON object with a `detail` key.

Status Code | Meaning | Description
:-----------|:--------|:------------
`200` | OK | Request was successful.
`400` | Bad Request | Invalid input (e.g., topic length < 5 characters, missing required fields, invalid language code).
`404` | Not Found | The requested `report_id` does not exist in the database.
`422` | Unprocessable Entity | Pydantic validation failed (e.g., sending a string instead of a JSON object).
`502` | Bad Gateway | LLM processing error (e.g., the AI failed to generate valid JSON, or the translation service failed).
`500` | Internal Server Error | Unexpected backend failure (e.g., database connection error).

## 🧪 Local Testing
You can test these endpoints locally using `curl` or tools like Postman or Insomnia.

*Example*: **Generate a Persian Report via cURL:**
  ```bash
  curl -X POST "http://127.0.0.1:8000/api/generate-report" \
     -H "Content-Type: application/json" \
     -d '{
           "topic": "مدیریت زمان برای دانشجویان مهندسی",
           "language": "fa"
         }'
  ```

*Example*: **Generate an English Report via cURL:**
  ```bash
  curl -X POST "http://127.0.0.1:8000/api/generate-report" \
     -H "Content-Type: application/json" \
     -d '{
           "topic": "Time management strategies for engineering students",
           "language": "en"
         }'
  ```

*Example*: **List All Reports via cURL:**
  ```bash
  curl -X GET "http://127.0.0.1:8000/api/reports"
  ```

*Example*: **Delete a Report via cURL:**
  ```bash
  curl -X DELETE "http://127.0.0.1:8000/api/reports/550e8400-e29b-41d4-a716-446655440000"
  ```

## 🔐 Environment Variables
The backend requires the following environment variables to be set in a `.env` file:

Variable | Description | Example
:--------|:------------|:--------
`OPENROUTER_API_KEY` | Your OpenRouter API key for LLM access | `sk-or-v1-...`
`LLM_MODEL` | The model ID to use for generation | `Your_Model_Name (eg. openai/gpt-oss-120b)`
`LLM_TIMEOUT` | Timeout in seconds for LLM requests | `60`
`MAX_INPUT_CHARS` | Maximum allowed length for user input | `2000`

## 📋 Request/Response Data Models

### GenerateReportRequest
The request body for generating a new report.
  ```json
  {
  "topic": "string (5-2000 characters)",
  "language": "string ('fa' or 'en', default: 'fa')"
  }
  ```

### GenerateReportResponse
The response returned after successfully generating a report.
  ```json
  {
  "final_report": "FinalReport object (see below)",
  "topic_en": "string (English translation of the topic)",
  "analysis_en": "object (raw English analysis JSON)",
  "report_id": "string (UUID of the saved report)"
  }
  ```

### FinalReport
The structured report object containing 12 sections.
  ```json
  {
  "project_title": "string",
  "executive_summary": "string",
  "problem_definition": "string",
  "assumptions_and_constraints": ["string"],
  "planning": "string (Markdown formatted)",
  "organizing": "string (Markdown formatted)",
  "leading": "string (Markdown formatted)",
  "controlling": "string (Markdown formatted)",
  "kpis": "string (Markdown formatted)",
  "risks": "string (Markdown formatted)",
  "final_recommendations": "string",
  "conclusion": "string"
  }
  ```

## 🎯 Pipeline Flow
When you call `/api/generate-report`, the backend executes the following pipeline:

1. **Input Validation**: Validate topic length and language parameter
2. **Translation (Persian → English)**: If input is Persian, translate to English using LLM
3. **Management Analysis**: Analyze the English topic using the 4 functions of management
4. **Output Formatting**:
  - If `language="fa"`: Translate the analysis back to Persian with proper formatting
  - If `language="en"`: Format the analysis directly in English with USD currency
5. **Database Storage**: Save the complete report to SQLite
6. **Response**: Return the final report with metadata

## 🎓 Academic Context
This project was developed as a university assignment for a **Management Principles** course. It demonstrates the practical application of AI in business analysis, combining classical management theory (Fayol's 4 functions) with modern software engineering practices (REST APIs, LLM integration, and bilingual NLP).

## 📄 License
This project is created for academic purposes.