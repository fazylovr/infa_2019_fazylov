#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
	k = 0
	while wall_is_beneath() == false:
		fill_cell()
		move_down(n=1)
		k += 1
	for i in range(k-2):
		move_right(n=1)
		if k%2 == 0:
			fill_cell(n=1)
			move_up(n=1)
		else:
			fill_cell()
			move_down(n=1)
    pass


if __name__ == '__main__':
    run_tasks()
