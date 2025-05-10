# display_manager_terminal.py

import curses
import time

def show_message(stdscr, text, duration=2):
    stdscr.clear()
    lines = text.split('\n')
    h, w = stdscr.getmaxyx()
    for idx, line in enumerate(lines):
        x = (w - len(line)) // 2
        y = (h // 2 - len(lines)//2) + idx
        stdscr.addstr(y, x, line)
    stdscr.refresh()
    time.sleep(duration)

def show_launch_animation(stdscr, frames=10, speed=0.2):
    h, w = stdscr.getmaxyx()
    rocket = ["  ^  ",
              " /|\\ ",
              "/_|_\\"]
    for i in range(frames):
        stdscr.clear()
        offset = int((i/frames)*(h + len(rocket)))
        y = h - offset
        for j, line in enumerate(rocket):
            if 0 <= y+j < h:
                x = (w - len(line)) // 2
                stdscr.addstr(y+j, x, line)
        stdscr.refresh()
        time.sleep(speed)
    time.sleep(1)

def main():
    curses.wrapper(run)

def run(stdscr):
    # Initialisierung
    curses.curs_set(0)
    stdscr.nodelay(False)

    # Demo
    show_message(stdscr, "Test: Willkommen an Bord", 2)
    show_launch_animation(stdscr)
    show_message(stdscr, "Test beendet", 2)

if __name__ == "__main__":
    main()
