# 🤖 AI Mock Interview Platform

An AI-powered mock interview platform built with **Python and Streamlit** that helps candidates practice technical interviews, receive AI-generated feedback, analyze resumes, track interview performance, and get personalized career advice.

The platform provides a complete interview preparation experience through AI-powered question generation, answer evaluation, follow-up questions, resume analysis, performance analytics, interview history, and downloadable PDF reports.

---

## 🚀 Live Demo

🔗 **Live Application:** (https://ai-mock-interview-platform-ksbw.onrender.com)

---

## 📌 Features

### 🎤 AI Mock Interviews
- AI-generated interview questions
- Multiple job roles
- Company-specific interview practice
- Easy, Medium, and Hard difficulty levels
- Customizable number of questions
- AI-powered answer evaluation
- AI-generated follow-up questions
- Voice-based answer input

### 📄 Resume Analyzer
- Upload resumes in PDF format
- Extract resume text automatically
- AI-powered resume analysis
- ATS compatibility score
- Resume strengths and weaknesses
- Skill analysis
- Improvement suggestions

### 📊 Performance Dashboard
- Total interviews completed
- Average interview score
- Highest score
- Interview performance tracking
- Score progression charts
- Role-based interview analytics
- Difficulty distribution analytics

### 📜 Interview History
- View previous interviews
- Review interview questions
- Review submitted answers
- View AI evaluations
- Track interview scores
- View interview dates and details

### 🤖 AI Career Coach
- Personalized career advice
- Performance-based recommendations
- Skill improvement suggestions
- Interview preparation guidance

### 📄 Professional PDF Reports
- Generate interview reports
- Include questions and answers
- Include AI evaluations
- Include scores
- Include follow-up questions
- Include career advice
- Download reports as PDF

### 🔐 Authentication
- User registration
- User login
- Secure password hashing
- CAPTCHA protection
- Session-based authentication

### 🎨 Premium UI
- Modern dark-themed interface
- Responsive dashboard
- Interactive performance charts
- Premium card-based design
- Clean navigation
- Mobile-friendly styling

---

## 🛠️ Tech Stack

### Frontend
- Streamlit
- HTML
- CSS
- Plotly

### Backend
- Python
- SQLite
- SQLAlchemy

### AI
- Google Gemini API
- Groq API

### Resume Processing
- PyPDF

### Voice Features
- Speech Recognition
- Streamlit Mic Recorder

### Authentication & Security
- bcrypt
- CAPTCHA
- python-dotenv

### PDF Generation
- ReportLab

### Deployment
- Render

### Version Control
- Git
- GitHub

---

## 🏗️ Project Structure

```text
AI Mock Interview Bot/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
│
├── database/
│   └── database.py
│
├── auth/
│   ├── login.py
│   ├── register.py
│   └── auth_service.py
│
├── dashboard/
│   └── dashboard.py
│
├── interview/
│   ├── interview_page.py
│   ├── interview_engine.py
│   └── evaluator.py
│
├── history/
│   ├── history_page.py
│   └── history_service.py
│
├── resume/
│   ├── upload.py
│   └── analysis.py
│
├── reports/
│   └── pdf_report.py
│
├── services/
│   ├── gemini_service.py
│   ├── career_coach.py
│   └── auth_service.py
│
├── utils/
│   ├── pdf_parser.py
│   └── score_parser.py
│
└── assets/
    └── ...