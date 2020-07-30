import sys, time, os
from random import randint
import curses

stdscr = curses.initscr()

red = "\033[91m"
bold = "\033[1m"
end = "\033[0m"

curses.start_color()
for i in range(1, 16):
    curses.init_pair(i, i, i + 2)
curses.init_pair(16, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(17, curses.COLOR_WHITE, curses.COLOR_BLACK)

skull2 = {
    "top": f"""      .ed"'"' "'"\$$$$be.
     -"           ^""**$$$e.
   ."                   '$$$c
  /                      "4$$b
 d  3                      $$$$
 $  *                   .$$$$$$
.$  ^c           $$$$$e$$$$$$$$.
d$L  4.         4$$$$$$$$$$$$$$b
$$$$b ^ceeeee.  4$$ECL.F*$$$$$$$
$$$$P d$$$$F $ $$$$$$$$$- $$$$$$
3$$$F "$$O$b   $"$$$$$O$  $$$$*
 $$P"  "$$b   .$ $$$$$...e$$
  *c    ..    $$ 3$$$$$$$$$$eF
    \ce""    $$$  $$$$$$$$$$*
     *$e.    *** d$$$$$"L$$
      $$$      4J$$$$$% $$$
     $"'$=e....$*$$**$cz$$'""".split(
        "\n"
    ),
    "laugh": """     $$$                $$
      $$$             $$$$""".split(
        "\n"
    ),
    "jaw": """     $  *=%4.$ L L$ P3$$$F
     $   "#*ebJLzb$e$$$$$b
      %..      4$$$$$$$$$$
       $$$e   z$$$$$$$$$$
        "*$c  "$$$$$$$P"
          ""'*$$$$$$$'""".split(
        "\n"
    ),
}

creds = ["" for i in range(int(curses.LINES) - 2)]


creditlines = """CREDITS
MMM... TOASTY
BY
BEST NATION SERBIA WARRIORS
WE CREATE HELL FOR CROAT
FUCK TO CROAT SWINE
SERBIA NUMBER 1
HACK SQUAD CHECKMATE 1992
GREETINGS TO:
HACK BABY, DIGITAL MAN 1994, TONY
TRANCE PRINCE, GHOSTWOMAN, BIOHOG, TAD,
FUCK TO CROAT !! IT IS A SHIT TO ME""".split(
    "\n"
)
for i in creditlines:
    creds.append(i)

for i in range(int(curses.LINES / 4)):
    creds.append("")


crack = ["PROGRAM IS CRACK BY", "HACK SQUAD CHECKMATE 1992", "SERBIA BEST NATION"]


def main(stdscr):

    for i in range(curses.LINES - 4):
        color = curses.color_pair(randint(1, 16))
        shit = {
            int((curses.LINES / 2) - 2): "YOU ARE",
            int((curses.LINES) / 2): "MOTHER FUCKER",
        }
        if i in shit:
            value = int(curses.COLS / 2)
            stdscr.addstr(" " * (value - int(len(shit[i]) / 2)), color)
            stdscr.addstr(shit[i], color)
            stdscr.addstr(" " * (value - int(len(shit[i]) / 2)), color)

        else:
            stdscr.addstr(" " * curses.COLS, color)
        stdscr.refresh()
        time.sleep(0.05)
    time.sleep(1)
    stdscr.clear()

    # skull time

    for laughtime in range(20, 0, -1):
        pieces = ["top", "laugh", "jaw"]
        if laughtime % 2 == 0:
            pieces = ["top", "jaw"]
        for piece in pieces:
            for i in skull2[piece]:
                stdscr.addstr(" " * int((curses.COLS / 2) - 16), curses.color_pair(16))
                stdscr.addstr(i, curses.color_pair(16))
                stdscr.addstr("\n", curses.color_pair(16))

        stdscr.refresh()
        time.sleep(0.2)
        if laughtime > 1:
            stdscr.clear()
            continue

        mmm = "Mmmm... Toasty"
        stdscr.addstr("\n", curses.color_pair(17))
        stdscr.addstr(
            " " * int(curses.COLS / 2 - int(len(mmm) / 2)), curses.color_pair(17)
        )
        stdscr.addstr(mmm, curses.color_pair(17))
        stdscr.addstr("\n", curses.color_pair(17))
        stdscr.addstr("\n", curses.color_pair(17))
        stdscr.refresh()
        time.sleep(1)

    for i in crack:
        stdscr.addstr(" " * int((curses.COLS / 2) - len(i) / 2), curses.color_pair(17))
        stdscr.addstr(i, curses.color_pair(17))
        stdscr.addstr("\n", curses.color_pair(17))
        stdscr.refresh()
        time.sleep(0.2)

    time.sleep(5)

    stdscr.clear()
    while len(creds) > 1:
        for i, cred in enumerate(creds):
            if i >= curses.LINES - 4:
                continue
            stdscr.addstr(
                " " * int((curses.COLS / 2) - len(cred) / 2), curses.color_pair(17)
            )
            stdscr.addstr(cred)
            stdscr.addstr("\n")
        stdscr.refresh()
        stdscr.clear()
        creds.pop(0)
        time.sleep(0.45)


curses.wrapper(main)
