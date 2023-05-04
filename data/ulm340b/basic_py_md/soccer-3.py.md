

You will have three actions to choose from:

* ``robot.move("gripper to the right of the ball")``
* ``robot.align("gripper behind the ball")``
* ``robot.slide("the ball to the goal")``

"""


# soccer: push the soccer ball into the target location
def soccer(robot):
    if check("the robot's gripper is not forward aligned with the soccer ball"):
        robot.move("gripper to the right of the ball")
    if check("the robot's gripper is left of the soccer ball and the robot's gripper is not aligned behind the ball"):
        robot.align("gripper behind the ball")
    if check("the robot's gripper is aligned behind the ball and the ball is not below the robot's gripper"):
        robot.slide("the ball to the goal")

# push: slide the puck to the target location
def push(robot):
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("the puck to the goal")

# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    if check("peg is horizontally aligned with hole"):
        robot.insert("peg into hole")

# reach: reach to the target location
def reach(robot):
    if check("the robot's gripper is not near reach target"):
        robot.reach("to goal")

# window-close: slide the window closed to the right
def window_close(robot):
   