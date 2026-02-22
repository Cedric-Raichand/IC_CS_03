# Phishing Detection System

**Built by Cedrick Dzodzodzi – Intern at Interncred Cybersecurity Internship**

## Overview

This project implements a **Phishing Detection System** that helps users identify phishing websites or emails to prevent compromise. The system combines **rule-based heuristics** and **machine learning models** for accurate detection, along with a clean **user interface** for easy interaction.

---

## Features

1. **Rule-Based Detection**
   - Checks URL patterns such as length, `@` symbol, hyphenated domains, multiple subdomains.
   - Verifies HTTPS encryption presence.
   - Detects common phishing keywords (login, verify, account, secure, etc.).

2. **Machine Learning Detection**
   - Extracts features from URLs (domain age, SSL info, WHOIS data, and more).
   - Trains a classifier (Random Forest / SVM) on phishing datasets.
   - Predicts if a URL is safe or phishing.

3. **User Interface**
   - Web-based interface built with Flask.
   - User inputs a URL and receives a **risk assessment**, rule-based result, and ML prediction.
   - Displays risk score and reasons for suspicion.

---

## Tech Stack

- **Programming Language:** Python  
- **Framework:** Flask  
- **Libraries:** scikit-learn, pandas, numpy, joblib, requests  
- **Dataset:** Phishing URL features from UCI ML repository / PhishTank API  


