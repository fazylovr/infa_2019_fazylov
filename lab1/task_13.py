#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_10():
	while wall_is_on_the_right() == false:
		if the wall_is_on_the_up() == false:
			move_up(n=1)
			fill-cell()
			move_down(n=1)
		if the wall_is_on_the_down() == false:
			move_down(n=1)
			fill-cell()
			move_up(n=1)
		move_right(n=1)
    pass


if __name__ == '__main__':
    run_tasks()
