import webbrowser
help(webbrowser)
chrome = webbrowser.get(using="google-chrome")
chrome.open_new("https://www.python.org")

# webbrowser.open("https://www.python.org")
# print

for i in range(2,20,2):
	print(i,i,sep='|',end=';')