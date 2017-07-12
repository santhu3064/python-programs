def python_function():
	width=80
	text="Spam "
	left_margin=(width - len(text))//2
	print (" " * left_margin,text)

def centre_text(text):
	left_margin=(80 - len(str(text)))//2
	print (" " * left_margin,text)

def centre_text_var_1(*texts):
	text = ""
	for x in texts:
		text = str(x) + " "
	left_margin=(80 - len(str(text)))//2
	print (" " * left_margin,text)

def centre_text_var(*texts,sep=' ',end = "\n",file=None,flush=False):
	text = ""
	for x in texts:
		text += str(x) + sep
	left_margin=(80 - len(str(text)))//2
	print (" " * left_margin,text,end=end,file=file,flush=flush)

#storing in file
with open("centeredfile","w") as centered_file:
	python_function()
	centre_text(10)
	centre_text("spam spam spam spam")
	centre_text_var("hello",45,"Hw are  you",sep=':',file=centered_file)

#uisng return
def centre_text_var2(*texts,sep=' '):
	text = ""
	for x in texts:
		text += str(x) + sep
	left_margin=(80 - len(str(text)))//2
	return " " * left_margin + text
with open("menu","w" ) as menu:
	S1=centre_text_var2("hello",345,"Hw are  you",sep=':')
	print (S1,file=menu)
	print(centre_text_var2("12"),file=menu)