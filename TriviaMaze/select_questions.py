import sqlite3
from sqlite3 import Error
import random


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


def get_questions():
    """
    Connecting to database and fetch certain amount of questions. Storing all fetched questions into
    a dictionary.
    :return: a dictionary which hold all questions and answers
    """
    try:
        database = "C:/Users/Ji/PycharmProjects/504pythonProject/TCSS504_CourseProject/TriviaMaze/TriviaMaze.db"

        conn = create_connection(database)

        cur = conn.cursor()
        cur.execute("SELECT *  FROM Questions")
        num_question = random.randrange(10, 50)
        rows = cur.fetchmany(num_question)

        question = []
        dist1 = []
        dist2 = []
        dist3 = []
        dist4 = []
        key = []
        for row in rows:
            question.append(str(row[0]).strip())
            dist1.append(str(row[1]))
            dist2.append(str(row[2]))
            dist3.append(str(row[3]))
            dist4.append(str(row[4]))
            key.append((str(row[5])))

        questions = {"question": question,
                     "A": dist1,
                     "B": dist2,
                     "C": dist3,
                     "D": dist4,
                     "correct_answer": key}
        cur.close()
        return questions
    except sqlite3.Error as error:
        print("Failed to read data from table", error)
    finally:
        if conn:
            conn.close()


def get_answer(questions):
    """
    Get correct answer from dictionary of questions
    :param questions: a dictionary which hold all questions and answers
    :return: correct answer
    """
    return questions["correct_answer"]


if __name__ == "__main__":
    q = get_questions()
    answer = get_answer(q)
    num_questions = len(q["question"])
    print(f"There are totally {num_questions} questions selected: \n")
    for i in range(len(q["question"])):
        print(q["question"][i])
        print(q["A"][i], end=", ")
        print(q["B"][i], end=", ")
        print(q["C"][i], end=", ")
        print(q["D"][i])
        print(get_answer(q)[i], "\n")
