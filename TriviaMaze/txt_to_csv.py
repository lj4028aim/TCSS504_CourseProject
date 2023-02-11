import os
import pandas as pd
import numpy as np


def txt_to_csv(path):
    """
    convert questions from txt to csv
    :param path: path where stored all txt files
    :return: dataframe of all questions
    """
    questions = []
    key = []
    dist1 = []
    dist2 = []
    dist3 = []
    dist4 = []
    with open(path, errors='ignore', mode="r") as file1:
        files = file1.readlines()
        i = 0
        for i in range(len(files)):
            if files[i][0] == '\n':
                try:
                    if files[i + 1][3] == '#':
                        continue
                    questions.append(files[i + 1][3:len(files) - 1])
                    key.append(files[i + 2][2:len(files[i + 2]) - 1])
                    if files[i + 3] != "\n":
                        dist1.append(files[i + 3][2:len(files[i + 3]) - 1])
                    else:
                        dist1.append(np.nan)
                        dist2.append(np.nan)
                        dist3.append(np.nan)
                        dist4.append(np.nan)
                        continue
                    if files[i + 4] != "\n":
                        dist2.append(files[i + 4][2:len(files[i + 4]) - 1])
                    else:
                        dist2.append(np.nan)
                        dist3.append(np.nan)
                        dist4.append(np.nan)
                        continue
                    if files[i + 5] != "\n":
                        dist3.append(files[i + 5][2:len(files[i + 5]) - 1])
                    else:
                        dist3.append(np.nan)
                        dist4.append(np.nan)
                        continue
                    if files[i + 6] != "\n":
                        dist4.append(files[i + 6][2:len(files[i + 6]) - 1])
                    else:
                        dist4.append(np.nan)
                except:
                    pass
    bank = {}
    bank["Questions"] = questions
    bank["answer_A"] = dist1
    bank["answer_B"] = dist2
    bank["answer_C"] = dist3
    bank["answer_D"] = dist4
    bank["Correct_answer"] = key
    df = pd.DataFrame(bank)
    return df


def parse_files(source_path, destination_path):
    """
    output file in csv mode
    :param source_path: path where stored all txt files
    :param destination_path: path where user want csv files to be stored
    :return: csv files
    """

    filenames = source_path
    for files in os.listdir(filenames):
        path = filenames + files
        data = txt_to_csv(path)
        data.to_csv(destination_path + files + '.csv')


if __name__ == "__main__":

    # source_path = "C:\Users\Ji\PycharmProjects\504pythonProject\TCSS504_CourseProject\TriviaMaze\TriviaMazeQuestion\txt_version\"
    # destination_path = "C:\Users\Ji\PycharmProjects\504pythonProject\TCSS504_CourseProject\TriviaMaze\TriviaMazeQuestion\csv_version\"
    parse_files(source_path=input('SourcePath: '), destination_path=input('Destination Path: '))
    print(f"Done converting~ ")
