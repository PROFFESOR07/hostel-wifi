#  Predicting Hostel Wi-Fi Load Using Student Internet Usage Patterns

##  Overview
In college hostels, Wi-Fi performance often degrades due to **simultaneous student usage**, especially during peak hours. Rather than predicting raw internet speed (which is unavailable in most real datasets), this project focuses on **modeling Wi-Fi load as a proxy for congestion** using student internet usage behavior.

The project is inspired by research on *understanding internet usage patterns among college students* and applies an interpretable machine learning approach to identify **when Wi-Fi is likely to feel slow or stable**.

---

##  Objective
- Analyze session-level internet usage data
- Understand **temporal usage behavior** of students
- Build a **regression model** to predict Wi-Fi load
- Provide **context-aware predictions** using user input
- Identify **best and worst hours** for high-bandwidth usage

---

##  Dataset
The dataset consists of **4,712 internet sessions**, where each row represents a single user session.

### Key Fields Used
- `start_time` — Session start timestamp  
- `usage_time` — Session duration (`DD:HH:MM:SS` format)  
- `total_transfer` — Total data transferred (KB)  
- `seession_break_reason` — Session termination reason  

---

##  Feature Engineering

### Engineered Features
- **Hour of Day (`hour`)**  
  Captures time-dependent usage patterns.

- **Session Duration (`duration_min`)**  
  Parsed using a custom parser to handle non-standard time formats.  
  
- **Wi-Fi Load (Target)**:  
Wi-Fi Load = Total Data Transferred / Session Duration
This represents data consumption intensity and serves as a proxy for congestion.

---

##  Model
A **Linear Regression** model was used to maintain interpretability and avoid over-engineering. The goal was to understand **patterns and trends**, not to maximize predictive accuracy.

---
##  User Input-Based Prediction System

In addition to aggregate analysis, the project includes an **interactive prediction mode** where a user can input:

- Hour of day (0–23)
- Expected session duration (minutes)

The trained model predicts the **expected Wi-Fi load** for that session.

---
##  Percentile-Based Comparison-INSPIRED BY STUDY OR SLEEP TASK

Instead of comparing user predictions against the **mean**, the system uses the **75th percentile of historical Wi-Fi load for that hour**.

### Why Percentiles?
- Early-morning hours contain many **idle sessions**
- Mean values are heavily skewed downward
- Percentiles provide **fair, human-aligned comparisons**

### Interpretation Logic
- If predicted load ≤ 75th percentile → ✅ Lighter than most sessions
- If predicted load > 75th percentile → ⚠️ Heavier than most sessions
---


##  Results
MAE : 3433.86
RMSE : 6367.25


- Wi-Fi congestion is highest during **evening and late-night hours**
- **Early morning (4–6 AM)** shows the lowest load and is best for downloads or streaming

---
## 📁 Project Structure
```text
hostel-wifi-prediction/
├── data/
│ └── Internetusage_Beginnertask03.csv
├── notebooks/
│ └── eda.ipynb
├── src/
│ ├── init.py
│ ├── data_loader.py
│ ├── feature_engineering.py
│ ├── eda.py
│ ├── model.py
│ ├── train.py
│ ├── evaluate.py
│ └── visualize.py
├── outputs/
│ └── figures/
├── main.py
├── requirements.txt
└── README.md
```

### File & Folder Descriptions

- **data/** — Contains the raw internet usage dataset  
- **notebooks/** — Exploratory data analysis and initial insights  
- **src/** — Core source code for data processing, modeling, and visualization  
- **outputs/** — Generated plots and figures  
- **main.py** — Entry point that runs the full pipeline  
- **requirements.txt** — Project dependencies  
- **README.md** — Project documentation and overview


---
##  Key Insight
> *Off-peak hours have low average congestion, but active sessions may still exceed typical usage because most users are idle.*

This distinction between **global trends** and **individual behavior** is a core contribution of the project.

---

##  Limitations
- Actual internet speed (Mbps) was not available
- Results model relative congestion, not exact speed
- External network factors are not included

---

##  Conclusion
This project demonstrates how realistic assumptions and thoughtful feature engineering can provide **actionable insights** into Wi-Fi congestion without relying on complex models.

---

##  Author
**Pranjal Choudhary**  

