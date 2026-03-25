import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("data_raw.csv")

df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

df['Geography'] = df['Geography'].str.replace('FRA', 'France')
df['Geography'] = df['Geography'].str.replace('French', 'France')

df['EstimatedSalary'] = df['EstimatedSalary'].str.replace('€', '')
df['Balance'] = df['Balance'].str.replace('€', '')

df['Age'] = df['Age'].astype(int)
df['Balance'] = df['Balance'].astype(float)
df['EstimatedSalary'] = df['EstimatedSalary'].astype(float)

df = df.drop(columns=['Tenure_y'])
df.rename(columns={'Tenure_x': 'Tenure'}, inplace=True)

df = pd.get_dummies(df, columns=['Geography', 'Gender'], drop_first=True)

df['Age_Binned'] = pd.cut(df['Age'], bins=4, labels=False)
df['Balance_Binned'] = pd.qcut(df['Balance'], q=4, labels=False, duplicates='drop')

numeric_cols = ['CreditScore', 'Age', 'Tenure', 'Balance', 'EstimatedSalary']
scaler = StandardScaler()
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

selected_cols = [
    'CreditScore',
    'Age',
    'Age_Binned',
    'Tenure',
    'Balance',
    'Balance_Binned',
    'EstimatedSalary',
    'Geography_Germany',
    'Geography_Spain',
    'Gender_Male'
]

df_final = df[selected_cols + ['Exited']]

df_final.to_csv("data_preprocessed.csv", index=False)