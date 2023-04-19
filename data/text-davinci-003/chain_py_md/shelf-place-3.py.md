

Steps:
  1. Put the gripper slightly above the block
  2. Drop the gripper around the block
  3. Close the gripper around the block
  4. Move the block to the target shelf
  5. Place the block on the shelf

# shelf-place: pick up the block and place it at the target location
# def shelf_place(robot):
    # Steps:
    #  1. Put the gripper slightly above the block
    if check("the robot's gripper is not almost vertically aligned with block"):
        robot.put("gripper slightly above block")
    #  2. Drop the gripper around the block
    if check("the robot's gripper is almost vertically aligned with the block and the robot's gripper is open"):
        robot.put("gripper around the block")
    #  3. Close the gripper around the block
    if check("the robot's gripper is around the block and the robot's gripper is open"):
        robot.close("gripper around block")
    #  4. Move the block to the target shelf
    if check("the robot's gripper is above the block and the robot's gripper is closed"):
        robot.move("block to goal")
    #  5. Place the block on the shelf
    if check("block is near goal shelf"):
        robot.place("block on shelf")