import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel("C:\\Users\\Admin\\OneDrive\\Documents\\TASK 4.xlsx",sheet_name="Dataset")

print(df)

df["TotalAmount"]=(df["Items"]*df["ItemPrice"])+df["DeliveryFee"]
print("\nTotalAmount\n:",df["TotalAmount"].sum())

Revenue_by_Restaurant=df.groupby("Restaurant")["TotalAmount"].sum().sort_values(ascending=False)
print("\nRevenue_by_Restaurant\n:",Revenue_by_Restaurant)

Revenue_by_City=df.groupby("City")["TotalAmount"].sum().sort_values(ascending=False)
print("\nRevenue_by_City\n:",Revenue_by_City)

Orders_count_by_category=df.groupby("Category")["Items"].sum().sort_values(ascending=False)
print("\nOrders_count_by_category\n:",Orders_count_by_category)

df.groupby("Restaurant")["TotalAmount"].sum().plot(kind="bar")
plt.title("Total_Amount_by_Restaurant")
plt.show()


df.groupby("City")["TotalAmount"].sum().plot(kind="bar")
plt.title("Total_Amount_by_City")
plt.show()

df.groupby("Category")["TotalAmount"].sum().plot(kind="pie")
plt.title("Total_Amount_by_Category")
plt.show()
