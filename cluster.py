import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv("data_preprocessed.csv")

cluster_features_scaled = ['CreditScore', 'Age', 'Tenure', 'Balance', 'EstimatedSalary']

kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(df[cluster_features_scaled])

cluster_counts = df['Cluster'].value_counts().sort_index()

cluster_features_orig = ['CreditScore_orig', 'Age_orig', 'Tenure_orig', 'Balance_orig', 'EstimatedSalary_orig']

with open('clusters.txt', 'w') as f:
    f.write("\nK-MEANS CLUSTERING RESULTS\n\n")
    f.write("Clustering Configuration:\n")
    f.write(f"  - Number of clusters: 4\n")
    f.write(f"  - Features used: {', '.join(cluster_features_scaled)}\n")
    f.write(f"  - Total samples: {len(df)}\n\n")

    f.write("SAMPLES PER CLUSTER\n\n")
    for cluster in sorted(cluster_counts.index):
        f.write(f"Cluster {cluster}: {cluster_counts[cluster]} customers "
                f"({cluster_counts[cluster]/len(df)*100:.1f}%)\n")

    f.write("\nCLUSTER CHARACTERISTICS:\n")
    for cluster in sorted(df['Cluster'].unique()):
        cluster_data = df[df['Cluster'] == cluster]

        f.write(f"\nCluster {cluster}:\n")
        f.write(f"Size: {len(cluster_data)} customers\n")

        for i, feature in enumerate(cluster_features_orig):
            original_feature_name = feature.replace('_orig', '')
            avg = cluster_data[feature].mean()
            f.write(f"Average {original_feature_name}: {avg:.2f}\n")

        churn_rate = cluster_data['Exited'].mean() * 100
        f.write(f"Churn Rate: {churn_rate:.1f}%\n")

        if cluster_data['Exited'].mean() > df['Exited'].mean():
            f.write("High-risk cluster (above average churn)\n")
        else:
            f.write("Low-risk cluster (below average churn)\n")

print("Results saved to clusters.txt")