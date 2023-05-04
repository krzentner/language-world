


The task `button-press-topdown-wall` requires the robot to push the button down from above with a wall next to it.
To push the button down from above with a wall next to it reliably, what steps the robot should perform?


The task `peg-insert-side-wall` requires the robot to grab the peg and insert it into the hole from the side with a wall next to it.
To grab the peg and insert it into the hole from the side with a wall next to it reliably, what steps the robot should perform?


The task `pick-place-wall` requires the robot to pick up the puck and hold it at the target location with a wall next to it.
To pick up the puck and hold it at the target location with a wall next to it reliably, what steps the robot should perform?


The task `push-wall` requires the robot to slide the puck to the target location with a wall next to it.
To slide the puck to the target location with a wall next to it reliably, what steps the robot should perform?


The task `door-open-wall` requires the robot to pull the door open with a wall next to it.
To pull the door open with a wall next to it reliably, what steps the robot should perform?


The task `window-open-wall` requires the robot to slide the window open to the left with a wall next to it.
To slide the window open to the left with a wall next to it reliably, what steps the robot should perform?


The task `window-close-wall` requires the robot to slide the window closed to the right with a wall next to it.
To slide the window closed to the right with a wall next to it reliably, what steps the robot should perform?


The task `drawer-open-wall` requires the robot to pull the drawer open with a wall next to it.
To pull the drawer open with a wall next to it reliably, what steps the robot should perform?


The task `drawer-close-wall` requires the robot to push the drawer close with a wall next to it.
To push the drawer close with a wall next to it reliably, what steps the robot should perform?"""

def generate_instruction_from_template(template, task_name, steps):
    template_list = template.split('\n')
    instructions = []
    i = 0
    for line in template_list:
        line_words = line.split(' ')
        instruction = ""
        for word in line_words:
            if line_words.index(word) == 0:
                instruction = word
                i += 1
                continue