from itertools import product
from argparse import ArgumentParser
import commands
import os
import time
import sys

VERSION = "1.0"

#Declaring the array to use to pull letters from, and the array to use to create letter combinations
passwordTest = ['a']
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#checks to see if a file exists
def check_file(file):
	if os.path.exists(file):
		return True
	else:
		return False

#Runs the steghide command with each letter combination
def bruteBoy(imgFile, count, start_time):
	ofile = "info_" + imgFile.split('.')[0] + ".txt"
	while(True):
		#Runs through every possible combination of the letters in letters array, starting with A and progressing to 26 Zs
		for combine in product(letters, repeat=len(passwordTest)):
			count += 1
			#Combines all letters in passwordTest array
			combine = ''.join(combine)
			#Runs steghide command with the current password to test and prints the password to the console
			r = commands.getoutput("yes | steghide extract -sf %s -p '%s' -xf %s" % (imgFile, combine, ofile))
			print("Last Attempt:" + combine)

			#Checks result from steghide command and if successful reads data from the output file and prints to the console
			if not "no pude extraer" in r and not "could not extract" in r:
				print("\n\n [+] " + "Information obtained with password:" + str(combine))
				if check_file(ofile):
					with open(ofile, 'r+') as outfile:
						for line in outfile.readlines():
							print(line)
				print("---%s combinations tried in  %s minutes ---" % ((str(count), (time.time() - start_time) / 60)))
				sys.exit()
		#Appends an additional A to passwordTest to increase the number of letters in the combinations that are tried
		passwordTest.append('a')

def main(count, start_time):
	#Parses the arguments from the command line
	argp = ArgumentParser(
		description="Steghide New Brute",
		usage="python new_brute.py [-f image_file]",
		version="New Brute Force Tool v" + VERSION)
	argp.add_argument('-f', '--file', dest='file', required=True, help='Path of File')
	
	args = argp.parse_args()

	#Calls bruteboy
	bruteBoy(args.file, count, start_time)

#Starts off the program, grabs the time at the start, and calculates the total time taken to run
if __name__ == "__main__":
	start_time = time.time()
	count = 0
	main(count, start_time)
