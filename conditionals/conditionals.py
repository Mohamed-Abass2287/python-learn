num1, num2 = 90, 123

if num1 < num2:
	print(f"Sure {num1} is less than {num2}")
elif num1 == num2:
	print(f"Sure {num1} is equal to {num2}")
else:
	print(f"{num1} is greater than {num2}")

if num1 < num2:
	if num1 == 90:
		print(f"{num1} is less than {num2} and it is 90")
	elif num1 < 100:
		print(f"{num1} is less than {num2} and also less than 100")
	
	else:
		print(f"{num1} is less than {num2} but greater than 100")
elif num1 == num2:
	print(f"Sure {num1} is equal to {num2}")
else:
	print(f"{num1} is greater than {num2}")

sentence = '''This is some random sentence I have just written.
It is in the JS file.
'''

if "have" in sentence:
	print("The word 'have' is in the sentence")

if "monumental" not in sentence:
	print("The word 'monumental' is not in the sentence")

if len(sentence) > 10:
	print("This is a very long sentence!!")

print("This is an extremely long sentence!!") if len(sentence) > 10 else print("Goddamn!")

if len(sentence) > 1000 or len(sentence) > 10:
	print("This is a veeeeery long sentence!!")