import curses
import time

def main(stdscr, words):
    global x, y
    # Clear the screen to start fresh
    stdscr.clear()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    # Get screen dimensions (rows, cols)
    height, width = stdscr.getmaxyx()

    text = words
    stdscr.addstr(10, 5, words)
    stdscr.move(y, x)
    usr_words = ""

    key = stdscr.getch()
    start = time.time()
    if key == curses.KEY_BACKSPACE or key == 127:
        x -= 1
        stdscr.move(y, x)
        stdscr.addch(y, x, words[x-5], curses.color_pair(3))
    elif 32 <= key <= 126:  # Printable characters
        stdscr.addch(y, x, chr(key), curses.color_pair(1))
        x += 1
        stdscr.move(y, x)

    while 1:
        key = stdscr.getch()
        if key == curses.KEY_BACKSPACE or key == 127:
            x -= 1
            stdscr.addch(y, x, words[x-5], curses.color_pair(3))
            stdscr.move(y, x)
        elif 32 <= key <= 126:  # Printable characters
            if str(chr(key)) == words[x-5]:
                stdscr.addch(y, x, chr(key), curses.color_pair(1))
            if str(chr(key)) != words[x-5]:
                stdscr.addch(y, x, chr(key), curses.color_pair(2))
            x += 1
            stdscr.move(y, x)
        if x - 5 >= len(words):
            for i in range(len(words)):
                char = str(chr(stdscr.inch(10, 5 + i) & curses.A_CHARTEXT))
                usr_words += char
            end = time.time()
            break

    elapsed_time = end-start

    return usr_words, elapsed_time


    # Refresh the screen to display changes
    stdscr.refresh()


# curses.wrapper handles setup and automatic terminal reset on exit
x = 5
y = 10

def init(words):
    return curses.wrapper(main, words)
