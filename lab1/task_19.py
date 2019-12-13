#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_29():
	while wall_is_on_the_left() == false:
		move_left(n=1)
		if wall_is_above() == false:
			while wall_is_above() == false:
				move_up(n=1)
		else:
			while wall_is_on_the_right() == false:
				move_right(n=1)
			if wall_is_above() == false:
				while wall_is_above() == false:
					move_up()
				while wall_is_on_the_left() == false:
					move_left(n=1)
    pass


if __name__ == '__main__':
    run_tasks()
