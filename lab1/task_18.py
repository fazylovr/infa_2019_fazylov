#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
	while wall_is_above() == true:
		move_left(n=1)
	while wall_is_above() == false:
		move_up(n=1)
	whilve wall_is_left() == false:
		move_left()
    pass


if __name__ == '__main__':
    run_tasks()
