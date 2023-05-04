

and then call the functions `robot.grab()`, `robot.close()`, `robot.pull()`, etc.
in a correct order.

--->

    
def handle_pull(robot):
    if check("the robot's gripper is not almost vertically aligned with handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is almost vertically aligned with the handle and the robot's gripper is open"):
        robot.grab("handle")
    if check("the robot's gripper is vertically aligned with handle"):
        robot.pull("handle up")
"""

# Instructions for the turker
# Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.

# Here's some code that demonstrates how the robot can do a variety of tasks:

# def peg_insert_side(robot):
#     if check("the robot's gripper is not vertically aligned with the peg"):
#         robot.put("gripper above peg")
#     if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
#         robot.grab("peg")
#     if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
#         robot.align("peg to hole")
#     if check("peg is horizontally aligned with hole"):
#         robot.insert("peg into hole")

# def push(robot):
#     if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
#         robot.put("the gripper above the puck")
#     if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
#         robot.push("the gripper into the puck")
#     if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
#         robot.slide("the puck to the goal")

# def reach(robot):
#     if check("the robot's gripper is not near reach target"):
#         robot.reach("to goal")

# def window_close(robot):
#     if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
#         robot.move("gripper to left of window handle")
