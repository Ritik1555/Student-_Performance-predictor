import pandas as pd
import numpy as np

np.random.seed(42)

n = 1000

gender = np.random.choice(['Male', 'Female'], n)

study_hours = np.random.randint(1, 11, n)

previous_scores = np.random.randint(40, 101, n)

participation = np.random.choice(
    ['Low', 'Medium', 'High'],
    n,
    p=[0.3, 0.4, 0.3]
)

performance = []

for i in range(n):
    score = (
        study_hours[i] * 5
        + previous_scores[i] * 0.7
        + (participation[i] == 'High') * 15
        + (participation[i] == 'Medium') * 8
    )

    if score >= 70:
        performance.append('Pass')
    else:
        performance.append('Fail')

df = pd.DataFrame({
    'StudentID': range(1, n + 1),
    'Gender': gender,
    'StudyHours': study_hours,
    'PreviousScores': previous_scores,
    'Participation': participation,
    'Performance': performance
})

df.to_csv('student_data.csv', index=False)

print("Dataset created successfully!")
print(df.head())