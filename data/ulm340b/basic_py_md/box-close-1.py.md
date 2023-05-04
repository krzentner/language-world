

Then write a series of `if` blocks like the ones above.


[Show sample solution]
```
# box-close: pick up the box lid and place it on the box
def box_close(robot):
    if check("the robot's gripper is not above the box"):
        robot.put("the gripper above the box")
    if check("the robot's gripper is not around box lid and the robot's gripper is open"):
        robot.drop("the gripper around box lid")
    if check("the robot's gripper is near box lid and the robot's gripper is open"):
        robot.close("the gripper around box lid")
    if check("the robot's gripper is above box lid and the robot's gripper is closed"):
        robot.move("the gripper above the box")
    if check("the robot's gripper is near the box and the robot's gripper is closed"):
        robot.place("box lid on box")
```
"""








# --------------------------------------------------
# PART 2
# --------------------------------------------------

task_example="""
box-close
def box_close(robot):
    if check("the robot's gripper is not above the box"):
        robot.put("the gripper above the box")
    if check("the robot's gripper is not around box lid and the robot's gripper is open"):
        robot.drop("the gripper around box lid")
    if check("the robot's gripper is near box lid and the robot's gripper is open"):
        robot.close("the gripper around box lid")
    if check("the robot's gripper is above box lid and the robot's gripper is closed"):
        robot.move("the gripper above the box")
    if check("the robot's gripper is near the box and the robot's gripper is closed"):
        robot.place("box lid on box")
"""

task_examples=[
    "box-close",
]

# Override this with your own code in the class_override file
def sample_tasks(verbose=True):
    if verbose:
        print(sample_task_description)
    task_dict = {}
    # TODO: Implement this
    raise NotImplementedError()
    return task_dict
[eod] [code]"""
    sphinx.util.docstrings
   