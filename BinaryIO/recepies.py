# import shelve
# blt=["bacon","lettuce","tomato","bread"]
# beans_on_toast=["beans","bread"]
# scrambled_eggs=["eggs","butter","milk"]
# soup=["tin of soup"]
# pasta=["pasta","cheese"]
#
# with shelve.open("recepies") as recepies:
# 	recepies["blt"]=blt
# 	recepies["bean_on _toast"]=beans_on_toast
# 	recepies["scrambled_eggs"]=scrambled_eggs
# 	recepies["soup"]=soup
# 	recepies["pasta"]=pasta
# 	recepies["blt"].append("butter")
# 	temp_list=list(recepies["blt"])
# 	temp_list.append("butter")
# 	recepies["blt"]=temp_list
# 	for i in recepies:
# 		print(i , recepies[i])

import shelve
blt=["bacon","lettuce","tomato","bread"]
beans_on_toast=["beans","bread"]
scrambled_eggs=["eggs","butter","milk"]
soup=["tin of soup"]
pasta=["pasta","cheese"]

with shelve.open("recepies",writeback=True) as recepies:
	recepies["blt"]=blt
	recepies["bean_on _toast"]=beans_on_toast
	recepies["scrambled_eggs"]=scrambled_eggs
	recepies["soup"]=soup
	recepies["pasta"]=pasta
	recepies["blt"].append("biscuit")
	for i in recepies:
		print(i , recepies[i])