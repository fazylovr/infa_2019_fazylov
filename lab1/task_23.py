#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
	while wall_is_on_the_right() == true:
		if wall_is_above() == false:
			while wall_is_above() == false:
				move_up(n=1)
				fill_cell()
			move_right(n=1)
				while wall_is_beneath() == true:
					fill_cell()
					move_down(n=1)
		move_right(n=1)
    pass


if __name__ == '__main__':
    run_tasks()
