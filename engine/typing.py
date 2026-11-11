import curses
import math
import time


def main(stdscr, words):
    global x, y
    # Clear the screen to start fresh
    # stdscr.clear()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    # Get screen dimensions (rows, cols)
    height, width = stdscr.getmaxyx()

    # useful info
    stdscr.addstr(1, int(math.floor(width / 2)) - 10, "Press <Tab> to restart")
    stdscr.addstr(2, int(math.floor(width / 2)) - 9, "Press <Esc> to exit")
    stdscr.refresh()

    # Make new window for textbox
    textbox = curses.newwin(height - 20, width - 10, 15, 5)
    textbox.attron(curses.color_pair(1))
    textbox.border()
    textbox.attroff(curses.color_pair(1))

    textbox.addstr(1, 1, words)
    textbox.move(1, 1)
    usr_words = ""
    textbox.refresh()

    x = 1
    y = 1

    key = textbox.getch()
    start = time.time()

    if key == 27:
        exit(0)
    if key == curses.KEY_BACKSPACE or key == 127:
        x -= 1
        textbox.move(y, x)
        textbox.addch(y, x, words[x - 1], curses.color_pair(3))
    elif 32 <= key <= 126:  # Printable characters
        textbox.addch(y, x, chr(key), curses.color_pair(1))
        x += 1
        textbox.move(y, x)

    while 1:
        key = textbox.getch()

        if key == 9:
            return 0, 0
        if key == 27:
            exit(0)
        elif key == curses.KEY_BACKSPACE or key == 127:
            x -= 1
            textbox.move(y, x)
            textbox.addch(y, x, words[x - 1], curses.color_pair(3))
        elif 32 <= key <= 126:  # Printable characters
            if str(chr(key)) == words[x - 1]:
                textbox.addch(y, x, chr(key), curses.color_pair(1))
            if str(chr(key)) != words[x - 1]:
                textbox.addch(y, x, chr(key), curses.color_pair(2))
            x += 1
            textbox.move(y, x)
        if x - 1 >= len(words):
            for i in range(len(words)):
                char = str(chr(textbox.inch(1, 1 + i) & curses.A_CHARTEXT))
                usr_words += char
            end = time.time()
            break
        stdscr.refresh()

    elapsed_time = end - start

    return usr_words, elapsed_time

    # Refresh the screen to display changes
    stdscr.refresh()


# curses.wrapper handles setup and automatic terminal reset on exit
x = 1
y = 1


def init(words):
    return curses.wrapper(main, words)
