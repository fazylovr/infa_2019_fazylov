#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_3():
	while wall_is_on_the_right() == false:
		while wall_is_on_the_up() == true or wall_is_on_the_down() == true:
			if cell_is_fill() == false:
				fill_cell()
		move_right(n=1)
    pass


if __name__ == '__main__':
    run_tasks()
