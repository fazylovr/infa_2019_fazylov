#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_11():
	while wall_is_on_the_right() == false:
		if the wall_is_above() == false:
			move_up(n=1)
			fill-cell()
			move_down(n=1)
		if the wall_is_beneath() == false:
			move_down(n=1)
			fill-cell()
			move_up(n=1)
		if the wall_is_beneath() == true and the_wall_is_above() == true:
			fill-cell()
		move_right(n=1)
    pass


if __name__ == '__main__':
    run_tasks()
