CREATE TABLE Movies (
  Sr_num INT PRIMARY KEY,
  Movie_name VARCHAR(40),
  Actor_name VARCHAR(40),
  Actress_name varchar(40),
  Director_name VARCHAR(40),
  year_of_relaese date
);

Insert into Movies Values(1, "Mimi", "Pankaj Tripathi", "Kriti Sanaon", "Laxman Utekar", "2021-07-26");
Insert into Movies Values(2, "Piku", "Amitabh Bacchhan", "Deepika Padukone", "Shoojit Sircar", "2015-05-08");
Insert into Movies Values(3, "Baby", "Akshay Kumar", "Madhurima Tuli", "Neeraj Pandey", "2015-01-23");
Insert into Movies Values(4, "Jolly LLB 2", "Akshay Kumar", "Huma Querishi", "Subhash Kapoor", "2017-02-10");
Insert into Movies Values(5, "3 Idiots", "Aamir Khan", "Kareena Kapoor", "Rajkumar Hirani", "2009-12-25");

select * from Movies;

SELECT Movie_name FROM Movies Where Actor_name = "Akshay Kumar";