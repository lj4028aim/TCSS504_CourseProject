import sqlite3
from sqlite3 import Error
import random
import os


# the relative file path
path = 'db/TriviaMaze.db'

# get the path to the directory this script is in
scriptdir = os.path.dirname(__file__)
# add the relative path to the database file from there
db_path = os.path.join(scriptdir, path)




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


def get_questions(num_questions_expect):
    """
    Connecting to database and fetch certain amount of questions. Storing all fetched questions into
    :param num_questions_expect: number of questions expected
    :return: a list which hold all questions. Each question and its associated answers is in dictionary format.
    """
    try:

        conn = create_connection(db_path)

        cur = conn.cursor()
        cur.execute("SELECT *  FROM Questions")
        rows = cur.fetchall()

        questions = []
        num_questions = gen_num_questions(num_questions_expect)
        for i in num_questions:
            question = {"question": str(rows[i][0]).strip(),
                        "A": str(rows[i][1]),
                        "B": str(rows[i][2]),
                        "C": str(rows[i][3]),
                        "D": str(rows[i][4]),
                        "correct_answer": str(rows[i][5])}
            questions.append(question)
        cur.close()
        return questions
    except sqlite3.Error as error:
        print("Failed to read data from table", error)
    finally:
        if conn:
            conn.close()


def gen_num_questions(num_questions_expect):
    """
    Generate a list holds all unique randomly generated number
    :return: a list which is composed of unique question index
    """
    total_num_questions = 49825  # number of questions stored in database
    num_questions = []
    while True:
        num = random.randrange(0, total_num_questions)
        num_questions.append(num)
        if len(num_questions) == 1:
            pass
        else:
            for i in range(len(num_questions) - 1):
                if num == num_questions[i]:
                    num_questions.pop()
                    pass
        if len(num_questions) == num_questions_expect:
            break

    return num_questions

def get_answer(questions):
    """
    Get correct answer from dictionary of questions
    :param questions: a dictionary which hold all questions and answers
    :return: correct answer
    """
    return questions["correct_answer"]


if __name__ == "__main__":
    pass
    # q = get_questions()
    # answer = get_answer(q)
    # num_questions = len(q["question"])
    # print(f"There are totally {num_questions} questions selected: \n")
    # for i in range(len(q["question"])):
    #     print(q["question"][i])
    #     print(q["A"][i], end=", ")
    #     print(q["B"][i], end=", ")
    #     print(q["C"][i], end=", ")
    #     print(q["D"][i])
    #     print(get_answer(q)[i], "\n")
