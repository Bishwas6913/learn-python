poem = """All that doth flows we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt"""

# print(poem)

one_3 = poem[:13]

print(one_3)

poem_len = len(poem)

print(poem_len)

poem_startwith = poem.startswith("All")

print(poem_startwith)
# returns a bool value wheater that is in the vatiable or not

poem_endswith = poem.endswith("that/s all folks")

print(poem_endswith)


word = "the"

print(poem.find(word))

print(poem.index(word))
