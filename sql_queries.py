# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = (""" create table if not exists songplay
(
    ts          timestamp,
    "userId"    integer,
    level       varchar,
    "songId"    integer,
    "artistId"  integer,
    "sessionId" integer,
    location    varchar,
    "userAgent" varchar
);
""")

user_table_create = ("""create table if not exists users
(
    "userId"    integer not null,
    "firstName" varchar,
    "lastName"  varchar,
    gender      varchar,
    level       varchar
);
""")

song_table_create = ("""create table if not exists songs
(
    song_id   varchar not null,
    title     varchar,
    artist_id varchar,
    year      integer,
    duration  double precision
);
""")

artist_table_create = (""" create table if not exists artists
(
    artist_id        integer not null,
    artist_name      varchar,
    artist_location  varchar,
    artist_latitude  double precision,
    artist_longitude double precision
);
""")

time_table_create = ("""create table if not exists time
(
    ts        timestamp,
    hour      integer,
    day       integer,
    week      integer,
    month     integer,
    year      integer,
    dayofweek integer
);

""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplay
    (ts, userId, level, songId, artistId, sessionId,location,userAgent)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""INSERT INTO users
    (useId, firstName, lastName, gender, level)
    VALUES (%s, %s, %s, %s, %s)
""")

song_table_insert = ("""INSERT INTO songs
    (song_id, title, artist_id, year, duration)
    VALUES (%s, %s, %s, %s, %s)
""")

artist_table_insert = ("""INSERT INTO artists(
    artist_id,
    artist_name,
    artist_location,
    artist_latitude,
    artist_longitude)
VALUES(%s, %s, %s, %s, %s)
""")

time_table_insert = ("""INSERT INTO time
    (ts, hour, day, week, month, year, dayofweek)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create,
                        time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
