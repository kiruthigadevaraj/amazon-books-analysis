# Amazon Books Analysis using Python & Pandas

## Project Description
This project analyzes the **best selling books on Amazon** using Python and Pandas.  
We take a dataset of Amazon books containing details like Title, Author, User Rating, Reviews, Price, Year, and Genre.  

Using this data, we perform **data analysis** and **visualization** to get insights such as:
- Top 10 most expensive books
- Average price per genre
- Top rated books
- Graphical representation of data

This project is perfect for **intermediate level Python learners**.

---

## Features
- Read and clean CSV dataset using Pandas
- Sort books by price and ratings
- Group data by genre and calculate average price
- Visualize insights using Matplotlib and Seaborn
- Provides a simple yet real-world **Data Analytics project experience**

---

## Code Overview
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV
df = pd.read_csv("amazon_books.csv")

# Top 10 expensive books
top_expensive = df.sort_values(by="Price", ascending=False).head(10)
print(top_expensive[["Title", "Price"]])

# Average price by Category
avg_price = df.groupby("Category")["Price"].mean()
print(avg_price)

# Visualization
plt.figure(figsize=(10,5))
sns.barplot(x=avg_price.index, y=avg_price.values)
plt.title("Average Book Price by Category")
plt.show()
