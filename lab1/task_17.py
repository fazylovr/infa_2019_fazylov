#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_27():
	while cell_is_filled() == false:
		move_up(n=1)
	move_left(n=1)
    pass


if __name__ == '__main__':
    run_tasks()
