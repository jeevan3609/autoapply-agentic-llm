# 📌 AutoApply: Agentic Generative AI Pipeline for Tailored Job Applications  
Final Project — Practical Data Science (Fall 2025)  
Author: **Jeevan Hemanth Yendluri**

---

## ✔️ Overview

This project implements a **multi-agent Generative AI pipeline** that analyzes a job description and a resume, identifies strengths and gaps, and then generates tailored application materials.

The system is built with **four cooperating LLM agents** connected through a clean orchestration pipeline.

All model inference uses **Groq’s free Llama-3.1 model**, which provides high-quality, real-time responses with no payment required.

---

## ✔️ Agent Pipeline

The pipeline consists of **4 modular agents**, each handling a specific reasoning task:

### **1. Job Description Parser Agent**
Extracts:
- role title  
- responsibilities  
- required skills  
- preferred skills  

### **2. Resume Analyzer Agent**
Compares resume vs. JD and returns:
- strengths  
- gaps  
- fit rating  
- relevant experience context  

### **3. Gap Recommender Agent**
Suggests:
- what to emphasize now  
- what to improve in the future (skills, tools, courses, etc.)  

### **4. Application Materials Generator Agent**
Creates:
- tailored resume bullet points  
- outreach email draft  
- role-specific messaging  

All agents use:

```python
from src.llm_client import call_llm

Project Structure
autoapply-agentic-llm/
│
├─ data/
│   ├─ sample_resume.txt
│   └─ sample_job_description.txt
│
├─ src/
│   ├─ main.py
│   ├─ llm_client.py
│   └─ agents/
│       ├─ jd_parser.py
│       ├─ resume_analyzer.py
│       ├─ gap_recommender.py
│       └─ application_generator.py
│
└─ README.md

✔️ LLM Setup (Groq API)

This project uses a free cloud LLM through Groq:

Provider: Groq

Model: llama-3.1-8b-instant

API style: OpenAI-compatible /chat/completions

Implementation: src/llm_client.py

Before running, set your Groq API key:

set GROQ_API_KEY=your_key_here


llm_client.py includes:

DUMMY_MODE = False


True → No external calls, preview/testing mode

False → Real inference using Groq Llama-3.1

The rest of the system stays unchanged when switching models.
The architecture is model-agnostic.

✔️ How to Run the Full Pipeline
1. Install dependencies:
pip install requests

2. Set your API key:
set GROQ_API_KEY=your_key_here

3. Run the pipeline:
python -m src.main --resume data/sample_resume.txt --job data/sample_job_description.txt


You will see 4 steps:

STEP 1: JD Parser

STEP 2: Resume Analyzer

STEP 3: Recommendations

STEP 4: Application Materials

Each step prints the output from one agent.

✔️ Example Outputs (Generated from Groq Llama-3.1)
Example JD Parser Output:
Data Analyst Intern
Responsibilities: cleaning data, analysis, dashboards
Required Skills: SQL, Python, Tableau, Power BI
Nice-to-Have: ML basics, statistics

Example Resume Analyzer Output:

Strengths identified

Gaps listed

Fit score

Matching experiences

Example Generated Resume Bullets:

Data Cleaning

Dashboard Creation

ML/Statistics Integration

Technical Skills Reinforcement

Example Outreach Email:

A fully generated professional email tailored to the job role.

✔️ Final Submission Components

This repository includes:

✔️ README.md

✔️ Full working agentic pipeline (4 agents + orchestrator)

✔️ 2-minute video demo (to be added in repo)

✔️ LaTeX poster / small paper PDF (Overleaf template used)

✔️ Real outputs generated from Groq’s Llama-3.1 model

✔️ Explanation of design, architecture, results, limitations, and future extensions

✔️ Future Enhancements

Integration with vector search (RAG)

Auto-apply workflows for job portals

Resume rewriting agent

UI front-end for end-users

Switching to larger Llama/GPT models when available