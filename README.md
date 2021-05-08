# shopify-data-intern-challenge-fall2021
## Question 1
Analysis for question 1 is performed [here](./q1.py)

a) Upon analyzing the dataset, we find that the "naive" calculation for the AOV is just the mean order_amount. We know that this mean is not a good representation of the data, because the standard deviation is at an absurdly high value of $41282.54.

Because the mean is so much higher than we might expect, we can expect to find a few outliers that each have an extremely high order_amount. These outliers are not representative of the rest of the data.

We find two "kinds" of outlliers:
  1. At shop with shop_id of 42, a customer with user_id 607 regularly makes a $704000 purchase of 2000 items. Customer 607 is likely a business rather than an individual, making bulk purchases in order to resell.
  2. At shop with shop_id 78, they sell single item that costs $25725. Because of this, we find regular orders from store 78 with order amounts that are multiples of $25725 (154350, 102900, 77175, 51450, 25725). Because this sneaker costs so much more than a typical sneaker, orders from this store do not accurately represent the 
  
One way to better evaluate the data would be to remove the outliers. Any value that is less than ```Q1 - 1.5*Interquartile Range(IQR)``` or greater than ```Q3 + 1.5*IQR``` is excluded.

b) With the outliers removed, a good metric to report would be the new mean.

Alternatively, the median of either the original dataset, or this new outlier-removed-dataset could be good metrics: the median is not heavily impacted by outliers, so removing outliers isn't especially important.

c) The mean order_amount of the dataset with outliers removed is $293.72, which is much more in line with what we may expect from a sneaker store. We know this mean is much more representative of the data, because the standard deviation now is only $144.45.


## Question 2
### a)
#### Answer
54 orders were shipped by Speedy Express in total.

#### Query
```sql
SELECT * FROM [Orders]
WHERE ShipperID == (
  SELECT ShipperID FROM [Shippers]
  where ShipperName = "Speedy Express"
)
```

### b)
#### Answer
Peacock is the last name of the employee with the most orders.

#### Query
```sql
SELECT LastName FROM [Employees]
WHERE EmployeeID == (
  SELECT EmployeeID
  FROM [Orders]
  GROUP BY EmployeeID
  ORDER BY COUNT(*) Desc
  LIMIT 1
)
```

### c)

I found that this question was amiguously worded, and could have two interpretations:
1. Find the product in Germany that was included in the most orders
2. Find the product in Germany that had the highest quantity of items ordered.

For instance, if a product was only ordered once in Germany, but this single order contianed 100000 of the product, it may be the answer for #2, but not #1

I answered this question for both interpretations

### Interpretation 1
#### Answer
Gorgonzola Telino is the product ordered the most by customers in Germany.
#### Query
```sql
SELECT ProductName FROM [Products]
WHERE ProductID == (
  SELECT ProductID FROM [OrderDetails]
  WHERE OrderID in (
    SELECT OrderID FROM [Orders]
    WHERE CustomerID IN (
      SELECT CustomerID FROM Customers
      WHERE Country == "Germany"
    )
  )
  GROUP BY ProductID
  ORDER BY COUNT(*) DESC
  LIMIT 1
)
```

### Interpretation 2
#### Answer
Boston Crab Meat is the product ordered the most by customers in Germany.
#### Query
```sql
SELECT ProductName FROM [Products]
WHERE ProductID == (
  SELECT ProductID FROM [OrderDetails]
  WHERE OrderID in (
    SELECT OrderID FROM [Orders]
    WHERE CustomerID IN (
      SELECT CustomerID FROM Customers
      WHERE Country == "Germany"
    )
  )
  GROUP BY ProductID
  ORDER BY SUM(Quantity) Desc
  LIMIT 1
)
```

