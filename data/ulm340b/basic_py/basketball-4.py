
    if check("the robot's gripper is not vertically aligned with the basketball"):
        robot.put("gripper above the basketball")
    if check("the basketball is not left of the robot's gripper and basketball is not forward aligned with robot's gripper"):
        robot.grab("basketball")
    if check("the robot's gripper is forward aligned with basketball and basketball is not horizontally aligned with hoop"):
        robot.align("basketball to hoop")
    if check("basketball is horizontally aligned with hoop"):
        robot.release("basketball into hoop")

# sweep: sweep the puck into the target area
def sweep(robot):
    if check("the robot's gripper is not vertically aligned with the puck and the robot's gripper is not above puck"):
        robot.put("the gripper above puck")
    if check("the robot's gripper is vertically aligned with puck and the robot's gripper is not near puck"):
        robot.push("gripper into puck")
    if check("the robot's gripper is near puck and the robot's gripper is above puck"):
        robot.slide("the puck to goal")

# push-right: push the puck to the right
def push_right(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is vertically aligned with puck and the robot's gripper is not near puck"):
        robot.push("gripper into puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("the puck right")

# lever-pull: pull down the lever
def lever_pull(robot):
    if check("the robot's gripper is not vertically aligned with the lever"):
        robot.put("gripper above lever")
    if check("the robot's gripper is vertically aligned with lever and the robot's gripper is not around lever"):
        robot.put("gripper around lever")
    if check("the robot's gripper is around lever"):
        robot.pull("down lever")

# door-close: close the door
def door_close(robot):
    if check("the robot's gripper is not near the door"):
        robot.reach("for door")
    if check("the robot's gripper is near the