

I will run your program several times on different arrangements of the puck and the target location to make sure that it can solve this task correctly.

For each object, we use the "center of mass" to define where the object is.
You can move the gripper to this point using:

-   the command `robot.move_gripper('horizontally aligned with the puck')` moves the gripper so that it is horizontally aligned with the puck and about the same distance from the edge of the table as the puck;
-   the command `robot.move_gripper('vertically aligned with the puck')` moves the gripper so that it is vertically aligned with the puck and about the same distance above the table as the puck;
-   the command `robot.move_gripper('above the puck')` moves the gripper so that it is above the puck, close to the top surface of the puck;
-   the command `robot.move_gripper('near the puck')` moves the gripper to near where the puck is.

Here are some examples of the gripper being aligned with objects and target locations:

![](images/aligned.jpg)

We say the gripper is above an object if it's closer to the top of the object than the table.
We say the gripper is below an object if it's closer to the bottom of the object than the table.
If the gripper is neither above nor below an object, we say it is near the object.

Here are some examples of the gripper being above, below, and near objects and target locations:

![](images/near.jpg)

We say the gripper is left of an object if it's farther left than the left edge of the object, and we say the gripper is right of an object if it's farther right than the right edge of the object.
If the gripper is neither right nor left of the object, we say that the gripper is around the object.

Here are some examples of the gripper being left of, right of, and around objects and target locations:

![](images/around.jpg)

Finally, we say the gripper is in front of an object if it's farther away from us than the far edge of the object, and we say the gripper is behind an object if it's closer to us than the close edge of the object.
If the gripper is neither in front of nor behind the object, we say that the gripper is forward aligned with the object.

Here are some examples of the gripper being in front of, behind, and forward aligned with objects and target locations:

![](images/forward-aligned.jpg)

Your robot can