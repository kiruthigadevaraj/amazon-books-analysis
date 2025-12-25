import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

df=pd.read_csv("amazon_books.csv")

print("first 5 books:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

top_expensive=df.sort_values(by='Price',ascending=False).head(10)
print("\nTop 10 Expensive Books:")
print(top_expensive[['Title','Price']])

top_rated=df.sort_values(by='Rating',ascending=False).head(10)
print("\nTop 10 Expensive Books:")
print(top_rated [['Title','Rating']])

avg_price_cat=df.groupby('Category')['Price'].mean().sort_values(ascending=False)
print("\nAverage Price per category:")
print(avg_price_cat)

plt.figure(figsize=(10,6))
sns.barplot(x='Price',y='Title',data=top_expensive)
plt.title("Top 10 most expensive Amazon Books")
plt.show()

plt.figure(figsize=(10,6))
sns.countplot(y='Category',data=df,order=df['category'].value_counts().index)
plt.title()
plt.show()