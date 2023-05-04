
    # Steps:
    #  1. Put gripper above plate handle
    #  2. Drop gripper around plate handle
    #  3. Slide the plate back towards the goal
    # First, put the gripper above the plate handle.
    if check("the robot's gripper is not above the plate handle"):
        robot.put("gripper above plate handle")
    # If the gripper isn't around the plate, put it around the plate.
    if check("the robot's gripper is not around plate handle"):
        robot.grab("plate handle")
    # If the gripper is near the plate handle and open, maybe we can grab it by
    # closing the gripper.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is around plate handle"):
        robot.slide("plate towards goal")

# switch-on: flip the switch up
def switch_on(robot):
    # Steps:
    #  1. Put gripper above switch
    #  2. Put gripper around switch
    #  3. Flip the switch
    # We need to put the gripper above the switch before we can grab it,
    # because of the angle of the robot's gripper.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with switch"):
        robot.put("gripper above switch")
    # As long as the gripper is mostly lined up with the switch, closing it
    # should line it up all the way.
    if check("the robot's gripper is vertically aligned with switch and the robot's gripper is open"):
        robot.put("gripper around switch")
    # Once the gripper is around the switch, we can flip the switch.
    if check("the robot's gripper is around switch"):
        robot.toggle("switch up")

# switch-off: flip the switch down
def switch_off(robot):
    # Steps:
    #  1. Put gripper above switch
    #  2. Put gripper around switch
    #  3. Flip the switch
    # We need to put the gripper above the switch before we can grab it,
