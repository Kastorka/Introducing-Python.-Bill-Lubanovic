# one_marx = 'Groucho',
# print(type(one_marx))
# print(type('Groucho',))
# print(type(('Groucho',)))

# marx_tuple = ('Groucho', 'Chico', 'Harpo')
# a, b, c = marx_tuple
# print(a)

# rows = range(1,4)
# cols = range(1,3)
# cells = [(row, col) for row in rows for col in cols]
# for cell in cells:
#     print(cell)

#homework

years_list = [year for year in range(1989,1995)]
print(years_list)
print(years_list[3])
print(years_list[-1])
tpl = ('mozzarella', 'cinderella', 'salmonella')
things = list(tpl)
print(things)

print(things[1].capitalize())
things[1] = things[1].capitalize()
print(things)
print(things[0].upper())
things[0] = things[0].upper()
print(things)
things.pop()
print(things)
surprise = 'Groucho, Chico, Harpo'
surprise = surprise.split(', ')
print(surprise)
# surprise[-1] = surprise[-1].lower()
# surprise.sort(reverse=True)
# surprise[0] = surprise[0].capitalize()
# print(surprise)
surprise[-1] = surprise[-1].lower()[::-1].capitalize()
# surprise[-1] = surprise[-1][::-1]
# surprise[-1] = surprise[-1].capitalize()
print(surprise)
even = [number for number in range(10)]
print(even)

start1 = ["fee", "fie", "foe"]
rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done"),
    ]
start2 = "Someone better"
start1_caps = " ".join([word.capitalize() + "!" for word in start1])
for first, second in rhymes:
    print(f"{start1_caps} {first.capitalize()}!")
    print(f"{start2} {second}.")