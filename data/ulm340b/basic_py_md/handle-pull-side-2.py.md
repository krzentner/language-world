

And then call `robot.gripper_close()` when the robot's gripper is around the handle.
Then call `robot.move()` to slide the handle up.

''')



def handle_pull_side(robot):
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is vertically aligned with the handle and the robot's gripper is not around the handle"):
        robot.put("gripper around handle")
    if check("the robot's gripper is around the handle"):
        robot.close("the gripper around the handle")
    if check("the handle is not raised"):
        robot.move("the handle up")





def reach(robot):
    if check("the robot's gripper is not near reach target"):
        robot.reach("to goal")

def push(robot):
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("the puck to the goal")

def window_close(robot):
    if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move("gripper to left of window handle")
    if check("the robot's gripper is near the window handle"):
        robot.slide("window right")
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window right harder")

def window_open(robot):
    if check("the robot's gripper is not vertically aligned with the window handle and the robot's gripper is below the window handle"):
        robot.move("gripper to right of window handle")
    if check("the robot's gripper is near the window handle"):
        robot.slide("window left")
    if check("the robot's gripper is in front of the window handle"):
        robot.