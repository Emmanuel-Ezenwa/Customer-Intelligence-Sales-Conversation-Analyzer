# 🚀 Emmanuel AI – Customer Intent & Sales Intelligence Engine

## Overview

Emmanuel AI is a machine learning-powered web application that analyses customer messages from WhatsApp conversations and predicts their **buying intent**.

The goal is simple:
- Help businesses prioritise serious buyers and improve conversion rates using data-driven insights.

---

## Problem Statement

In everyday sales conversations, especially in industries like tiles and building materials:

* Customers ask many questions
* Not all leads convert
* Time is wasted on low-intent buyers

Emmanuel AI solves this by automatically identifying:

* Who is serious
* Who is just inquiring
* Who is negotiating

---

## Features

* Intent Classification (Inquiry, Buying, Negotiation, Not Serious)
* Buyer Scoring System
* Real-time Message Analysis
* Deployed Web Application (accessible anywhere)

---

## How It Works

1. **Data Collection**

   * Real WhatsApp chat exports
   * Customer messages extracted and cleaned

2. **Data Processing**

   * Text cleaning (lowercasing, regex, stopword removal)
   * Noise filtering (removing seller responses)

3. **Model Training**

   * TF-IDF Vectorisation
   * Logistic Regression model (scikit-learn)

4. **Prediction**

   * Input message → cleaned → vectorized → classified

---

## Sample Output

| Message                    | Intent      | Score |
| -------------------------- | ----------- | ----- |
| How much is 60x120 tiles?  | Inquiry     | 40    |
| I want to order 50 cartons | Buying      | 90    |
| Can you reduce the price?  | Negotiation | 70    |

---

## Tech Stack

* Python
* Streamlit
* Scikit-learn
* Pandas
* Regex (Text Processing)

---

## Project Structure

```
├── app.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── README.md
```

---

## How to Run Locally

```bash
pip install -r requirements.txt
python -m streamlit run app.py
```

---

## Live Demo

(https://ai-sales-analyzer.streamlit.app/)

---

## Future Improvements

* Add prediction confidence scores
* Bulk message analysis
* Customer segmentation dashboard
* WhatsApp automation integration

---

## Business Use Case

This tool can be used by:

* Tile vendors
* Real estate marketers
* Sales teams

To:

* Prioritise high-value leads
* Improve response strategy
* Increase conversion rates

---

## Author

**Emmanuel Ezenwa**
Aspiring Data Scientist | Business Intelligence Analyst

GitHub: https://github.com/Emmanuel-Ezenwa

---

## Final Note

This project demonstrates the power of combining **real business data with machine learning** to create practical, revenue-impacting solutions.
