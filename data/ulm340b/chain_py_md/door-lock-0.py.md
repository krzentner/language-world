

You need to write the rest of the door-lock function.

Write down the steps of the door lock process.

Here are a few things you can have the robot do:

`robot.check("statement")`:
This statement looks at the state of the world, and checks if the statement is true.

Here are some statements that you can check:

`robot.gripper.vertically_aligned_with(object_name)`:
This is true if an object is vertically aligned with the robot's gripper.

`robot.gripper.forward_aligned_with(object_name)`:
This is true if an object is horizontally aligned with the robot's gripper.

`object_name.left_of(other_object_name)`:
This is true if the left edge of the object is left of the right edge of the other object.

`object_name.below(other_object_name)`:
This is true if the bottom edge of the object is below the top edge of the other object.

`object_name.right_of(other_object_name)`:
This is true if the right edge of the object is right of the left edge of the other object.

`object_name.above(other_object_name)`:
This is true if the top edge of the object is above the bottom edge of the other object.

`robot.gripper.around(object_name)`:
This is true if the robot's gripper is around an object.

`robot.gripper.near(object_name)`:
This is true if the robot's gripper is near an object.

`robot.gripper.open`:
This is true if the robot's gripper is open.

`robot.gripper.closed`:
This is true if the robot's gripper is closed.

`object_name.small`:
This is true if the object is small.

`object_name.big`:
This is true if the object is big.

`object_name.long`:
This is true if the object is long.

Here are some things you can do:

`robot.move("gripper below object_name")`:
This will make the gripper go below the object.

`robot.move("gripper above object_name")`:
This will make the gripper go above the object.

`robot.move("gripper left of object_name")`:
This will make the gripper go left of the object.

`robot.move("gripper right of object_name")`:
This will make the gripper go right of the object.
