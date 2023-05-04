

and press the **"Check"** button to verify it's correct.

In this environment, the robot can perform the following actions:

  - **robot.place("object at goal")** will move the robot's gripper to try to
    place the object at the target location,
  - **robot.slide("object into goal")** will slide the object sideways into
    the target location,
  - **robot.slide("object to goal")** will slide the object forward towards
    the target location,
  - **robot.grab("object")** will put the robot's gripper around the object,
  - **robot.align("object to other_object")** will put the object near the
    other object,
  - **robot.push("object to goal")** will push the object towards the target
    location,
  - **robot.reach("to goal")** will move the robot's gripper to the target
    location,
  - **robot.insert("object into other_object")** will insert the object into
    the other object,
  - **robot.pull("object to goal")** will pull the object towards the target
    location,
  - **robot.put("gripper above object")** will put the robot's gripper above
    the object,
  - **robot.move("gripper to object")** will move the robot's gripper near the
    object,
  - **robot.close("gripper around object")** will close the robot's gripper
    around the object,
  - **robot.push("gripper into object")** will push the robot's gripper into
    the object,
  - **robot.grab("object")** will put the robot's gripper around the object,
  - **robot.drop("gripper around object")** will put the robot's gripper around
    the object.

This environment also has some **check** functions:
  - **check("the robot's gripper is not near object")** will return whether the
    robot's gripper is near the object or not,
  - **check("the robot's gripper is not near object and the robot's gripper is below object")** will return whether the robot's gripper is near the object and the robot's gripper is below the object or not,
  - **check("the robot's gripper is above object")** will return whether the robot's gripper is above the object or not,
  - **check("the robot's gripper is vertically