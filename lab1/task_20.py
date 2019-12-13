#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
	for i in range(11):
		if i%2 == 0:
			for j in range(26):
				move_left(n=1)
				fill_cell()
			move_down(n=1)
		else:
			for j in range(26):
				move_right(n=1):
					fill_cell()
			move_down(n=1)
    pass


if __name__ == '__main__':
    run_tasks()
