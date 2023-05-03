


# pick-place: pick up the puck and hold it at the target location
def pick_place(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Grab the puck with the gripper
    #  3. Move the gripper to target location
    #  4. Close the gripper to maintain hold on the puck
    # First, put the gripper above the puck.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above puck")
    # Once the gripper is above the puck, we should be able to grab it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is open"):
        robot.grab("puck")
    # Once the gripper is around the puck, we can just move the gripper up to
    # the target location.
    if check("the robot's gripper is actually holding the puck"):
        robot.move("gripper to target location")
    # Once the gripper is at the target location, close the gripper to make sure
    # we don't lose the puck.
    if check("the robot's gripper is at the target location"):
        robot.close("gripper")