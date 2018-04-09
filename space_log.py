#!/usr/bin/env python3
#
# Use like `./space_log.py -s|-p|-t|-d|-f log_file

from sys import argv
import fuel
import lightYears

# Opens the log file and grabs the contents.
try:
	fh = open(argv[1], 'r')
	content = fh.read()
	fh.close()
except IndexError:
	exit("Missing name of log file.")
except:
	exit("Couldn't open file \""+sys.argv[1]+"\".")

# Uncomment, and add your work in the appropriate spots.
argSwitcher = {
#	'-s': NAMES OF SYSTEMS VISITED
#	'-p': NAMES OF PLANETS SCANNED
#	'-t': TOTAL NUMBER OF TERRAFORMABLE PLANETS SCANNED
	'-d': lightYears.get_total_distance
	'-f': fuel.get_total_fuel,	# The example.
}

try:
	func = argSwitcher.get(argv[2], lambda x: "Incorrect search argument.")
except IndexError:
	exit("Missing search argument.")

print(func(content))
