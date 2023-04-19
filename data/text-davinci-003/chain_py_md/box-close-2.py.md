

Steps: 
1. Put the gripper on top of the lid
2. Open the gripper to grab the lid
3. Lift the lid and bring it towards the box
4. Place the lid on the box

```
# box-close: pick up the box lid and place it on the box
# def box_close(robot):
    # Steps:
    #  1. Put the gripper on top of the lid
    #  2. Open the gripper to grab the lid
    #  3. Lift the lid and bring it towards the box
    #  4. Place the lid on the box
    # Put the gripper above the lid.
    if check("the robot's gripper is not vertically aligned with the lid"):
        robot.put("gripper above lid")
    # Once the gripper is above the lid, open it to grab the lid.
    if check("the robot's gripper is vertically aligned with the lid"):
        robot.open("gripper grabbed lid")
    # Now that the gripper is closed around the lid, move the lid towards the box.
    if check("the robot's gripper is holding the lid"):
        robot.lift("lid towards box")
    # Assuming the gripper moved the lid to the box, now we can just place the lid on the box.
    if check("the robot's gripper is near the box and the lid is above the box"):
        robot.place("lid on box")