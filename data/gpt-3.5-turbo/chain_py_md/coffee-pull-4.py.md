# coffee-pull: grab the mug and pull it to the target location
def coffee_pull(robot):
    # Steps:
    #  1. Put gripper above mug handle
    #  2. Drop gripper around mug handle
    #  3. Close gripper around mug handle
    #  4. Move mug to goal by pulling it
    # First, put the gripper above the mug handle.
    if check("the robot's gripper is not above the mug handle"):
        robot.put("gripper above mug handle")
    # If the gripper isn't around the mug handle, drop it around the handle.
    if check("the robot's gripper is not around mug handle and the robot's gripper is open"):
        robot.drop("gripper around mug handle")
    # If the gripper is near the mug handle and open, grab it by closing the gripper.
    if check("the robot's gripper is near mug handle and the robot's gripper is open"):
        robot.close("gripper around mug handle")
    # We've grabbed the handle. Pull the mug towards the target location.
    if check("the robot's gripper is around mug handle and the mug is not at the goal"):
        robot.pull("mug to goal")