import pickle
from player import Player
from maze import Maze

"""Use this file to test save data"""

player = Player()
player.coordinates[0] = 4
player.coordinates[1] = 4
maze = Maze(5, 5)
room_size = 90

current_progres = [player, maze, room_size]
print(current_progres)

# create a binary file for writing 'wb' called laptopstore.pkl
# pkl extension is not necessary but it is standard for pickle files
pickle_file = open('game_data.pkl', 'wb')

# pickle the nested object and write it to file
pickle.dump(current_progres, pickle_file)

# close the file
pickle_file.close()

# now read the pickle file, 'rb' open a binary file for reading
pickle_file = open('game_data.pkl', 'rb')

# unpickle the nested object from the file
saved_data = pickle.load(pickle_file)

# close file
pickle_file.close()

# print the read in contents :-)
print("Here are the unpickled player from", saved_data[0].name)
print("--------------------------------------------------")
for data in saved_data:
    print(data)
print("==================================================")
print("I can pickle almost as well as my grandma used to!")
print("==================================================")

