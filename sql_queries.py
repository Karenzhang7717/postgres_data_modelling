# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

songplay_table_create = (""" create table if not exists songplay
(
    songplay_id SERIAL PRIMARY KEY NOT NULL,
    ts bigint NOT NULL,
    userId    integer NOT NULL,
    level       varchar,
    songId    integer,
    artistId  integer,
    sessionId integer,
    location    varchar,
    userAgent varchar
);
""")

user_table_create = ("""create table if not exists users
(
    userId    integer PRIMARY KEY,
    firstName varchar,
    lastName  varchar,
    gender      varchar,
    level       varchar
);
""")

song_table_create = ("""create table if not exists songs
(
    song_id   varchar PRIMARY KEY NOT NULL,
    title     varchar,
    artist_id varchar,
    year      integer,
    duration  double precision
);
""")

artist_table_create = (""" create table if not exists artists
(
    artist_id        varchar PRIMARY KEY NOT NULL,
    artist_name      varchar,
    artist_location  varchar,
    artist_latitude  double precision,
    artist_longitude double precision
);
""")

time_table_create = ("""create table if not exists time
(
    ts        timestamp PRIMARY KEY NOT NULL,
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
    (userId, firstName, lastName, gender, level)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT(userId)
    DO 
        UPDATE SET level = EXCLUDED.level
""")

song_table_insert = ("""INSERT INTO songs
    (song_id, title, artist_id, year, duration)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (song_id) DO NOTHING
""")

artist_table_insert = ("""INSERT INTO artists(
    artist_id,
    artist_name,
    artist_location,
    artist_latitude,
    artist_longitude)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (artist_id) DO NOTHING
""")

time_table_insert = ("""INSERT INTO time
    (ts, hour, day, week, month, year, dayofweek)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (ts) DO NOTHING
""")

# FIND SONGS

song_select = ("""
    SELECT s.song_id, a.artist_id 
        FROM songs s JOIN artists a ON s.artist_id= a.artist_id
        WHERE s.title = %s 
         AND a.artist_id = %s 
         AND s.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create,
                        time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
