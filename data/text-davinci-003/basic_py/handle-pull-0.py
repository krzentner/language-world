
    if check("the robot's gripper is not near the handle"):
        robot.grab("handle")
    if check("the robot's gripper is near the handle and the robot's gripper is open"):
        robot.close("gripper around handle")
    if check("the robot's gripper is around the handle"):
        robot.pull("handle up")

# cat-pet: move the robot's gripper to pet the cat
def cat_pet(robot):
    if check("the robot's gripper is not near cat"):
        robot.reach("to cat")
    if check("the robot's gripper is near the cat"):
        robot.pet("cat")