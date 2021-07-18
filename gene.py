#!/bin/env python

def gener():
	for i in range(3):
		yield i
	return "hello world"
def genera():
	a = yield from gener()
	return a

gg = gener().__iter__()
print(gg)
print(gg.__next__())
print(gg.__next__())
print(gg.__next__())
try:
	print(gg.__next__())
except StopIteration as e:
	print(e.value)

gg = genera().__iter__()
print(genera)
print(gg)
print(gg.__next__())
print(gg.__next__())
print(gg.__next__())
try:
	print(gg.__next__())
except StopIteration as e:
	print(e.value)
