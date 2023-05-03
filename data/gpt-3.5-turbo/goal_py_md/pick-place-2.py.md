# pick-place: pick up the puck and hold it at the target location
def pick_place(robot):
    # We first need to locate the puck and move the gripper above it.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    # Once the gripper is lined up with the puck from above, we can grab it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not around puck"):
        robot.move_gripper("around the puck", close_gripper=True)
    # Once the gripper has a hold of the puck, move it to the target location.
    if check("the robot's gripper is around the puck and the robot's gripper is not above the target location"):
        robot.move_gripper("above the target location", close_gripper=True)