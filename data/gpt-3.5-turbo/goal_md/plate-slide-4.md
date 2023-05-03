To slide the plate into the target location reliably, the robot should perform the following steps:

    Steps: 1. Put gripper above the plate 
    2. Push gripper into top of plate 
    3. Slide the plate to the target location
    
The robot can slide the plate by trapping it by pushing down on it from above and moving the gripper. If the plate isn't below the gripper as seen from above, move the gripper above the plate.
    
    - When the robot's gripper is not above the plate and the robot's gripper is not vertically aligned with the plate, 
      move the robot's gripper until the robot's gripper is vertically aligned with the plate
    
If the gripper is aligned with the plate but not near it, move the gripper down to the plate to slide it.
    
    - When the robot's gripper is vertically aligned with the plate and the robot's gripper is not near the plate, 
      move the robot's gripper until the robot's gripper is above the plate and the robot's gripper is closed
    
If the gripper is near the plate, we've probably trapped the plate and can slide it to the target location. Close the gripper to make sure we keep control of the plate.
    
    - When the robot's gripper is near the plate and the plate is below the robot's gripper, 
      move the robot's gripper until the robot's gripper is above the target location