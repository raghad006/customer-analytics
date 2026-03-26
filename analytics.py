import pandas as pd

df = pd.read_csv("data_preprocessed.csv")

with open('insight1.txt', 'w') as f:

    f.write("INSIGHT 1: Customer Churn Analysis\n\n")
    churn_rate = df['Exited'].mean() * 100
    f.write(f"Overall Churn Rate: {churn_rate:.2f}%\n\n")
    
    if 'Gender_Male' in df.columns:
        male_churn = df[df['Gender_Male'] == 1]['Exited'].mean() * 100
        female_churn = df[df['Gender_Male'] == 0]['Exited'].mean() * 100
        f.write("Churn by Gender:\n")
        f.write(f" Male customers: {male_churn:.2f}%\n")
        f.write(f" Female customers: {female_churn:.2f}%\n\n")

    if 'Geography_Germany' in df.columns:
        germany_churn = df[df['Geography_Germany'] == 1]['Exited'].mean() * 100
        spain_churn = df[df['Geography_Spain'] == 1]['Exited'].mean() * 100
        france_churn = df[(df['Geography_Germany'] == 0) & (df['Geography_Spain'] == 0)]['Exited'].mean() * 100
        f.write("Churn by Geography:\n")
        f.write(f" Germany: {germany_churn:.2f}%\n")
        f.write(f" Spain: {spain_churn:.2f}%\n")
        f.write(f" France: {france_churn:.2f}%\n")

with open('insight2.txt', 'w') as f:
    f.write("INSIGHT 2: Credit Score Impact on Churn\n\n")
    churned_credit = df[df['Exited'] == 1]['CreditScore_orig'].mean()
    retained_credit = df[df['Exited'] == 0]['CreditScore_orig'].mean()
  
    f.write("Average Credit Score:\n")
    f.write(f" Churned customers: {churned_credit:.2f}\n")
    f.write(f" Retained customers: {retained_credit:.2f}\n\n")
    
    credit_diff = retained_credit - churned_credit
    f.write(f"Insight: Retained customers have {credit_diff:.2f} points higher credit scores on average\n")
    f.write("Conclusion: Higher credit scores correlate with lower churn risk\n")

with open('insight3.txt', 'w') as f:

    f.write("INSIGHT 3: Age and Balance Analysis\n")

    
    churned_age = df[df['Exited'] == 1]['Age_orig'].mean()
    retained_age = df[df['Exited'] == 0]['Age_orig'].mean()
    
    f.write("Age Analysis:\n")
    f.write(f" Churned customers avg age: {churned_age:.2f} years\n")
    f.write(f" Retained customers avg age: {retained_age:.2f} years\n\n")
    
    churned_balance = df[df['Exited'] == 1]['Balance_orig'].mean()
    retained_balance = df[df['Exited'] == 0]['Balance_orig'].mean()
    
    f.write("Balance Analysis:\n")
    f.write(f" Churned customers avg balance: €{churned_balance:.2f}\n")
    f.write(f" Retained customers avg balance: €{retained_balance:.2f}\n\n")
    
    if 'Age_Binned' in df.columns:
        f.write("Churn Rate by Age Group:\n")
        for age_group in sorted(df['Age_Binned'].unique()):
            group_churn = df[df['Age_Binned'] == age_group]['Exited'].mean() * 100
            f.write(f" Age Group {age_group + 1}: {group_churn:.2f}%\n")
    
    f.write("\nKey Finding: Older customers and those with higher balances show different churn patterns\n")

print("Generated insight1.txt, insight2.txt, insight3.txt")