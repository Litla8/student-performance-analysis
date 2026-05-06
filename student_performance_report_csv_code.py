import numpy as np
import pandas as pd

np.random.seed(42)
num_students = 50
names = [f"Student_{i}" for i in range(1, num_students + 1)]
subjects = ['Math', 'Physics', 'Chemistry', 'English', 'Biology']
marks = np.random.randint(35, 100, size=(num_students, len(subjects)))
attendance = np.random.uniform(50, 100, size=num_students).round(2)
study_hours = np.random.uniform(1, 8, size=num_students).round(1)

df = pd.DataFrame(marks, columns=subjects)
df.insert(0, 'Name', names)
df['Attendance_%'] = attendance
df['Study_Hours'] = study_hours
df['Total_Marks'] = df[subjects].sum(axis=1)
df['Average_Marks'] = df[subjects].mean(axis=1).round(2)

def assign_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'

df['Grade'] = df['Average_Marks'].apply(assign_grade)
df['Status'] = np.where(df['Average_Marks'] >= 40, 'Pass', 'Fail')
class_stats = df[subjects].agg(['mean', 'median', 'std']).round(2)
grade_breakdown = df['Grade'].value_counts().sort_index()
top_5_students = df.nlargest(5, 'Total_Marks')[['Name', 'Total_Marks', 'Average_Marks', 'Grade']]

report_content = f"""STUDENT PERFORMANCE ANALYSIS - SUMMARY REPORT
=================================================================================

1. CLASS STATISTICS (SUBJECT-WISE)
----------------------------------
{class_stats.to_string()}

2. GRADE BREAKDOWN
------------------
{grade_breakdown.to_string(name=False)}

3. TOP 5 PERFORMING STUDENTS
----------------------------
{top_5_students.to_string(index=False)}

=================================================================================
Report automatically generated from NumPy/Pandas analysis.
"""

with open('student_performance_report.txt', 'w') as f:
    f.write(report_content)

df.sort_values(by='Total_Marks', ascending=False, inplace=True)
df.to_csv('student_performance_processed.csv', index=False)
