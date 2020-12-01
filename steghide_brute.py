from itertools import product
from argparse import ArgumentParser
import commands
import os
import time
import sys

VERSION = "1.0"

passwordTest = ['a']
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def check_file(file):
	if os.path.exists(file):
		return True
	else:
		return False

def bruteBoy(imgFile, count):
	ofile = "info_" + imgFile.split('.')[0] + ".txt"
	while(True):
		for combine in product(letters, repeat=len(passwordTest)):
			count += 1
			combine = ''.join(combine)
			r = commands.getoutput("yes | steghide extract -sf %s -p '%s' -xf %s" % (imgFile, combine, ofile))
			print("Last Attempt:" + combine)

			if not "no pude extraer" in r and not "could not extract" in r:
				print("\n\n [+] " + "Information obtained with password:" + str(combine))
				if check_file(ofile):
					with open(ofile, 'r+') as outfile:
						for line in outfile.readlines():
							print(line)
				sys.exit()
		passwordTest.append('a')
def main(count):
	argp = ArgumentParser(
		description="Steghide New Brute",
		usage="python new_brute.py [-f image_file]",
		version="New Brute Force Tool v" + VERSION)
	argp.add_argument('-f', '--file', dest='file', required=True, help='Path of File')
	
	args = argp.parse_args()

	bruteBoy(args.file, count)

if __name__ == "__main__":
	start_time = time.time()
	count = 0
	main(count)
	print("---%s combinations tried in  %s minutes ---" % ((str(count), (time.time() - start_time)/ 60)))
