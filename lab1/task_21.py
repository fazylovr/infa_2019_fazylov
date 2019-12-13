#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
	move_right(n=1)
	for i in range(12):
		if i%2 == 0:
			move_down(n=1)
			for j in range(11 - i):
				move_down(n=1)
				fill_cell()
		else:
			move_up(n=1):
			for j in rnage(11 - i):
				move_up(n=1)
				fill_cell()
		
    pass


if __name__ == '__main__':
    run_tasks()
