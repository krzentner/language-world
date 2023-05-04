

The `door_close` function should not have more than 15 lines of code.


######################################################################

def door_close(robot):
    if check("the robot's gripper is not below the handle"):
        robot.put("gripper below door handle")
    if check("the robot's gripper is forward aligned with the handle"):
        robot.grab("door handle")
    if check("the robot's gripper is aligned with the handle"):
        robot.push("door closed")

################################################################################################
#
#   TASK 2.7:
#
################################################################################################

# Hello. Today we will work on a task that will require some abstraction.

```
# put-on-floor-onside: put the object on the floor and put the gripper beside the object
def put_on_floor_onside(robot):
    if check("the gripper is above the object and the gripper is open"):
        robot.drop("the object")
    if check("the object is below the robot's gripper and the robot's gripper is open"):
        robot.put("the robot's gripper next to the object")
    if check("the gripper is next to the object"):
        robot.open("the robot's gripper")

# place-in-r1: place the object inside region 1
def place_in_r1(robot):
    if check("the robot's gripper is left of region 1 and the gripper is above the object and the robot's gripper is open"):
        robot.move("gripper into region 1")
    if check("the robot's gripper is in region 1 and the gripper is above the object and the robot's gripper is open"):
        robot.drop("the object")
    if check("the robot's gripper is above the object and the robot's gripper is open"):
        robot.open("the robot's gripper")

# grasp-r1: grip the object in region 1
def grasp_r1(robot):
    if check("the robot's gripper is above the object and the robot's gripper is open"):
        robot.close("the robot's gripper")
    if check("the robot's gripper is in region 1 and the robot's gripper is closed"):
        robot.move("the object out of region 1")
