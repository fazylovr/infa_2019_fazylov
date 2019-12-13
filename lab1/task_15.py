#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
	if wall_is_on_the_left() == true:
		move_right(n=9)
		if wall_is_above == true:
			move_down(n=9)
		if wall_is_beneath() == true:
			move_up(n=9)
	else:
		move_left(n=9):
		if wall_is_above == true:
			move_down(n=9)
		if wall_is_beneath() == true:
			move_up(n=9)
			
    pass


if __name__ == '__main__':
    run_tasks()
