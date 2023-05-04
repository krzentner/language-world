

Your function should return once the faucet is closed (vertical).
Each step of the function, it should check a single fact about the world and execute a single robot command if the fact is true.

The robot can perform the following checks:

- check("the robot's gripper is open")
- check("the robot's gripper is closed")
- check("the robot's gripper is above $object")
- check("the robot's gripper is below $object")
- check("the robot's gripper is aligned to $object")
- check("the robot's gripper is not aligned to $object")
- check("the robot's gripper is near $object")
- check("the robot's gripper is not near $object")
- check("the robot's gripper is aligned to $object and $object is not horizontally aligned with $object2")
- check("the robot's gripper is aligned to $object and $object is horizontally aligned with $object2")
- check("the robot's gripper is aligned to $object and $object is not vertically aligned with $object2")
- check("the robot's gripper is aligned to $object and $object is vertically aligned with $object2")
- check("the robot's gripper is vertically aligned with $object")
- check("the robot's gripper is not vertically aligned with $object")
- check("the robot's gripper is forward aligned with $object")
- check("the robot's gripper is not forward aligned with $object")

The robot can perform the following actions:

- robot.move("$object")
- robot.move("gripper to left of $object")
- robot.move("gripper to right of $object")
- robot.move("gripper above $object")
- robot.move("gripper below $object")
- robot.put("gripper around $object")
- robot.put("gripper above $object")
- robot.put("gripper below $object")
- robot.put("$object in front of gripper")
- robot.put("$object above gripper")
- robot.put("$object below gripper")
- robot.grab("$object")
- robot.drop("$object")
- robot.close("$object")
- robot.align("$object to $object")
- robot.insert("$object into $object")
- robot.slide("$object to $object")
- robot.pull("$object towards the robot")
- robot.push("$object away from the robot")
- robot.align("$object with $object")
- robot.move