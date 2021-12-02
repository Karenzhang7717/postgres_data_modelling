**Introduction**

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

**Purpose of the database and the analytical goals**

The Postgres database with tables designed to optimize queries on song play analysis. Instead of storing large volume of data into JSON files, a database that is scalable and can be easily used for modelling is designed. The database makes querying, retrieval of data much easier.

The schema helps Sparkify to understand the following business logics:

- Types of songs, artists that a user are interested in listening over a particular period of time

- Potential "Next songs" that a user would like to listen to.

  With these information, Sparkify could do several analysis and recommend top hits for a country, most popular songs over a time period, and recommend artists, musics that an user may be interested in.

**Justifications of the database schema design and ETL pipeline**

The STAR schema consists of one fact table, referencing numbers of dimension tables. 

The Fact table, songplay, contains attributes include user information and song information referencing to the dimension tables.

The dimension tables, songs, users, artists, time that record various attributes.

ETL Pipeline:

- Create songs, artists dimension tables, from extracting songs_data
- Create users, time dimension tables, from extracting log_data
- Create the fact table, songplay, from joining and selecting columns from the dimension tables

​		

**ERD Diagram:**

![https://github.com/Karenzhang7717/postgres_data_modelling/blob/main/sparkifydb_erd.png]()

**How to execute:**

1. Install requirements from requirements.txt, and create a database called sparkifydb with owner to "student"
2. Run create_tables.py
3. Run etl.py
4. Check results in test.ipynb