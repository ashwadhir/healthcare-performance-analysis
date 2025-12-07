import matplotlib.pyplot as plt
import pandas as pd

# Analyst Email for Verification: 22f2000771@ds.study.iitm.ac.in

# 1. Dataset Preparation
data = {
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
    'Score': [3.4, 5.8, 3.01, 9.67]
}
df = pd.DataFrame(data)

# 2. Analysis
average_score = df['Score'].mean()
target = 4.5

print(f"Calculated Average: {average_score}") # Output: 5.47

# 3. Visualization
plt.figure(figsize=(10, 6))
plt.plot(df['Quarter'], df['Score'], marker='o', label='Patient Satisfaction', linewidth=2, color='blue')
plt.axhline(y=target, color='r', linestyle='--', label=f'Industry Target ({target})')
plt.axhline(y=average_score, color='g', linestyle=':', label=f'Current Avg ({average_score:.2f})')

plt.title('2024 Quarterly Patient Satisfaction Trends')
plt.ylabel('Satisfaction Score')
plt.legend()
plt.grid(True)

# Save plot for the report
plt.savefig('trend_analysis.png')
print("Analysis complete. Plot saved.")
