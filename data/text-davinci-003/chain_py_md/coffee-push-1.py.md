

# coffee-push: grab the mug and move it to the target location
def coffee_push(robot):
    # Steps:
    #  1. Put gripper above mug handle
    #  2. Drop gripper around mug handle
    #  3. Close gripper around mug handle
    #  4. Move mug to goal
    # First, put the gripper roughly above the mug handle.   
    if check("the robot's gripper is not almost vertically aligned with the mug handle"):
        robot.put("gripper above mug handle")
    # If the gripper isn't close to the mug handle, try to grab it by moving it
    # down.
    if check("the robot's gripper is not close to mug handle and the robot's gripper is around mug handle"):
        robot.drop("gripper around mug handle")
    # Once the gripper is near the mug handle, close it around the handle to grab
    # it.
    if check("the robot's gripper is near mug handle and the robot's gripper is open"):
        robot.close("gripper around mug handle")
    # If the mug is still near the gripper, we should have grabbed it with the
    # gripper, so move it to the target location.
    if check("the robot's gripper is above mug handle and the robot's gripper is closed"):
        robot.move("mug to goal")