
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Line up the gripper as viewed from the side
    #  3. Line up the gripper as viewed from the front
    #  4. Push down on the button
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # Line up the robot's gripper from the side.
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.put("gripper horizontally aligned with button")
    # Line up the robot's gripper from the front.
    if check("the robot's gripper is not aligned with button"):
        robot.put("gripper aligned with button")
    # The gripper is probably aligned with the button now, so just push down.
    if check("the robot's gripper is aligned with button"):
        robot.push("down on button")

# peg-insert-topdown: drop the peg into the hole from above
def peg_insert_topdown(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Drop gripper around the peg
    #  3. Grab peg with the gripper
    #  4. Lift the peg up and line it up with the hole
    #  5. Drop the peg in the hole
    # Put the gripper above the peg so it doesn't bump into the peg while we're
    # grabbing it.
    if check("the robot's gripper is not vertically aligned with peg"):
        robot.put("gripper above peg")
    # We're trying to grab the peg, so open the gripper.
    if check("the robot's gripper is not open"):
        robot.put("the gripper open")
    # If the gripper is aligned with the peg but not near it, move the gripper
    # down to the peg to grab it.
    if check("the robot's gripper is vertically aligned with the peg and the robot's gripper is not near peg"):
        robot.drop("gripper around peg")
    # If the gripper is around the peg, we should