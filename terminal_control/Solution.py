#!/usr/bin/python3

import curses
from picar import back_wheels, front_wheels
from time import sleep

# get the curses screen window
screen = curses.initscr()
# turn off input echoing
curses.noecho()
# respond to keys immediately (don't wait for enter)
curses.cbreak()
# map arrow keys to special values
screen.keypad(True)

fw = front_wheels.Front_Wheels(debug=False)
bw = back_wheels.Back_Wheels(debug=False)
bw.ready()
fw.ready()

global SPEED 
SPEED=60
global bw_status
bw_status=0

steering=0
direction=0

try:
    while True:
        char = screen.getch()

        ## Control steering left and rights

        if steering == 0 and char == curses.KEY_RIGHT:
            screen.addstr(0, 0, 'right')
            fw.turn_right()
            steering = 1
        elif steering == 0 and char == curses.KEY_LEFT:
            screen.addstr(0, 0, 'left ')
            fw.turn_left()
            steering = -1
        elif (steering == -1 and char == curses.KEY_RIGHT) or (steering == 1 and char == curses.KEY_LEFT):
            screen.addstr(0, 0, 'straight ')
            fw.turn_straight()
            steering = 0

        # control forward / back
        if char == curses.KEY_UP and bw_status == 0:
            screen.addstr(0, 0, 'up   ')
            bw.speed = SPEED
            bw.forward()
            bw_status = 1
            debug = "speed =", SPEED
        elif char == curses.KEY_DOWN and bw_status == 0:
            screen.addstr(0, 0, 'up   ')
            bw.speed = SPEED
            bw.backward()
            bw_status = -1
        elif (char == curses.KEY_UP and bw_status == -1) or (char == curses.KEY_DOWN and bw_status == 1):
            screen.addstr(0, 0, 'stop   ')
            bw.stop()
            bw_status = 0


finally:
    # shut down cleanly
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()