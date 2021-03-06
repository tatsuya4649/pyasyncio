#!/bin/env python

import asyncio
import time

def f(tag):
	for _ in range(3):
		yield
		time.sleep(1)
		print(f"{tag}")
	return f"hello {tag}"

loop = asyncio.get_event_loop()
tasks = []
for tag in range(3):
	# return generator
	task = f(tag)
	print(task)
	tasks += [task]
# exec in order for `tasks`
# so ... output
# 0
# 1
# 2
# 0
# 1
# 2
# 0
# 1
# 2
res = loop.run_until_complete(asyncio.gather(*tasks))
print(res)
