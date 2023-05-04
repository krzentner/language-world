
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Line up the gripper as viewed from the front
    #  3. Push down on the button
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # Once the gripper is above the button, make sure it is lined up with the
    # button as seen from the front as well.
    if check("the robot's gripper is vertically aligned with button and the robot's gripper is not horizontally aligned with button"):
        robot.align("gripper with button")
    # Now that the gripper is lined up with the button, push the button.
    if check("the robot's gripper is vertically aligned with button and the robot's gripper is horizontally aligned with button"):
        robot.push("button")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper below the door handle
    #  2. Put gripper behind the door handle
    #  3. Push the door closed
    # First, the robot's gripper should be below the door handle.
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.put("gripper below door handle")
    # Next, the gripper should be behind the door handle so we can push the door
    # closed.
    if check("the robot's gripper is below door handle and the robot's gripper is not forward aligned with door handle"):
        robot.put("gripper behind door handle")
    # Now we can push the door closed from the front.
    if check("the robot's gripper is forward aligned with door handle"):
        robot.push("door closed")

# peg-insert-down: grab the peg and insert it into the hole from above
def peg_insert_down(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Put the peg into the hole
    # First, put the