import shelve
with shelve.open("fruitsdesc") as fruit:
	fruit["grape"] = "Grape is  sweet fruit in bunches"
	fruit["apple"] = "apple is red in colour and sweet"
	fruit["banana"] = "banana fruit fir fast revive"
	fruit["orange"] = "Orange is a citrus fruit"
	fruit["pomegranate"] = "pomegranate fruit with red sweets"
	print (fruit["grape"])
	print (fruit["orange"])
	fruit["guava"] ="Good for health"
	for key in fruit:
		print(key)
	while True:
		fruit_key=input("Please enter a fruit \n").lower()
		if fruit_key == "quit":
			break
		description=fruit.get(fruit_key,"we dont ahve the fruit " + fruit_key + " that you entered")
		print (description)