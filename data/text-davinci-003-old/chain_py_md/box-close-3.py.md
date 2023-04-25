

Steps:
1. Put gripper above the lid
2. Grab the lid with the gripper
3. Move the lid to the box
4. Place lid on the box

```
# box-close: pick up the box lid and place it on the box
# def box_close(robot):
    # Steps:
    #  1. Put gripper above the lid
    #  2. Grab the lid with the gripper
    #  3. Move the lid to the box
    #  4. Place lid on the box
    # First, put the gripper above the lid.
    if check("the robot's gripper is not above lid"):
        robot.put("gripper above lid")
    # Once the gripper is above the lid, grab it by moving the gripper around it.
    if check("the robot's gripper is above lid and the robot's gripper is not around lid"):
        robot.grab("lid")
    # Once the gripper is around the lid, move it to the box.
    if check("the robot's gripper is around lid"):
        robot.move("lid to box")
    # Once the lid is above the box, place it on the box.
    if check("lid is above box"):
        robot.place("lid on box")