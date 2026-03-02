sns.set(style="whitegrid")

plt.figure(figsize=(8,5))
sns.boxplot(data=df)
plt.xticks(rotation=45)
plt.show()

for col in df.select_dtypes(include=np.number).columns:
    sns.kdeplot(df[col], fill=True)

plt.legend(df.select_dtypes(include=np.number).columns)
plt.show()

sns.jointplot(x=df.select_dtypes(include=np.number).columns[0],
              y=df.select_dtypes(include=np.number).columns[1],
              data=df,
              kind="reg")
plt.show()

if len(df.select_dtypes(include="object").columns) > 0:
    cat = df.select_dtypes(include="object").columns[0]
    num = df.select_dtypes(include=np.number).columns[0]
    sns.violinplot(x=cat, y=num, data=df)
    plt.xticks(rotation=45)
    plt.show()

    sns.countplot(x=cat, data=df)
    plt.xticks(rotation=45)
    plt.show()