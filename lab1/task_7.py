#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
	while wall_is_on_the_down() == false:
		move_down(n=1)
	while wall_is_on_the_down() == true:
		move_right(n=1)
	move_down(n=1)
	while wall_is_on_the_left() == false:
		move_left(n=1)
    pass


if __name__ == '__main__':
    run_tasks()
