import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("data_preprocessed.csv")

age_col = 'Age_orig' if 'Age_orig' in df.columns else 'Age'
balance_col = 'Balance_orig' if 'Balance_orig' in df.columns else 'Balance'
credit_col = 'CreditScore_orig' if 'CreditScore_orig' in df.columns else 'CreditScore'

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

ax1 = axes[0, 0]
churn_counts = df['Exited'].value_counts()
colors = ['lightblue', 'lightcoral']
labels = ['Retained (0)', 'Churned (1)']
ax1.pie(churn_counts, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
ax1.set_title('Customer Churn Distribution', fontsize=14, fontweight='bold')

ax2 = axes[0, 1]
churned_scores = df[df['Exited']==1][credit_col]
retained_scores = df[df['Exited']==0][credit_col]
ax2.hist(retained_scores, bins=30, alpha=0.5, label='Retained', color='green')
ax2.hist(churned_scores, bins=30, alpha=0.5, label='Churned', color='red')
ax2.set_title('Credit Score Distribution by Churn', fontsize=14, fontweight='bold')
ax2.set_xlabel('Credit Score')
ax2.set_ylabel('Frequency')
ax2.legend()

ax3 = axes[1, 0]
corr_cols = [credit_col, age_col, 'Tenure', balance_col, 'EstimatedSalary', 'Exited']
if 'Age_Binned' in df.columns:
    corr_cols.append('Age_Binned')
if 'Balance_Binned' in df.columns:
    corr_cols.append('Balance_Binned')
corr_matrix = df[corr_cols].corr()
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', center=0, ax=ax3)
ax3.set_title('Feature Correlation Heatmap', fontsize=14, fontweight='bold')

ax4 = axes[1, 1]
scatter = ax4.scatter(df[age_col], df[balance_col], c=df['Exited'], cmap='coolwarm', alpha=0.6, s=50)
ax4.set_title('Age vs Balance (Colored by Churn)', fontsize=14, fontweight='bold')
ax4.set_xlabel('Age (Years)')
ax4.set_ylabel('Balance (€)')
cbar = plt.colorbar(scatter, ax=ax4)
cbar.set_label('Churn (0=No, 1=Yes)')

plt.tight_layout()
plt.savefig('summary_plot.png', dpi=300, bbox_inches='tight')
plt.show()

print("Saved as summary_plot.png")