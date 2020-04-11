import random
import re
import time

MIN_COLOR_CODE = 0
MAX_COLOR_CODE = 255
DELAY_TIME = 0.5


def get_planets(file_name):
    with open(file_name, 'r') as f:
        raw_planets = f.read()
    planets = re.split('\n\n', raw_planets)
    return planets


def clear_planet(planet):
    planet_height = len(planet.split("\n"))
    move_cursor_up_seq = f"\u001b[{planet_height}A]"
    clear_screen_seq = "\033[2J"
    print(move_cursor_up_seq + "\n" + clear_screen_seq, end='')


def change_color_randomly():
    random_color_code = random.randrange(MIN_COLOR_CODE, MAX_COLOR_CODE)
    print(f"\u001b[38;5;{random_color_code}m", end='')


def draw_planets(planets):
    for planet in planets:
        change_color_randomly()
        print(planet, end="")
        time.sleep(DELAY_TIME)
        clear_planet(planet)


def main():
    planets = get_planets('planets.txt')
    draw_planets(planets)
    print("THE END")


if __name__ == '__main__':
    main()
