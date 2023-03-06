import sqlite3
from sqlite3 import Error
import pandas as pd
import os

class QuestionAnswerDatabase:

    def __init(self):
        pass

    def get_db_path(self):
        # relative file path
        path = 'db/TriviaMaze.db'
        # get the path to the directory this script is in
        script_dir = os.path.dirname(__file__)
        # add the relative path to the database file from there
        db_path = os.path.join(script_dir, path)
        # make sure the path exists and if not create it
        os.makedirs(os.path.dirname(db_path), exist_ok=True)

        return db_path

    def get_question_path(self):
        # relative file path
        csv_path = 'TriviaMazeQuestion/csv_version/'
        # get the path to the directory this script is in
        script_dir = os.path.dirname(__file__)
        # add the relative path to input question csv file
        q_path = os.path.join(script_dir, csv_path)

        return q_path

    def create_connection(self, db_file):
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

    def main(self):
        """
         Inserting values stored in csv files into database with panda package
         :return:
         """
        database = db_path
        question_path = q_path
        conn = self.create_connection(database)

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
    db = QuestionAnswerDatabase()
    db_path = db.get_db_path()
    q_path = db.get_question_path()
    db.main()
