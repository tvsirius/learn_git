from task1 import House

h1 = House('Dom1')
h2 = House('Nord', 10)

print(h1)
print(h2)

h2.hot(True)
h1.cond(True)

print(h1)
print(h2)

h3 = House('Dom2')
h4 = House('Afrika', 60)
h4.hot()
h3.cond()
print(h1, h2, h3, h4)

print('hello git')
