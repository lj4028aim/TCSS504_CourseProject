import sqlite3
from sqlite3 import Error
import pandas as pd


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


# def create_questions(conn, questions):
#     sql = """ INSERT INTO questions (Questions, answer_A, answer_B, answer_C, answer_D, Correct_answer)
#                 VALUES (?, ?, ?, ?, ?, ?)"""
#     cur = conn.cursor()
#     cur.execute(sql, questions)
#     conn.commit()
#
#     return cur.lastrowid


def main():
    """
     Inserting values stored in csv files into database with panda package
     :return:
     """
    database = "C:/Users/Ji/PycharmProjects/504pythonProject/TCSS504_CourseProject/TriviaMaze/TriviaMaze.db"
    question_path = "C:/Users/Ji/PycharmProjects/504pythonProject/TCSS504_CourseProject/TriviaMaze/TriviaMazeQuestion/csv_version/"
    conn = create_connection(database)

    question_list = ["animals.csv",
                     "brain-teasers.csv",
                     "celebrities.csv",
                     "entertainment.csv",
                     "for-kids.csv",
                     "general.csv",
                     "geography.csv",
                     "history.csv",
                     "hobbies.csv",
                     "humanities.csv",
                     "literature.csv",
                     "movies.csv",
                     "music.csv",
                     "newest.csv",
                     "people.csv",
                     "rated.csv",
                     "religion-faith.csv",
                     "science-technology.csv",
                     "sports.csv",
                     "television.csv",
                     "video-games.csv",
                     "world.csv"]
    fields = ["Questions", "answer_A", "answer_B", "answer_C", "answer_D", "Correct_answer"]
    for i in range(len(question_list)):
        df = pd.read_csv(question_path + f"{question_list[i]}", usecols=fields)

        df.to_sql("Questions", conn, if_exists="append", index=False)


if __name__ == "__main__":
    main()
