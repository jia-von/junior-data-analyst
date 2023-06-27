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


