# Personal AI Health Solutions

A college-project prototype based on the accompanying presentation.

## Project idea

**Data → AI → Insight → Action**

The prototype accepts basic personal wellness data such as sleep, activity, resting heart rate, water intake, and a personal goal. It analyzes the entered values and produces simple personalized wellness insights and suggested actions.

## Features

- Simple Streamlit web interface
- Sleep, steps, resting heart rate, and hydration inputs
- Personal goal input
- Rule-based health/wellness analysis
- Personalized action suggestions
- Sample CSV data
- Clear non-diagnostic safety disclaimer

## Tech stack

- Python
- Streamlit
- Pandas
- NumPy

## Run the project

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Repository structure

```text
Personal-AI-Health-Solutions/
├── app.py
├── health_engine.py
├── sample_data.csv
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## Important note

This is an educational prototype. It does not diagnose, treat, or prevent medical conditions and should not replace professional medical care.
