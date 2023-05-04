
-- When the robot's gripper is not near the handle, the robot should get gripper near the handle.
-- When the robot's gripper is near the handle and the robot's gripper is not around the handle, the robot should grab handle.
-- When the robot's gripper is around the handle, the robot should pull the handle.

The task `stick-push` requires the robot to push the long stick into the hole.
To push the long stick into the hole reliably, what steps the robot should perform?
-- When the robot's gripper is not around the top of the stick, the robot should grab the stick.
-- When the robot's gripper is around the top of the stick and the robot's gripper is not aligned with the hole, the robot should put gripper in line with hole.
-- When the stick is aligned with the hole and the stick is not forward aligned with the hole, the robot should push the stick into the hole.

The task `stick-push-side` requires the robot to push the long stick into the hole to the side.
To push the long stick into the hole to the side reliably, what steps the robot should perform?
-- When the robot's gripper is not around the top of the stick, the robot should grab the stick.
-- When the robot's gripper is around the top of the stick and the robot's gripper is not aligned with the hole, the robot should put gripper in line with hole.
-- When the stick is aligned with the hole and the stick is not horizontally aligned with the hole, the robot should line up the stick to the hole.
-- When the stick is horizontally aligned with the hole, the robot should push the stick into the hole.

"""

print(prompt)
prompt_type = int(input("Prompt type (-1 to exit): "))
while prompt_type != -1:
    print()
    for i in range(prompt_type):
        print()
    prompt_type = -1

    text = ("\n" +
            "Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.\n\n" +
            "The task `peg-insert-side` requires the robot to grab the peg and insert it into the hole from the side.\n" +
            "To grab the peg and insert it into the hole from the side reliably, the robot should perform the following steps:\n" +
            "    Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Line