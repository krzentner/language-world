
""")


def task_to_description(task: str):
    if task == 'pick-place':
        description = (
            'The task pick-place requires the robot to pick up the puck and hold it at the target location.'
        )
    elif task == 'push':
        description = (
            'The task push requires the robot to slide the puck to the target location.'
        )
    elif task == 'button-press-topdown':
        description = (
            'The task button-press-topdown requires the robot to push the button down from above.'
        )
    elif task == 'door-open':
        description = 'The task door-open requires the robot to pull the door open.'
    elif task == 'drawer-close':
        description = (
            'The task drawer-close requires the robot to push the drawer close.'
        )
    elif task == 'drawer-open':
        description = 'The task drawer-open requires the robot to pull the drawer open.'
    elif task == 'peg-insert-side':
        description = (
            'The task peg-insert-side requires the robot to grab the peg and insert it into the hole from the side.'
        )
    elif task == 'reach':
        description = 'The task reach requires the robot to reach to the target location.'
    elif task == 'window-close':
        description = (
            'The task window-close requires the robot to slide the window closed to the right.'
        )
    elif task == 'window-open':
        description = (
            'The task window-open requires the robot to slide the window open to the left.'
        )
    else:
        raise ValueError(f'unknown task: {task}')

    return description


def instruction_to_description(task: str, instruction: str):
    descriptions = {
        'button-press-topdown': {
            'put gripper above button': (
                'When the robot\'s gripper is not vertically aligned with button, '
                'the robot should put gripper above button.'
            ),
            'push down on button': 'When the robot\'s gripper is vertically aligned with button, '
                                  'the robot should push down on button.'
        },
        'drawer-close': {
            'grab drawer handle': (
                'When the robot\'s gripper is not near the drawer