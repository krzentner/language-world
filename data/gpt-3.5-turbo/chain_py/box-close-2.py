# Steps:
    # 1. Put gripper above box lid
    # 2. Drop gripper around box lid
    # 3. Lift the box lid
    # 4. Align the box lid with the box
    # 5. Place the box lid on the box
    # First, put the gripper roughly above the box lid.
    if check("the robot's gripper is not above the box lid"):
        robot.place("gripper above box lid")
    # If the gripper isn't around the box lid, put it around the box lid.
    if check("the robot's gripper is not around box lid and the robot's gripper is open"):
        robot.drop("gripper around box lid")
    # If the gripper is near the box lid and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near box lid and the robot's gripper is open"):
        robot.close("gripper around box lid")
    # We closed the gripper, and the box lid is still near the gripper, so maybe we
    # grabbed it.
    # Try to lift the box lid.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is around box lid and the robot's gripper is closed"):
        robot.lift("box lid")
    # If the box isn't near the gripper, move it towards the box.
    if check("the robot's gripper is not above the box and the robot's gripper is holding the box lid"):
        robot.move("gripper towards box")
    # If the box lid is above the box, align it with the box.
    if check("the box lid is aligned with the box"):
        robot.align("box lid with box")
    # Once the box lid is aligned, place it on top of the box.
    if check("the box lid is aligned with the box and the robot's gripper is holding the box lid"):
        robot.place("box lid on top of box")