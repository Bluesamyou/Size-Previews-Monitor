# base.py
# developer: @eggins

# This gives you a basic understanding of how I set all my new projects up.
# Everything here is what I would use as a base to any python project.

# Please see installation instructions in README for further information
# Coming soon: documentation on every line to show how everything is being done

# initialise all libraries that are needed
import time, json, requests, random, colorama, threading
from time import sleep



# custom coded libraries
from classes.logger import logger
log = logger().log

# if you plan on using this script, please dont delete the below line
log("[@eggins] PyBase initalised. (github.com/eggins/pybase)", "info")
# if you plan on using this script, please dont delete the above line

# the below functions are all of the colours that are able to be used
# from within the logger functions

log("", showtime=False)
log("Success message w/ time", "success", "success.txt")
log("Success message w/ time", "success", nocolor="and tailing information")
log("Success message without time", "success", nocolor="and tailing information", showtime=False)

log("", showtime=False)
log("Error message w/ time", "error")
log("Error message w/ time", "error", nocolor="and tailing information")
log("Error message without time", "error", nocolor="and tailing information", showtime=False)

log("", showtime=False)
log("Info message w/ time", "info")
log("Info message w/ time", "info", nocolor="and tailing information")
log("Info message without time", "info", nocolor="and tailing information", showtime=False)

log("", showtime=False)
log("Debug message w/ time", "debug")
log("Debug message w/ time", "debug", nocolor="and tailing information")
log("Debug message without time", "debug", nocolor="and tailing information", showtime=False)

log("", showtime=False)
log("Default message w/ time")
log("Default message w/ time", nocolor="and tailing information")
log("Default message without time", nocolor="and tailing information", showtime=False)