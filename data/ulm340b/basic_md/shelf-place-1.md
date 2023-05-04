
    
    """
    print(question)
    return question


def instructions_shelf_place():
    question = """The task `shelf-place` requires the robot to pick up the block and place it at the target location.
To pick up the block and place it at the target location reliably, the robot should perform the following steps:
    - When the robot's gripper is not above block, the robot should put gripper above block.
    - When the robot's gripper is not around block and the robot's gripper is open, the robot should drop gripper around block.
    - When the robot's gripper is near block and the robot's gripper is open, the robot should close gripper around block.
    - When the robot's gripper is above block and the robot's gripper is closed, the robot should place block on goal.

The task `hook-hang` requires the robot to pick up the ring and place it on the target location.
To pick up the ring and place it on the target location reliably, what steps the robot should perform?
    
    """
    print(question)
    return question


def instructions_hook_hang():
    question = """The task `hook-hang` requires the robot to pick up the ring and place it on the target location.
To pick up the ring and place it on the target location reliably, the robot should perform the following steps:
    - When the robot's gripper is not above ring, the robot should put gripper above ring.
    - When the robot's gripper is not around ring and the robot's gripper is open, the robot should drop gripper around ring.
    - When the robot's gripper is near ring and the robot's gripper is open, the robot should close gripper around ring.
    - When the robot's gripper is above ring and the robot's gripper is closed, the robot should place ring on goal.

The task `stick-push` requires the robot to move the stick to the target location.
To move the stick to the target location reliably, the robot should perform the following steps:
    - When the robot's gripper is not above stick and the robot's gripper is not almost vertically aligned with stick, the robot should put gripper above stick.
    - When the robot's gripper is almost vertically aligned with stick and the robot's gripper is not near stick, the robot should grab stick.
    - When the robot's gripper is near stick and the robot's gripper is not open, the robot should put gripper around stick.
    - When the robot's gripper is around