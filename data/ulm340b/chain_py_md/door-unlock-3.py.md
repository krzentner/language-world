

and then put your code below.
""")

DOOR_UNLOCK_TEMPLATE = """
# door-unlock: turn the dial on the door
def door_unlock(robot):
    # Steps:
    #  1. Put gripper above the dial
    #  2. Put gripper left of the dial
    #  3. Move gripper to turn the dial
    if check("the robot's gripper is not above dial"):
        robot.put("gripper above dial")
    if check("the robot's gripper is not left of dial and the robot's gripper is not near dial"):
        robot.move("gripper to left of dial")
    if check("the robot's gripper is left of dial and the robot's gripper is near dial"):
        robot.turn("dial")
"""

def check_task(obj):
    """
    Check if the object is a valid program, according to the instructions.
    Return the score.
    """
    task_text = obj["task_text"]
    task = DOOR_UNLOCK_TASK.splitlines()
    task_code = task_text.splitlines()
    if (not task_code[0].startswith('#') or
            task_code[0] != task[0] or
            task_code[-1] != task[-1]):
        return 0

    for idx, program_line in enumerate(task[1:-1]):
        text = task_code[idx+1]
        if not (program_line.startswith('#') and text.startswith('#')):
            # We should only compare code with code or comment with comment
            continue

        if text != program_line:
            return 0

    return 1

if __name__ == "__main__":
    for key in TASK_TEMPLATES.keys():
        if key == "door-unlock":
            TASK_TEMPLATES[key] = DOOR_UNLOCK_TEMPLATE

    TASK_TEMPLATES = dict(TASK_TEMPLATES, **{
        "door-unlock": DOOR_UNLOCK_TEMPLATE,
    })

    obj = json.load(sys.stdin)

    task = task_text = obj["task_text"]

    task_code = task_text.splitlines()

    score = check_task(obj)
    if score == 1:
        print(task_code)
        print(task_text)
    