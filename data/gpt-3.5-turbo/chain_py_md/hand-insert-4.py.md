# hand-insert: pick up the puck and move it to the target location
def hand_insert(robot):
    # Steps:
    # 1. Place one end of the puck on the table.
    # 2. Place the robot's gripper around the other end of the puck and close the gripper.
    # 3. Lift the puck with the gripper.
    # 4. Move the gripper to the target location.
    # 5. Lower the puck onto the target location.
    # Determine which end of the puck to place on the table based on its shape.
    if check("the puck is circular"):
        robot.place("one end of the puck on the table")
    elif check("the puck is rectangular"):
        robot.place("one edge of the puck on the table")
    # Once one end of the puck is on the table, position the gripper around the
    # other end and close it to grab the puck.
    if check("one end of the puck is on the table and the robot's gripper is not around the other end of the puck"):
        robot.put("gripper above the other end of the puck")
        robot.drop("gripper around the other end of the puck")
        robot.close("the gripper around the other end of the puck")
    # With the gripper around the puck, lift it off the table.
    if check("the robot's gripper is around the other end of the puck and is closed"):
        robot.lift("the puck")
    # Move the gripper to the target location.
    if check("the puck is lifted by the robot's gripper"):
        robot.move("the gripper to the target location")
    # Lower the puck onto the target location.
    if check("the gripper is at the target location"):
        robot.drop("the puck on the target location")