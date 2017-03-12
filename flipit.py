import sys
flipper = sys.argv[1]

f = open(flipper,"r+")
file_text = f.readlines()
f.write("\n\nYour bits have been flipped!\n")

def flipping_fantastic(dec_str):
	for num in dec_str:
		if num != "\n":
			b = format(int(num),'b').replace("0","2").replace("1","0").replace("2","1")
			b = str(int(b,2)) + "\n"
			f.write(b)


flipping_fantastic(file_text)
f.close()