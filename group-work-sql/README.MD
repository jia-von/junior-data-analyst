# SQL Basics Activity
This excercise are done using [DB Browser for SQLite ](https://sqlitebrowser.org/dl/)

## Review the Book table and answer the following questions accordingly:
### Create database and import data using SQL:
```SQL
-- Use this sql script to create table and import data--

BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Book" (
	"BookISBN"	INTEGER,
	"Status"	TEXT,
	"Category"	TEXT,
	"PurchaseCost"	NUMERIC
);
INSERT INTO "Book" VALUES (978033195055014,'Out','Crime',25.99);
INSERT INTO "Book" VALUES (97814002096298021,'Out','Medical',12.99);
INSERT INTO "Book" VALUES (978055381762015,'In','Travel',14);
INSERT INTO "Book" VALUES (978066295055012,'Out','Cookery',18.99);
INSERT INTO "Book" VALUES (978112895055013,'Out','Crime',11.99);
INSERT INTO "Book" VALUES (978041996298023,'Out','Architecture',35);
INSERT INTO "Book" VALUES (97814002081762016,'In','Travel',17);
INSERT INTO "Book" VALUES (978051896298012,'Out','Travel',9.99);
INSERT INTO "Book" VALUES (978044796298026,'Out','Gardening',12.5);
INSERT INTO "Book" VALUES (978039481762021,'In','Cookery',17.5);
INSERT INTO "Book" VALUES (978111995055024,'In','Gardening',13.50);
INSERT INTO "Book" VALUES (978026181762012,'Out','Astronomy',24.50);
COMMIT;
```

### What is the output of this query?
```SQL
Select * from Book where PurchaseCost >12;
```
#### Output
| BookISBN          | Status | Category     | PurchaseCost |
|-------------------|--------|--------------|--------------|
| 978033195055014   | Out    | Crime        | 25.99        |
| 97814002096298021 | Out    | Medical      | 12.99        |
| 978055381762015   | In     | Travel       | 14           |
| 978066295055012   | Out    | Cookery      | 18.99        |
| 978041996298023   | Out    | Architecture | 35           |
| 97814002081762016 | In     | Travel       | 17           |
| 978044796298026   | Out    | Gardening    | 12.5         |
| 978039481762021   | In     | Cookery      | 17.5         |
| 978111995055024   | In     | Gardening    | 13.5         |
| 978026181762012   | Out    | Astronomy    | 24.5         |

### What is the output of this query?
```SQL
Select DISTINCT Category from Book;
```

#### Output
| Category     |
|--------------|
| Crime        |
| Medical      |
| Travel       |
| Cookery      |
| Architecture |
| Gardening    |
| Astronomy    |

### Write a SQL query to retrieve all the data from Book where Status equals “out”.
```SQL
SELECT * FROM Book WHERE Status = 'Out';
```

#### Output
| BookISBN          | Status | Category     | PurchaseCost |
|-------------------|--------|--------------|--------------|
| 978033195055014   | Out    | Crime        | 25.99        |
| 97814002096298021 | Out    | Medical      | 12.99        |
| 978066295055012   | Out    | Cookery      | 18.99        |
| 978112895055013   | Out    | Crime        | 11.99        |
| 978041996298023   | Out    | Architecture | 35           |
| 978051896298012   | Out    | Travel       | 9.99         |
| 978044796298026   | Out    | Gardening    | 12.5         |
| 978026181762012   | Out    | Astronomy    | 24.5         |

### Write SQL statement to retrieve only the first 3 rows from book.
```SQL
SELECT * FROM Book LIMIT 3;
```

#### Output
| BookISBN          | Status | Category | PurchaseCost |
|-------------------|--------|----------|--------------|
| 978033195055014   | Out    | Crime    | 25.99        |
| 97814002096298021 | Out    | Medical  | 12.99        |
| 978055381762015   | In     | Travel   | 14           |


### Write a SQL statement to count all books where the Category equals Travel.
```SQL
SELECT COUNT(*) FROM Book WHERE Category = "Travel";
```

#### Output
| COUNT |
|-------|
| 3     |

### Write SQL statements to delete the books with ISBN of “978111995055024, 978026181762012”
```SQL
DELETE FROM Book WHERE BookISBN in (978111995055024,978026181762012);
```

#### Output 
| BookISBN          | Status | Category     | PurchaseCost |
|-------------------|--------|--------------|--------------|
| 978033195055014   | Out    | Crime        | 25.99        |
| 97814002096298021 | Out    | Medical      | 12.99        |
| 978055381762015   | In     | Travel       | 14           |
| 978066295055012   | Out    | Cookery      | 18.99        |
| 978112895055013   | Out    | Crime        | 11.99        |
| 978041996298023   | Out    | Architecture | 35           |
| 97814002081762016 | In     | Travel       | 17           |
| 978051896298012   | Out    | Travel       | 9.99         |
| 978044796298026   | Out    | Gardening    | 12.5         |
| 978039481762021   | In     | Cookery      | 17.5         |



