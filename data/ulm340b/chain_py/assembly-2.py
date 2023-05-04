
    # Steps:
    #  1. Put gripper above wrench
    #  2. Grab wrench with gripper
    #  3. Put gripper above peg
    #  4. Put peg above wrench
    #  5. Release the wrench
    #  6. Line wrench up with hole
    #  7. Push wrench down
    #  8. Slide wrench left
    # First, put the gripper above wrench.
    if check("the robot's gripper is not vertically aligned with wrench"):
        robot.put("gripper above wrench")
    # If the wrench is not in the gripper, grab it by moving the gripper down
    # around it.
    if check("the robot's gripper is vertically aligned with wrench and the robot's gripper is open"):
        robot.grab("wrench")
    # Since we have the wrench, we need to move the gripper up to clear the peg.
    # Once we're above the peg, drop the gripper down around the peg.
    if check("the robot's gripper is above peg and the robot's gripper is open"):
        robot.put("gripper around peg")
    # At this point, we should have the gripper around the peg and the wrench in
    # the gripper.
    # Move the gripper down around the peg and move the peg up near the wrench.
    if check("the robot's gripper is around peg and the robot's gripper is closed"):
        robot.put("peg above wrench")
    # Drop the wrench in.
    if check("the robot's gripper is around peg"):
        robot.release("wrench")
    # If the wrench is not aligned with the peg's hole, move it above the hole.
    if check("wrench is not vertically aligned with peg"):
        robot.put("wrench above peg")
    # If the wrench is lined up vertically, we can just push it down.
    if check("wrench is vertically aligned with peg"):
        robot.push("wrench into peg")
    # Slide the wrench left until it goes in.
    if check("wrench is near peg"):
        robot.slide("wrench left")

# pick-place-side: pick up the puck and place it to the side
def pick_place_