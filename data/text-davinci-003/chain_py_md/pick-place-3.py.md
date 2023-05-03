

# pick-place: pick up the puck and hold it at the target location
def pick_place(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Grab the puck with the gripper
    #  3. Hold the puck at the goal
    # We need to put the gripper above the puck before we can grab it.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above puck")
    # Once the gripper is above the puck, we should be able to grab the puck.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not around puck"):
        robot.grab("puck")
    # Once the puck is grabbed, move the puck to the target location.
    if check("the robot's gripper is around the puck and the puck is not at the goal"):
        robot.move("puck to goal")
    # When the puck is at the target location, keep holding it in the gripper.
    if check("the robot's gripper is still around the puck and the puck is at the goal"):
        robot.hold("puck at goal")