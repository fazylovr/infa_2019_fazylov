#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_22():
	while wall_is_on_the_left() == true and wall_is_on_the_right() == true:
		move_up(n=1)
	if wall_is_on_the_left() == true
		while wall_is_on_the_left() == false:
			move_left(n=1)
	if wall_is_on_the_right() == true
		while wall_is_on_the_right() == false:
			move_right(n=1)
    pass


if __name__ == '__main__':
    run_tasks()
