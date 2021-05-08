import numpy as np
import pandas as pd

data = pd.read_csv("2019 Winter Data Science Intern Challenge Data Set - Sheet1.csv")
print(data.order_amount.describe(),"\n")

order_amount_frequency = data.groupby(['order_amount']).size().reset_index(name='count').sort_values(by='order_amount', ascending=False).head(7)
print(order_amount_frequency,"\n")

q1 = data.order_amount.quantile(q=0.25)
q3 = data.order_amount.quantile(q=0.75)
IQR = q3 - q1

outliers_removed = data[(data.order_amount <= q3 + IQR * 1.5) & (data.order_amount >= q1 - IQR * 1.5)]

print(outliers_removed.order_amount.describe())