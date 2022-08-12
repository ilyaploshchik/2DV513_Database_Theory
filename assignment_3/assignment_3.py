# import libraries
import streamlit as st
import MySQLdb as sql
import pandas as pd
from sqlalchemy import create_engine
pd.options.mode.chained_assignment = None # default='warn'
import numpy as np
from PIL import Image

st.set_page_config(
    page_title='Olympics Historical Data',
    page_icon="olympics.png")

col1, col2 = st.columns(2)

with col1:
        st.header('Olympics Historical Data')

with col2:
        image = Image.open('olympics.jpg')
        st.image(image)

# # create daraframes from csvs
# df_athlete_bio = pd.read_csv(r'source/athlete_bio.csv', )
# df_results = pd.read_csv(r'source/athlete_event_results.csv')
# df_country = pd.read_csv(r'source/country.csv')
# df_games = pd.read_csv(r'source/games.csv')

# # keep only 'athlete_id', 'name', 'sex', 'born', 'height', 'weight' and 'country_noc' columns in df_athlete_bio
# df_athlete_bio = df_athlete_bio[['athlete_id', 'name', 'sex', 'born', 'height', 'weight', 'country_noc']]
# # keep only 'result_id', 'athlete_id', 'sport', 'event', 'edition', 'medal' and 'isTeamSport' columns in df_results
# df_results = df_results[['result_id', 'athlete_id', 'sport', 'event', 'edition', 'medal', 'isTeamSport']]
# # keep only 'games', 'year', 'cities', 'country_noc', 'start_date' and  'end_date' columns in df_games
# df_games = df_games[['games', 'years', 'cities', 'countries_noc', 'start_date', 'end_date']]
# # change country_nok to country_code and born to date_of_birth in df_athlete_bio
# df_athlete_bio.rename(columns={'country_noc':'country_code', 'born':'date_of_birth'}, inplace=True)
# # change nok to country_code in df_country
# df_country.rename(columns={'noc':'country_code'}, inplace=True)
# # change country_nok to sport in category
# df_results.rename(columns={'sport':'category'}, inplace=True)
# # change games to edition, year to year, cities to city, country_nok to country_code columns in df_games
# df_games.rename(columns={'games':'edition', 'years':'year', 'cities':'city', 'countries_noc':'country_code'}, inplace=True)


# # convert 'na' to nan
# df_athlete_bio = df_athlete_bio.replace('na', np.nan)
# df_results = df_results.replace('na', np.nan)
# df_games = df_games.replace('na', np.nan)

# # try to convert to numeric, if not possible, drop row
# df_athlete_bio['height'] = pd.to_numeric(df_athlete_bio['height'], errors='coerce')
# df_athlete_bio['weight'] = pd.to_numeric(df_athlete_bio['weight'], errors='coerce')
# df_athlete_bio['date_of_birth'] = pd.to_datetime(df_athlete_bio['date_of_birth'], errors='coerce')
# df_games['start_date'] = pd.to_datetime(df_games['start_date'], errors='coerce')
# df_games['end_date'] = pd.to_datetime(df_games['end_date'], errors='coerce')

# # replace na with 'none' in df_results.medal to keep values 
# df_results.medal = df_results.medal.replace(np.nan, 'none')

# # drop rows with nan values
# df_athlete_bio = df_athlete_bio.dropna()
# df_results = df_results.dropna()
# df_games = df_games.dropna()


# # check for any duplicates in df_results athlete_id and result_id, remove if any
# # these values to be used as primary leys later on
# df_athlete_bio.drop_duplicates(subset=['athlete_id'])
# df_results = df_results.drop_duplicates(subset=['athlete_id', 'result_id'])
# df_country = df_country.drop_duplicates(subset=['country_code'])
# df_games = df_games.drop_duplicates(subset=['year'])

# # connect to host using MySQLdb
# db = sql.connect(host='localhost', user='root', passwd='root')
# # create a cursor object
# cursor = db.cursor()

# # drop database if it exists
# cursor.execute('DROP DATABASE IF EXISTS olympcisdb')
# cursor.execute("CREATE DATABASE IF NOT EXISTS olympcisdb")

# cursor.execute("USE olympcisdb")
# engine = create_engine("mysql+mysqldb://{user}:{pw}@localhost/{db}".format(user="root", pw="root", db="olympcisdb"))
# # set engine charset to utf8mb4
# engine.execute("ALTER DATABASE olympcisdb CHARACTER SET = utf8mb4")

# # Insert Dataframes into SQL database, set index column to be index
# df_athlete_bio.to_sql('athlete_bio', con = engine, if_exists = 'replace', index= True)
# df_results.to_sql('results', con = engine, if_exists = 'replace', index= True)
# df_country.to_sql('country', con = engine, if_exists = 'replace', index= True)
# df_games.to_sql('games', con = engine, if_exists = 'replace', index= True)

# # set athlete_id  as primary key for athlete_bio table
# cursor.execute("ALTER TABLE athlete_bio ADD PRIMARY KEY (athlete_id)")
# # set result_id and athlete_id as primary keys for results table
# cursor.execute("ALTER TABLE results ADD PRIMARY KEY (athlete_id, result_id)")
# # set country_code type as char(5) and primary key
# cursor.execute("ALTER TABLE country MODIFY country_code CHAR(5) NOT NULL PRIMARY KEY")
# # set year as primary key for games table
# cursor.execute("ALTER TABLE games ADD PRIMARY KEY (year)")


# # create view with city, edition and country as columns, join with country table
# cursor.execute("CREATE VIEW IF NOT EXISTS city_view AS SELECT games.city, games.edition, country.country FROM games INNER JOIN country ON games.country_code = country.country_code")

# # country with the highest number of athletes over the years
# cursor.execute("SELECT country.country, COUNT(athlete_bio.athlete_id) AS athletes FROM country INNER JOIN athlete_bio ON country.country_code = athlete_bio.country_code GROUP BY country.country_code ORDER BY athletes DESC LIMIT 1")
# for row in cursor:
#     print(row)


# # which country has the tallest athlets in the olympics?
# cursor.execute("SELECT country.country, MAX(athlete_bio.height) AS tallest FROM country INNER JOIN athlete_bio ON country.country_code = athlete_bio.country_code GROUP BY country.country_code ORDER BY tallest DESC LIMIT 1")
# for row in cursor:
#     print(row)

# # country with max number of athletes who won gold medals
# cursor.execute("SELECT country.country, COUNT(results.medal) AS gold FROM country INNER JOIN athlete_bio ON country.country_code = athlete_bio.country_code INNER JOIN results ON athlete_bio.athlete_id = results.athlete_id  WHERE results.medal = 'gold' GROUP BY country.country_code ORDER BY gold DESC LIMIT 1")
# for row in cursor:
#     print(row)

# # which country held the most olympic games?
# cursor.execute("SELECT country.country, COUNT(games.year) AS games FROM country INNER JOIN games ON country.country_code = games.country_code GROUP BY country.country_code ORDER BY games DESC LIMIT 1")
# for row in cursor:
#     print(row)

# # Are there any cities that hold more than one olympcs? if there are more then one print them
# cursor.execute("SELECT city_view.city, COUNT(city_view.edition) AS games FROM city_view GROUP BY city_view.city HAVING games > 1")
# for row in cursor:
#     print(row)




