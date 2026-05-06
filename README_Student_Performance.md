🚀 Student Performance Analysis — Academic Insights from Simulated Data

📌 Summary

End-to-end exploratory data analysis on student performance metrics to uncover academic trends, attendance impacts, and study habits. Built in a reproducible notebook with clean structure and dependencies.

🎯 Objectives

*   Generate random student dataset using NumPy
*   Calculate grades, totals, and pass/fail status
*   Compute statistical class summaries
*   Visualize grade distribution and correlations

📊 Dataset

*   **File:** `data/student_performance_processed.csv` (self-generated)
*   **Typical fields:** `Name`, `Subject Marks`, `Attendance (%)`, `Study Hours`
*   **Size:** 50 simulated student records

🧠 Approach

*   Data generation (NumPy random distributions)
*   Data processing & grading logic (Pandas)
*   Statistical calculations (mean, median, standard deviation)
*   Visualization (bar, pie, histogram, scatter, heatmap)

📈 Key Insights (example)

*   **Study hours** show a positive correlation with average marks
*   **High attendance** helps avoid extreme failing grades
*   **Subject averages** identify areas requiring more teaching focus

🖼️ Visuals

Add your screenshots to `outputs/` and reference here
*   Grade distribution pie chart
*   Study hours vs average marks scatter plot

🗂️ Project Structure

```text
student-performance-analysis/
├── data/
│   └── student_performance_processed.csv
├── notebooks/
│   └── analysis.ipynb
├── outputs/
│   └── student_dashboard.png
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

▶️ Run Locally

```bash
git clone https://github.com/Litla8/student-performance-analysis.git
cd student-performance-analysis
pip install -r requirements.txt
jupyter notebook notebooks/analysis.ipynb
https://www.kaggle.com/code/lalitraos/student-performance-analysis-system
```

🧪 Reproducibility

*   Python 3.9+
*   NumPy seed fixed (`np.random.seed(42)`) for deterministic generation

🛠️ Tech Stack

*   Python (Pandas, NumPy)
*   Matplotlib / Seaborn
*   Jupyter Notebook

🚀 Extensions (next steps)

*   Machine learning prediction of student grades
*   Deploy interactive dashboard (Streamlit)

👤 Author

Lalit Rao — [https://github.com/Litla8](https://github.com/Litla8)

📜 Certificate

[View Certificate](https://github.com/Litla8/student-performance-analysis/blob/main/certificates/student-performance-certificate.pdf)
