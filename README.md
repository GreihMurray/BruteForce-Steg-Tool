# BruteForce-Steg-Tool
Uses steghide tool to brute force passwords by trying every combination of letters until finding the proper password. For longer passwords, has a long run time

Loosely based on Steghide-Brute-Force-Tool

# How to Use
Clone the repository, or just the file then navigate your terminal or command prompt to the location of the file.

Use the below command outline to craft your commands

python new_brute.py -f <PATH TO IMAGE FILE>
  
  -f : Path to image file which has embedded data 
  
Will output each attempt as the attempt is made and after finding the password will output the embedded data and the password used to the console.
