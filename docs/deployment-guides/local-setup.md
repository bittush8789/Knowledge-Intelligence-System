# Local Setup Guide

Follow these steps to run the Knowledge Intelligence System on your local machine.

## 1. Prerequisites
- Python 3.11+
- Git

## 2. Clone the Repository
```bash
git clone https://github.com/bittush8789/Knowledge-Intelligence-System.git
cd Knowledge-Intelligence-System
```

## 3. Create a Virtual Environment
```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

## 4. Install Dependencies
```bash
pip install -r requirements.txt
```

## 5. Configure Environment Variables
Create a `.env` file in the root folder:
```env
OPENAI_API_KEY=your_key
AWS_ACCESS_KEY=your_key
AWS_SECRET_KEY=your_secret
```

## 7. Run the Frontend
Since the frontend is now pure **HTML/CSS/JS**, you can just open `frontend/index.html` in your browser. 
Or, use a simple local server:
```bash
cd frontend
npx serve .
```
Aapka frontend ab `http://localhost:3000` (agar serve use kiya) par chal raha hoga.
