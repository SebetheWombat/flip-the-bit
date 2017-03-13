#TODO: pack those bits!
import sys

#Inform user they did it wrong
if len(sys.argv) != 2:
	print("\nDirections:")
	print("Please make sure to enter the path for the file you wish to change.")
	print("Use: flipit.py /path/to/file.txt\n")
	sys.exit()

#Set flipper to file path
flipper = sys.argv[1]

#Open file for both reading and writing
f = open(flipper,"r+")
file_text = f.readlines()

f.write("\n\nYour bits have been flipped!\n\n")

#0s to 1s, 1s to 0s
def flipping_fantastic(digit):
	b = format(int(digit),'b').replace("0","2").replace("1","0").replace("2","1")
	b = str(int(b,2))
	return b

#Extract integers from file and send them to have their bits flipped. Re-write them to file.
for sentence in file_text:
	flipped = ""
	for word in sentence.split():
		if word.isdigit():
			word = flipping_fantastic(word)
		flipped += word + " "
	f.write(flipped + "\n")

#Because it's nice to get feedback
print("Done! Go check out your file!")

#We're done with you now
f.close()