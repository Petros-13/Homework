import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('company_sales_data.csv')

months = df['month_number']

plt.figure(figsize=(8,5))
plt.plot(months, df['total_profit'], marker='o', linewidth=2)
plt.title('Company Profit Per Month')
plt.xlabel('Month')
plt.ylabel('Total Profit')
plt.xticks(months)
plt.grid(True)
plt.show()

plt.figure(figsize=(8,5))
plt.plot(months, df['facecream'], marker='o')
plt.plot(months, df['facewash'], marker='o')
plt.plot(months, df['toothpaste'], marker='o')
plt.plot(months, df['bathingsoap'], marker='o')
plt.plot(months, df['shampoo'], marker='o')
plt.plot(months, df['moisturizer'], marker='o')
plt.title('Sales Data of All Products Per Month')
plt.xlabel('Month')
plt.ylabel('Units Sold')
plt.xticks(months)
plt.legend(['Face Cream','Face Wash','Toothpaste','Bathing Soap','Shampoo','Moisturizer'])
plt.grid(True)
plt.show()

plt.figure(figsize=(8,5))
plt.bar(months - 0.2, df['facecream'], width=0.4)
plt.bar(months + 0.2, df['facewash'], width=0.4)
plt.title('Face Cream and Face Wash Sales Per Month')
plt.xlabel('Month')
plt.ylabel('Units Sold')
plt.xticks(months)
plt.legend(['Face Cream','Face Wash'])
plt.grid(True)
plt.show()
