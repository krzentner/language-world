
    - When the robot's gripper is not in front of button, the robot should put gripper in front of button.
    - When the robot's gripper is in front of button, the robot should push the button from the front.
'''


def get_help_messages():
    return [HELP_MESSAGES[task] for task in TASKS]


def get_instruction_messages(tasks):
    return {task: INSTRUCTIONS[task] for task in tasks}


def get_instruction_labels():
    return [task + '_instructions' for task in TASKS]


def get_question_labels(tasks):
    return {task: QUESTIONS[task] for task in tasks}


def get_answer_labels(tasks):
    return [task + '_answers' for task in TASKS]


# Instructions:
INSTRUCTIONS = {
    'reach': """The task `reach` requires the robot to reach to the target location.
To reach to the target location reliably, the robot should perform the following steps:
    Steps:  1. Reach towards the target
    We don't have any objects to manipulate, so we can just move the robot's gripper directly to the target location
    - When the robot's gripper is not near reach target, the robot should reach to goal.""",
    'window-open': """The task `window-open` requires the robot to slide the window open to the left.
To slide the window open to the left reliably, the robot should perform the following steps:
    Steps:  1. Put gripper right of the window handle  2. Start pushing against the window handle to open the window  3. Push the window open harder
    If the robot's gripper is not vertically lined up with the window handle, we should move the gripper near the window handle to start pushing
    - When the robot's gripper is not vertically aligned with the window handle and the robot's gripper is below the window handle, the robot should move gripper to right of window handle.
    If the robot's gripper is near the window handle we can probably slide the window open now by moving the gripper left.
    - When the robot's gripper is near the window handle, the robot should slide window left.
    If the robot's gripper is starting to be in front of the window handle, push harder.
    - When the robot's gripper is in front of the window handle, the robot should push window left harder.""",
    'door-open': """The task `door-open` requires the robot