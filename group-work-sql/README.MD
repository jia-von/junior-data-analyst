# SQL Basics Activity
- This excercise are done using [DB Browser for SQLite ](https://sqlitebrowser.org)
- Thanks to [TableConvert](https://tableconvert.com/sql-to-markdown) turning my SQL statements into markdown table!

## Review the Book table and answer the following questions accordingly:
### Create database and import data using SQL:
```SQL
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
| ----------------- | ------ | ------------ | ------------ |
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
| ------------ |
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
| ----------------- | ------ | ------------ | ------------ |
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
| ----------------- | ------ | -------- | ------------ |
| 978033195055014   | Out    | Crime    | 25.99        |
| 97814002096298021 | Out    | Medical  | 12.99        |
| 978055381762015   | In     | Travel   | 14           |


### Write a SQL statement to count all books where the Category equals Travel.
```SQL
SELECT COUNT(*) FROM Book WHERE Category = "Travel";
```

#### Output
| COUNT |
| ----- |
| 3     |

### Write SQL statements to delete the books with ISBN of “978111995055024, 978026181762012”
```SQL
DELETE FROM Book WHERE BookISBN in (978111995055024,978026181762012);
```

#### Output 
| BookISBN          | Status | Category     | PurchaseCost |
| ----------------- | ------ | ------------ | ------------ |
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

## Practicing with Movies using Where Clause
Firstly to create two tables: `movie_reviewer` and `movies`

### Create movie_reviewer table
Set the `mov_id` as foreign key. After creating table, import the files as `.csv`
```SQL
CREATE TABLE "movie_reviewer" (
	"mov_id"	INTEGER,
	"rev_name"	TEXT,
	"rev_id"	INTEGER,
	"rev_stars"	TEXT,
	"num_o_ratings"	TEXT,
	FOREIGN KEY("mov_id") REFERENCES "movies"("mov_id")
)
```
#### Output
| mov_id | rev_name           | rev_id | rev_stars | num_o_ratings |
| ------ | ------------------ | ------ | --------- | ------------- |
| 901    | Righty Sock        | 9001   | 8.4       | 263575        |
| 902    | Jack Malvern       | 9002   | 7.9       | 20207         |
| 903    | Flagrant Baronessa | 9003   | 8.3       | 202778        |
| 904    | Alec Shaw          | 9005   | 8.2       | 484746        |
| 905    | Francois Truffaut  | 9006   | 7.3       |               |
| 906    | Victor Woeltjen    | 9007   | 8.6       | 779489        |
| 907    | Simon Wright       | 9008   |           | 227235        |
| 908    | Neal Wruck         | 9009   | 3         | 195961        |
| 909    | Paul Monks         | 9010   | 8.1       | 203875        |
| 910    | Mike Salvati       | 9011   | 8.4       |               |
| 911    | Armond White       | 9013   | 7         | 862618        |
| 912    | Wesley S. Walker   | 9001   | 7.7       | 830095        |
| 913    | Sasha Goldshtein   | 9014   | 4         | 642132        |
| 914    | Josh Cates         | 9015   | 7.7       | 81328         |
| 915    | Krug Stillo        | 9016   |           | 580301        |
| 916    | Scott LeBrun       | 9017   | 8.1       | 609451        |
| 917    | Hannah Steele      | 9018   | 8         | 667758        |
| 918    | Vincent Cadena     | 9019   | 8.4       | 511613        |
| 919    | Brandt Sponseller  | 9020   | 6.7       | 13091         |
| 920    | Richard Adams      | 9021   | 7         | 544452        |
| 921    | Andre Bazin        | 9022   | 7         | 557054        |
| 922    | Judith Christ      | 9023   | 7         | 569657        |
| 923    | Peter Travers      | 9024   | 6.9       | 582260        |
| 924    | Roger Ebert        | 9025   | 6.9       | 594862        |
| 926    | Pauline Kael       | 9026   | 6.9       | 607465        |
| 927    | Leonard Martin     | 9027   | 6.8       | 620067        |
| 928    | Andrew Sarris      | 9028   | 6.8       | 632670        |
| 925    | Gene Shalit        | 9029   | 6.8       | 645273        |

### Create movies table
Set the `mov_id` as primary key. After creating table, import the files as `.csv`
```SQL
CREATE TABLE "movies" (
	"mov_id"	INTEGER,
	"mov_name"	TEXT,
	"mov_year"	INTEGER,
	"mov_time"	INTEGER,
	"mov_lang"	TEXT,
	"mov_dt_rel"	TEXT,
	"mov_rel_country"	TEXT,
	PRIMARY KEY("mov_id")
)
```
#### Output
| mov_id | mov_name                 | mov_year | mov_time | mov_lang | mov_dt_rel | mov_rel_country |
| ------ | ------------------------ | -------- | -------- | -------- | ---------- | --------------- |
| 901    | Vertigo                  | 1958     | 128      | English  | 1958-08-24 | UK              |
| 902    | The Innocents            | 1961     | 100      | English  | 1962-02-19 | SW              |
| 903    | Lawrence of Arabia       | 1962     | 216      | English  | 1962-12-11 | UK              |
| 904    | The Deer Hunter          | 1978     | 183      | English  | 1979-03-08 | UK              |
| 905    | Amadeus                  | 1984     | 160      | English  | 1985-01-07 | UK              |
| 906    | Blade Runner             | 1982     | 117      | English  | 1982-09-09 | UK              |
| 907    | Eyes Wide Shut           | 1999     | 159      | English  |            | UK              |
| 908    | The Usual Suspects       | 1995     | 106      | English  | 1995-08-25 | UK              |
| 909    | Chinatown                | 1974     | 130      | English  | 1974-08-09 | UK              |
| 910    | Boogie Nights            | 1997     | 155      | English  | 1998-02-16 | UK              |
| 911    | Annie Hall               | 1977     | 93       | English  | 1977-04-20 | USA             |
| 912    | Princess Mononoke        | 1997     | 134      | Japanese | 2001-10-19 | UK              |
| 913    | The Shawshank Redemption | 1994     | 142      | English  | 1995-02-17 | UK              |
| 914    | American Beauty          | 1999     | 122      | English  |            | UK              |
| 915    | Titanic                  | 1997     | 194      | English  | 1998-01-23 | UK              |
| 916    | Good Will Hunting        | 1997     | 126      | English  | 1998-06-03 | UK              |
| 917    | Deliverance              | 1972     | 109      | English  | 1982-10-05 | UK              |
| 918    | Trainspotting            | 1996     | 94       | English  | 1996-02-23 | UK              |
| 919    | The Prestige             | 2006     | 130      | English  | 2006-11-10 | UK              |
| 920    | Donnie Darko             | 2001     | 113      | English  |            | UK              |
| 921    | Slumdog Millionaire      | 2008     | 120      | English  | 2009-01-09 | UK              |
| 922    | Aliens                   | 1986     | 137      | English  | 1986-08-29 | UK              |
| 923    | Beyond the Sea           | 2004     | 118      | English  | 2004-11-26 | UK              |
| 924    | Avatar                   | 2009     | 162      | English  | 2009-12-17 | UK              |
| 925    | Braveheart               | 1995     | 178      | English  | 1995-09-08 | UK              |
| 926    | Seven Samurai            | 1954     | 207      | Japanese | 1954-04-26 | JP              |
| 927    | Spirited Away            | 2001     | 125      | Japanese | 2003-09-12 | UK              |
| 928    | Back to the Future       | 1985     | 116      | English  | 1985-12-04 | UK              |

### Write a query in SQL to find the name and year of the movies.
```SQL
SELECT mov_name,mov_year FROM movies;
```
#### Output
| mov_name                 | mov_year |
| ------------------------ | -------- |
| Vertigo                  | 1958     |
| The Innocents            | 1961     |
| Lawrence of Arabia       | 1962     |
| The Deer Hunter          | 1978     |
| Amadeus                  | 1984     |
| Blade Runner             | 1982     |
| Eyes Wide Shut           | 1999     |
| The Usual Suspects       | 1995     |
| Chinatown                | 1974     |
| Boogie Nights            | 1997     |
| Annie Hall               | 1977     |
| Princess Mononoke        | 1997     |
| The Shawshank Redemption | 1994     |
| American Beauty          | 1999     |
| Titanic                  | 1997     |
| Good Will Hunting        | 1997     |
| Deliverance              | 1972     |
| Trainspotting            | 1996     |
| The Prestige             | 2006     |
| Donnie Darko             | 2001     |
| Slumdog Millionaire      | 2008     |
| Aliens                   | 1986     |
| Beyond the Sea           | 2004     |
| Avatar                   | 2009     |
| Braveheart               | 1995     |
| Seven Samurai            | 1954     |
| Spirited Away            | 2001     |
| Back to the Future       | 1985     |

### Write a query in SQL to find the year when the movie American Beauty released
```SQL
SELECT mov_year FROM movies WHERE mov_name = 'American Beauty';
```
#### Output
| mov_year |
| -------- |
| 1999     |
### Write a query in SQL to find the movie which was released in the year 1999
```SQL
SELECT mov_name FROM movies WHERE mov_year = 1999;
```
#### Output
| mov_name        |
| --------------- |
| Eyes Wide Shut  |
| American Beauty |
### Write a query in SQL to find the movies which was released before 1998.
```SQL
SELECT mov_name FROM movies WHERE mov_year < 1998;
```

#### Output
| mov_name                 |
| ------------------------ |
| Vertigo                  |
| The Innocents            |
| Lawrence of Arabia       |
| The Deer Hunter          |
| Amadeus                  |
| Blade Runner             |
| The Usual Suspects       |
| Chinatown                |
| Boogie Nights            |
| Annie Hall               |
| Princess Mononoke        |
| The Shawshank Redemption |
| Titanic                  |
| Good Will Hunting        |
| Deliverance              |
| Trainspotting            |
| Aliens                   |
| Braveheart               |
| Seven Samurai            |
| Back to the Future       |
### Write a query in SQL to return the name of all reviewers and name of movies together in a single list
Reference: [SQLite Inner Join](https://www.sqlitetutorial.net/sqlite-inner-join/)
```SQL
SELECT movies.mov_name, movie_reviewer.rev_name
FROM movie_reviewer
INNER JOIN movies
    ON movie_reviewer.mov_id = movies.mov_id;
```
#### Output
| mov_name                 | rev_name           |
|--------------------------|--------------------|
| Vertigo                  | Righty Sock        |
| The Innocents            | Jack Malvern       |
| Lawrence of Arabia       | Flagrant Baronessa |
| The Deer Hunter          | Alec Shaw          |
| Amadeus                  | Francois Truffaut  |
| Blade Runner             | Victor Woeltjen    |
| Eyes Wide Shut           | Simon Wright       |
| The Usual Suspects       | Neal Wruck         |
| Chinatown                | Paul Monks         |
| Boogie Nights            | Mike Salvati       |
| Annie Hall               | Armond White       |
| Princess Mononoke        | Wesley S. Walker   |
| The Shawshank Redemption | Sasha Goldshtein   |
| American Beauty          | Josh Cates         |
| Titanic                  | Krug Stillo        |
| Good Will Hunting        | Scott LeBrun       |
| Deliverance              | Hannah Steele      |
| Trainspotting            | Vincent Cadena     |
| The Prestige             | Brandt Sponseller  |
| Donnie Darko             | Richard Adams      |
| Slumdog Millionaire      | Andre Bazin        |
| Aliens                   | Judith Christ      |
| Beyond the Sea           | Peter Travers      |
| Avatar                   | Roger Ebert        |
| Seven Samurai            | Pauline Kael       |
| Spirited Away            | Leonard Martin     |
| Back to the Future       | Andrew Sarris      |
| Braveheart               | Gene Shalit        |
### Write a query in SQL to find the name of all reviewers who have rated 7 or more stars to their rating.
```SQL
SELECT rev_name, rev_stars
FROM movie_reviewer
WHERE rev_stars >= 7;
```
#### Output
| rev_name           | rev_stars |
|--------------------|-----------|
| Righty Sock        | 8.4       |
| Jack Malvern       | 7.9       |
| Flagrant Baronessa | 8.3       |
| Alec Shaw          | 8.2       |
| Francois Truffaut  | 7.3       |
| Victor Woeltjen    | 8.6       |
| Paul Monks         | 8.1       |
| Mike Salvati       | 8.4       |
| Armond White       | 7         |
| Wesley S. Walker   | 7.7       |
| Josh Cates         | 7.7       |
| Scott LeBrun       | 8.1       |
| Hannah Steele      | 8         |
| Vincent Cadena     | 8.4       |
| Richard Adams      | 7         |
| Andre Bazin        | 7         |
| Judith Christ      | 7         |

### Write a query in SQL to find the titles of all movies that have no ratings.
Reference: [SQLite IN](https://www.sqlitetutorial.net/sqlite-in/)
```SQL
SELECT 
    movies.mov_name, movie_reviewer.num_o_ratings
FROM 
    movie_reviewer
    INNER JOIN movies ON 
        movies.mov_id = movie_reviewer.mov_id
    WHERE 
        movie_reviewer.num_o_ratings IS NULL;
```
#### Output
| mov_name      | num_o_ratings |
|---------------|---------------|
| Amadeus       |               |
| Boogie Nights |               |

### Write a query in SQL to find the titles of the movies with ID 905, 907, 917
```SQL
SELECT mov_name FROM movies
WHERE mov_id IN (905,907,917)
```

#### Output
| mov_name       |
|----------------|
| Amadeus        |
| Eyes Wide Shut |
| Deliverance    |

### Write a query in SQL to find the list of all those movies with year which include the words Boogie Nights
References: [SQLite LIKE](https://www.sqlitetutorial.net/sqlite-like/)
```SQL
SELECT
	mov_name,mov_year
FROM
	movies
WHERE
	mov_name LIKE '%Boogie Nights%';
```
#### Output
| mov_name      | mov_year |
|---------------|----------|
| Boogie Nights | 1997     |


