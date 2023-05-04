
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck backwards to goal
    # The robot can slide the puck by trapping it by pushing down on it from
    # above and moving the gripper.
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it to the target location.
    # Close the gripper to make sure we keep control of the puck.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("the puck to the goal backwards")

# hook: hook the ring and pull it to the target location
def hook(robot):
    # Steps:
    #  1. Put gripper below ring
    #  2. Hook ring
    #  3. Pull ring to goal
    # We want to grab the ring, so first, move the gripper below the ring.
    if check("the robot's gripper is not below ring"):
        robot.put("gripper below ring")
    # If the gripper is lined up under the ring, try to hook it.
    if check("the robot's gripper is below ring and the robot's gripper is vertically aligned with the ring"):
        robot.hook("ring")
    # If the ring is hooked, pull the ring to the target location.
    if check("the robot's gripper is above ring and the robot's gripper is not vertically aligned with the ring"):
        robot.pull("ring towards goal")

# sweep: sweep the ring to the target location
def sweep(robot):
 