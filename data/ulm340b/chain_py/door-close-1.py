
    # Steps:
    #  1. Put gripper above door handle
    #  2. Move gripper down to around door handle
    #  3. Push the door closed
    # If the gripper isn't vertically aligned with the door handle, put it above
    # the door handle.
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.put("gripper above door handle")
    # Now that the gripper is vertically aligned with the door handle, it should
    # be easy to grab the door handle from the top.
    if check("the robot's gripper is vertically aligned with door handle and the robot's gripper is open"):
        robot.close("gripper around door handle")
    # If the gripper is near the door handle and the door is open, we can push
    # the door closed.
    if check("the robot's gripper is forward aligned with door handle and door is open"):
        robot.push("door closed")

# block-insert-side: grab the block and slide it sideways into the box
def block_insert_side(robot):
    # Steps:
    #  1. Put gripper above block
    #  2. Drop gripper around block
    #  3. Slide block into box
    # First, put the gripper above the block.
    if check("the robot's gripper is not vertically aligned with block"):
        robot.put("gripper above block")
    # If the block becomes left of the gripper, go back to putting the gripper
    # above the block.
    # Because the block is a long object, check if the gripper is lined up with
    # it from the front instead of around it.
    if check("block is not left of the robot's gripper and block is not forward aligned with the robot's gripper"):
        robot.grab("block")
    # As long the gripper is still mostly around the block and the block isn't
    # lined up with the box, line up the block with the box.
    if check("the robot's gripper is forward aligned with block and block is not aligned with box"):
        robot.align("block to box")
    # If the block is aligned with the box to the side, insert it.
    if check("block is