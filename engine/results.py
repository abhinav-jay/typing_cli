import curses
import math
import time


def main(stdscr, accuracy, wpm):
    if accuracy == 0:
        return None
    # Clear the screen to start fresh
    # stdscr.clear()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    # Get screen dimensions (rows, cols)
    height, width = stdscr.getmaxyx()

    # useful information
    stdscr.addstr(1, int(math.floor(width / 2)) - 10, "Press <Tab> to restart")
    stdscr.addstr(2, int(math.floor(width / 2)) - 9, "Press <Esc> to exit")
    stdscr.addstr(10, int(math.floor(width / 2)) - 5, "Typing test")

    # Make new window for accuracy
    accuracywin = curses.newwin(
        height - 20, int(math.floor((width - 10) / 2)) - 2, 15, 5
    )
    accuracywin.attron(curses.color_pair(1))
    accuracywin.border()

    accuracywin.addstr(0, 2, "Accuracy")
    accuracywin.attroff(curses.color_pair(1))
    accuracywin.addstr(5, 5, accuracy)
    accuracywin.refresh()

    # Make new window for speed
    speedwin = curses.newwin(
        height - 20,
        int(math.floor((width - 10) / 2)) - 2,
        15,
        int(math.floor(width / 2)) + 2,
    )
    speedwin.attron(curses.color_pair(1))
    speedwin.border()

    speedwin.addstr(0, 2, "WPM")
    speedwin.attroff(curses.color_pair(1))
    speedwin.addstr(5, 5, str(wpm) + " WPM speed")
    speedwin.refresh()

    # wait keypress before exit
    key = stdscr.getch()
    if key == 27:
        exit(0)
    # start = time.time()
    # if key == curses.KEY_BACKSPACE or key == 127:
    #     x -= 1
    #     textbox.move(y, x)
    #     textbox.addch(y, x, words[x - 1], curses.color_pair(3))
    # elif 32 <= key <= 126:  # Printable characters
    #     textbox.addch(y, x, chr(key), curses.color_pair(1))
    #     x += 1
    #     textbox.move(y, x)
    #
    # while 1:
    #     key = textbox.getch()
    #     if key == curses.KEY_BACKSPACE or key == 127:
    #         x -= 1
    #         textbox.addch(y, x, words[x - 1], curses.color_pair(3))
    #         textbox.move(y, x)
    #     elif 32 <= key <= 126:  # Printable characters
    #         if str(chr(key)) == words[x - 1]:
    #             textbox.addch(y, x, chr(key), curses.color_pair(1))
    #         if str(chr(key)) != words[x - 1]:
    #             textbox.addch(y, x, chr(key), curses.color_pair(2))
    #         x += 1
    #         textbox.move(y, x)
    #     if x - 1 >= len(words):
    #         for i in range(len(words)):
    #             char = str(chr(textbox.inch(10, 1 + i) & curses.A_CHARTEXT))
    #             usr_words += char
    #         end = time.time()
    #         break
    #
    # elapsed_time = end - start

    # return usr_words, elapsed_time

    # Refresh the screen to display changes
    stdscr.refresh()


# curses.wrapper handles setup and automatic terminal reset on exit


def init(accuracy, wpm):
    return curses.wrapper(main, accuracy, wpm)
