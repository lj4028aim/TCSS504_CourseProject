import sqlite3
from sqlite3 import Error
import pandas as pd
import os



# the relative file path
path = 'db/TriviaMaze.db'
csv_path = 'TriviaMazeQuestion/csv_version/'
# get the path to the directory this script is in
script_dir = os.path.dirname(__file__)
# add the relative path to the database file from there
db_path = os.path.join(script_dir, path)
# add the relative path to input question csv file
q_path = os.path.join(script_dir, csv_path)
# make sure the path exists and if not create it
os.makedirs(os.path.dirname(db_path), exist_ok=True)

def create_connection(db_file):
    """
       create a database connection to the SQLite database specified by the db_file
       :param db_file: database file
       :return: connection object or None
       """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn



def main():
    """
     Inserting values stored in csv files into database with panda package
     :return:
     """
    database = db_path
    question_path = q_path
    conn = create_connection(database)

    question_list = ["animals.csv",
                     # "brain-teasers.csv",
                     # "celebrities.csv",
                     # "entertainment.csv",
                     # "for-kids.csv",
                     # "general.csv",
                     # "geography.csv",
                     # "history.csv",
                     # "hobbies.csv",
                     # "humanities.csv",
                     # "literature.csv",
                     # "movies.csv",
                     # "music.csv",
                     # "newest.csv",
                     # "people.csv",
                     # "rated.csv",
                     # "religion-faith.csv",
                     # "science-technology.csv",
                     # "sports.csv",
                     # "television.csv",
                     # "video-games.csv",
                     "world.csv"]
    fields = ["Questions", "answer_A", "answer_B", "answer_C", "answer_D", "Correct_answer"]
    for i in range(len(question_list)):
        df = pd.read_csv(question_path + f"{question_list[i]}", usecols=fields)

        df.to_sql("Questions", conn, if_exists="append", index=False)


if __name__ == "__main__":
    main()
