#!/usr/bin/env python3

import sys
import os


def main():
	# Read file
	filename = 'sample.feature'
	path_to_file = 'Tracking-Test-Cases/data/'

	if not os.path.exists(path_to_file):
		print("The path doesn't exist")
		return

	os.chdir(path_to_file)

	try:
		with open(filename) as test_file:
			for line_count, line in enumerate(test_file):
				stripped_line = line.strip('\n \t')
				if stripped_line != '':
					print("Line {}: {}".format(line_count, stripped_line))
	except IOError as error:
		print("An error occurred: {}".format(str(error)))


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("Exiting the system")
		sys.exit(0)
