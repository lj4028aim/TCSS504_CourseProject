import random

import math
import PySimpleGUI as psg
from dungeon import Dungeon
from adventurer import Adventurer


def dungeon_adventrue_test():
    intro()
    should_play = ask_to_play()
    if should_play:
        name = ask_for_name()
        maze_size = ask_for_input_size()
        adventurer = Adventurer(name)
        print(f"Good luck {name}!")
        print(adventurer)
    my_map = init_games(maze_size)
    layout(name, my_map, maze_size)


def layout(name, my_map, maze_size):
    ad = Adventurer(name)
    AppFont = 'Any 16'
    psg.theme('DarkAmber')
    layout = [[(psg.Graph((60 * maze_size, 60 * maze_size), (0, 0), (60 * maze_size, 60 * maze_size), key='Graph'))],
              [psg.Text('Player: ' + str(ad._name), key='-P1-', text_color='white'),
               psg.Text('Hit point: ' + str(ad.hit_point), key='-P2-', text_color='white'),
               psg.Text('Healing potion: ' + str(ad._number_healing_potions), key='-P3-', text_color='white'),
               psg.Text('Vision potion:  ' + str(ad._number_vision_potions), key='-P4-', text_color='white')],
              [psg.Text('Pillars Found: ', key='-P5-', text_color='white'),
               psg.Text('', key='-P6-', text_color='white'),
               psg.Text('', key='-P7-', text_color='white'),
               psg.Text('', key='-P8-', text_color='white'),
               psg.Text('', key='-P9-', text_color='white')],
              [psg.Button('Re-play', font=AppFont), psg.Text('', key='-P10-', text_color='white')]]
    window = psg.Window('Dungeon Adventure', layout, resizable=True, finalize=True, return_keyboard_events=True)
    dungeon_adventure_event_checker(my_map, window, ad)


def init_games(maze_size):
    my_map = Dungeon(maze_size, maze_size)  # assume the rows and columns must be greater than 1
    my_map.generate()
    random_assign_room_and_items(my_map)
    return my_map


def intro():
    print("Welcome to Dungeon Adventure!\n"
          "\n"
          "We need you to explore the dungeon and find the four pillars of OOP.\n"
          "Your goal:\n"
          "\t1) Collect all the four pillars of OOP\n"
          "\t2) You can use arrow  \"UP\", \"DOWN\", \"LEFT\", \"RIGHT\" key to move .\n"
          "\t3) \"V\" key to use Vision potion.\n"
          "\t4) \"H\" key to use Healing potion.\n"
          "\t5) Get to the exit safely.\n"
          "\t6) Click \"Re-play\" button to replay the game.\n"
          "\n"
          "Items randomly placed in each room:\n"
          "\t1) Healing potion(random heal amount),\n"
          "\t2) Vision potion(reveal, adjacent rooms)\n"
          "\t3) Pit(random damage to adventurer),\n"
          "\t4) OOP pillars(\"A\",\"P\",\"I\",\"E\")\n"
          "\n"
          "Are you ready to play?!!!\n"
          "\n"
          "\'c\' : for continue\n"
          "\'q\' : for quit\n"
          "\n")


def ask_to_play():
    choice = input("Your choice: ")
    while not (choice.startswith("c") or choice.startswith("q")):
        print("Sorry not an option, please type one of the options.\n"
              "\'c\' : for continue\n"
              "\'q\' : for quit\n"
              "\n")
        choice = input("Your choice: ")
    if choice.startswith("c"):
        return True
    else:
        return False


def ask_for_name():
    player_name = input("What is your name? ")
    return player_name


def ask_for_input_size():
    while True:
        try:
            maze_size = int(input("Please input the maze a size range from 6 - 12:    "))
        except ValueError:  # just catch the exceptions you know!
            print
            'That\'s not a number!'
        else:
            if 6 <= maze_size <= 12:  # this is faster
                break
            else:
                print("Out of range. Try input again")
    return maze_size


def checkEvents(event):
    """
    Method is used to check event which has been executed by user.
    :param event: event name, such as 'Up', 'Down' or etc.
    :return: one of the even name.
    """
    move = ''
    if len(event) == 1:
        if ord(event) == 63232:  # UP
            move = 'Up'
        elif ord(event) == 63233:  # DOWN
            move = 'Down'
        elif ord(event) == 63234:  # LEFT
            move = 'Left'
        elif ord(event) == 63235:  # RIGHT
            move = 'Right'
        elif ord(event) == 86 or ord(event) == 118:  # V
            move = 'V'
        elif ord(event) == 72 or ord(event) == 104:  # H
            move = 'H'
        elif ord(event) == 87 or ord(event) == 119:  # W
            move = 'W'
    # Filter key press Windows :
    else:
        if event.startswith('Up'):
            move = 'Up'
        elif event.startswith('Down'):
            move = 'Down'
        elif event.startswith('Left'):
            move = 'Left'
        elif event.startswith('Right'):
            move = 'Right'
        elif event.startswith('V'):
            move = 'V'
        elif event.startswith('H'):
            move = 'H'
        elif event.startswith('W'):
            move = 'W'
    return move


def random_assign_room_and_items(my_map):
    exit_count = 1
    entrance_count = 1
    A_count = 1
    E_count = 1
    I_count = 1
    P_count = 1
    healing_potion_count = math.floor(0.1 * my_map.rows * my_map.cols)  # 10% of healing potion
    vision_potion_count = math.floor(0.1 * my_map.rows * my_map.cols)  # 10% of vision potion
    pit_count = math.floor(0.1 * my_map.rows * my_map.cols)  # 10% of pit
    total_count = exit_count + entrance_count + A_count + E_count + I_count + P_count + pit_count
    random_assign_room_list = random.sample(range(0, my_map.rows * my_map.cols - 1), total_count)
    for n in random_assign_room_list:
        if exit_count > 0:
            my_map.rooms[n // my_map.cols][n % my_map.rows].set_exit(True)
            exit_count -= 1
        elif A_count > 0:
            my_map.rooms[n // my_map.cols][n % my_map.rows].set_pillar("Abstraction")
            A_count -= 1
        elif E_count > 0:
            my_map.rooms[n // my_map.cols][n % my_map.rows].set_pillar("Encapsulation")
            E_count -= 1
        elif I_count > 0:
            my_map.rooms[n // my_map.cols][n % my_map.rows].set_pillar("Inheritance")
            I_count -= 1
        elif P_count > 0:
            my_map.rooms[n // my_map.cols][n % my_map.rows].set_pillar("Polymorphism")
            P_count -= 1
        elif pit_count > 0:
            my_map.rooms[n // my_map.cols][n % my_map.rows].set_pit(True)
            pit_count -= 1
        random_assign_healing_potion_list = random.sample(range(0, my_map.rows * my_map.cols - 1), healing_potion_count)
        for i in random_assign_healing_potion_list:
            if healing_potion_count > 0:
                my_map.rooms[i // my_map.cols][i % my_map.rows].set_health_potion(True)
                healing_potion_count -= 1
        random_assign_vision_potion_list = random.sample(range(0, my_map.rows * my_map.cols - 1), vision_potion_count)
        for j in random_assign_vision_potion_list:
            if vision_potion_count > 0:
                my_map.rooms[j // my_map.cols][j % my_map.rows].set_vision_potion(True)
                vision_potion_count -= 1


def draw_image(x, y, my_map, window):
    """
    Method is used to generate an image based on x, y, and my_map all three parameters.
    :param x: x coordinate. e.g.: current x coordinate.
    :param y: y coordinate. e.g.: current y coordinate.
    :param my_map: a 2D array created in class Dungeon.
    :return: an visualized image.
    """
    room = my_map.get_room()
    if 0 > x or x >= my_map.rows or 0 > y or y >= my_map.cols:
        return
    if room[x][y]._exit:
        window['Graph'].draw_image(filename='images/exit.png', location=(y * 60, my_map.rows * 60 - x * 60))
    elif room[x][y]._pit:
        window['Graph'].draw_image(filename='images/pit.png', location=(y * 60, my_map.rows * 60 - x * 60))
    elif room[x][y].south and room[x][y].west and room[x][y].east:
        window['Graph'].draw_image(filename='images/T1.png', location=(y * 60, my_map.rows * 60 - x * 60))
    elif room[x][y].north and room[x][y].south and room[x][y].west:
        window['Graph'].draw_image(filename='images/T2.png', location=(y * 60, my_map.rows * 60 - x * 60))
    elif room[x][y].north and room[x][y].south and room[x][y].east:
        window['Graph'].draw_image(filename='images/T3.png', location=(y * 60, my_map.rows * 60 - x * 60))
    elif room[x][y].north and room[x][y].west and room[x][y].east:
        window['Graph'].draw_image(filename='images/T4.png', location=(y * 60, my_map.rows * 60 - x * 60))
    elif room[x][y].north and room[x][y].west:
        window['Graph'].draw_image(filename='images/L1.png', location=(y * 60, my_map.rows * 60 - x * 60))
    elif room[x][y].north and room[x][y].east:
        window['Graph'].draw_image(filename='images/L2.png', location=(y * 60, my_map.rows * 60 - x * 60))
    elif room[x][y].north and room[x][y].south:
        window['Graph'].draw_image(filename='images/L3.png', location=(y * 60, my_map.rows * 60 - x * 60))
    elif room[x][y].west and room[x][y].east:
        window['Graph'].draw_image(filename='images/L4.png', location=(y * 60, my_map.rows * 60 - x * 60))
    elif room[x][y].west and room[x][y].south:
        window['Graph'].draw_image(filename='images/L5.png', location=(y * 60, my_map.rows * 60 - x * 60))
    elif room[x][y].east and room[x][y].south:
        window['Graph'].draw_image(filename='images/L6.png', location=(y * 60, my_map.rows * 60 - x * 60))
    elif room[x][y].south:
        window['Graph'].draw_image(filename='images/S1.png', location=(y * 60, my_map.rows * 60 - x * 60))
    elif room[x][y].west:
        window['Graph'].draw_image(filename='images/S2.png', location=(y * 60, my_map.rows * 60 - x * 60))
    elif room[x][y].north:
        window['Graph'].draw_image(filename='images/S3.png', location=(y * 60, my_map.rows * 60 - x * 60))
    elif room[x][y].east:
        window['Graph'].draw_image(filename='images/S4.png', location=(y * 60, my_map.rows * 60 - x * 60))
    if room[x][y].get_health_potion() and room[x][y].get_vision_potion():
        window['Graph'].draw_image(filename='images/H.png', location=(y * 60, my_map.rows * 60 - x * 60))
        window['Graph'].draw_image(filename='images/V.png', location=(y * 60, my_map.rows * 60 - x * 60))
    elif room[x][y].get_health_potion():
        window['Graph'].draw_image(filename='images/H.png', location=(y * 60, my_map.rows * 60 - x * 60))
    elif room[x][y].get_vision_potion():
        window['Graph'].draw_image(filename='images/V.png', location=(y * 60, my_map.rows * 60 - x * 60))
    elif room[x][y].get_pillar() == "Abstraction":
        window['Graph'].draw_image(filename='images/A.png', location=(y * 60, my_map.rows * 60 - x * 60))
    elif room[x][y].get_pillar() == "Encapsulation":
        window['Graph'].draw_image(filename='images/E.png', location=(y * 60, my_map.rows * 60 - x * 60))
    elif room[x][y].get_pillar() == "Inheritance":
        window['Graph'].draw_image(filename='images/I.png', location=(y * 60, my_map.rows * 60 - x * 60))
    elif room[x][y].get_pillar() == "Polymorphism":
        window['Graph'].draw_image(filename='images/P.png', location=(y * 60, my_map.rows * 60 - x * 60))


def dungeon_adventure_event_checker(my_map, window, ad):
    """
    Method is used to check event and move the warrior.
    :return:
    """
    current_x = random.randint(0, my_map.rows - 1)
    current_y = random.randint(0, my_map.cols - 1)
    draw_image(current_x, current_y, my_map, window)
    window['Graph'].draw_image(filename='images/Huntress.png',
                               location=(current_y * 60, my_map.rows * 60 - current_x * 60))  # 60 * x
    while True:
        room = my_map.get_room()
        event, values = window.read()
        old_x = current_x
        old_y = current_y
        if room[current_x][current_y].north and checkEvents(event) == 'Up' and current_x - 1 >= 0:
            current_x = current_x - 1
        elif room[current_x][current_y].south and checkEvents(
                event) == 'Down' and current_x + 1 < my_map.cols:
            current_x = current_x + 1
        elif room[current_x][current_y].west and checkEvents(event) == 'Left' and current_y - 1 >= 0:
            current_y = current_y - 1
        elif room[current_x][current_y].east and checkEvents(
                event) == 'Right' and current_y + 1 < my_map.rows:
            current_y = current_y + 1
        elif ad.get_vision_potion() > 0 and checkEvents(event) == 'V':
            ad.use_vision_potion()
            window['-P4-'].update('Vision potion: ' + str(ad._number_vision_potions))
            draw_image(current_x, current_y + 1, my_map, window)
            draw_image(current_x, current_y - 1, my_map, window)
            draw_image(current_x + 1, current_y, my_map, window)
            draw_image(current_x - 1, current_y, my_map, window)
            draw_image(current_x + 1, current_y + 1, my_map, window)
            draw_image(current_x - 1, current_y + 1, my_map, window)
            draw_image(current_x + 1, current_y - 1, my_map, window)
            draw_image(current_x - 1, current_y - 1, my_map, window)
        elif ad.get_healing_potion() > 0 and checkEvents(event) == 'H':
            ad.use_healing_potion()
            window['-P2-'].update('Hit point: ' + str(ad.hit_point))
            window['-P3-'].update('Healing potion: ' + str(ad._number_healing_potions))
        draw_image(current_x, current_y, my_map, window)
        window['Graph'].draw_image(filename='images/Huntress.png',
                                   location=(current_y * 60, my_map.rows * 60 - current_x * 60))
        if room[current_x][current_y].get_pit():
            ad.damage_by_pit()
            window['-P2-'].update('Hit point: ' + str(ad.hit_point))
        if room[current_x][current_y].get_health_potion() and room[current_x][current_y].get_vision_potion():
            ad.add_vision_potion()
            ad.add_healing_potion()
            window['-P3-'].update('Healing potion: ' + str(ad._number_healing_potions))
            window['-P4-'].update('Vision potion: ' + str(ad._number_vision_potions))
            room[current_x][current_y].set_vision_potion(False)
            room[current_x][current_y].set_health_potion(False)
        elif room[current_x][current_y].get_health_potion():
            ad.add_healing_potion()
            window['-P3-'].update('Healing potion: ' + str(ad._number_healing_potions))
            room[current_x][current_y].set_health_potion(False)
        elif room[current_x][current_y].get_vision_potion():
            ad.add_vision_potion()
            window['-P4-'].update('Vision potion: ' + str(ad._number_vision_potions))
            room[current_x][current_y].set_vision_potion(False)
        if room[current_x][current_y].get_pillar() == "Abstraction":
            ad.pillar_A = True
            window['-P6-'].update("Abstraction")
            room[current_x][current_y].set_pillar("No pillar")
        elif room[current_x][current_y].get_pillar() == "Encapsulation":
            ad.pillar_E = True
            window['-P7-'].update("Encapsulation")
            room[current_x][current_y].set_pillar("No pillar")
        elif room[current_x][current_y].get_pillar() == "Inheritance":
            ad.pillar_I = True
            window['-P8-'].update("Inheritance")
            room[current_x][current_y].set_pillar("No pillar")
        elif room[current_x][current_y].get_pillar() == "Polymorphism":
            ad.pillar_P = True
            window['-P9-'].update("Polymorphism")
            room[current_x][current_y].set_pillar("No pillar")
        if old_x != current_x or old_y != current_y:
            draw_image(old_x, old_y, my_map, window)
        if ad.hit_point <= 0:
            window['-P10-'].update("You lose !", font='Any 16', text_color='red')
            draw_all_image(my_map, window)
        if ad.pillar_A and ad.pillar_E and ad.pillar_I and ad.pillar_P and my_map.get_room()[current_x][
            current_y].get_exit() and ad.hit_point > 0:
            window['-P10-'].update("You Win !", font='Any 16', text_color='green')
            draw_all_image(my_map, window)
        if event == 'Re-play':
            window['Graph'].erase()
            my_map = init_games(my_map.rows)
            ad.set_hit_point()
            ad.set_number_healing_potions(1)
            ad.set_number_vision_potions(1)
            ad.reset_all_pillar()
            current_x = random.randint(0, my_map.rows - 1)
            current_y = random.randint(0, my_map.cols - 1)
            draw_image(current_x, current_y, my_map, window)
            window['Graph'].draw_image(filename='images/Huntress.png',
                                       location=(current_y * 60, my_map.rows * 60 - current_x * 60))
            window['-P2-'].update('Hit point: ' + str(ad.hit_point))
            window['-P3-'].update('Healing potion: ' + str(ad._number_healing_potions))
            window['-P4-'].update('Vision potion: ' + str(ad._number_vision_potions))
            window['-P6-'].update('')
            window['-P7-'].update('')
            window['-P8-'].update('')
            window['-P9-'].update('')
            window['-P10-'].update('')
        if checkEvents(event) == 'W':
            draw_all_image(my_map, window)
        if event == psg.WIN_CLOSED:
            break
    window.close()


def draw_all_image(my_map, window):
    for i in range(my_map.rows):
        for j in range(my_map.cols):
            draw_image(i, j, my_map, window)


if __name__ == "__main__":
    dungeon_adventrue_test()
