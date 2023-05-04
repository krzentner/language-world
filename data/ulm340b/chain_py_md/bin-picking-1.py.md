

Please write your code in the editor. 

## Data Types

The following data types are defined for the robot:

- gripper_opened -- true when the robot's gripper is open
- gripper_closed -- true when the robot's gripper is closed
- above -- true when the robot's gripper is above the object specified by the next parameter
- below -- true when the robot's gripper is below the object specified by the next parameter
- in_front_of -- true when the robot's gripper is in front of the object specified by the next parameter
- behind -- true when the robot's gripper is behind the object specified by the next parameter
- to_left_of -- true when the robot's gripper is left of the object specified by the next parameter
- to_right_of -- true when the robot's gripper is right of the object specified by the next parameter
- aligned_vertically_with -- true when the robot's gripper is aligned vertically with the object specified by the next parameter
- aligned_horizontally_with -- true when the robot's gripper is aligned horizontally with the object specified by the next parameter
- near -- true when the robot's gripper is near the object specified by the next parameter
- far -- true when the robot's gripper is far from the object specified by the next parameter
- forward_aligned_with -- true when the robot's gripper is forward aligned with the object specified by the next parameter
- around -- true when the robot's gripper is around the object specified by the next parameter
- not_around -- true when the robot's gripper is not around the object specified by the next parameter
- at -- true when the robot's gripper is at the location specified by the next parameter
- not_at -- true when the robot's gripper is not at the location specified by the next parameter
- reachable -- true when the robot's gripper can reach the location specified by the next parameter
- not_reachable -- true when the robot's gripper cannot reach the location specified by the next parameter

## Actions

The following actions can be performed with the robot:

- put(x): moves the robot's gripper to location x
- place(x): moves the robot's gripper to location x
- reach(x): tries to reach the robot's gripper to location x
- grab(x): tries to close the robot's gripper around object x
- close(x): closes the robot's gripper around object x
- drop(x): drops the robot's gripper around object x
- insert(x): inserts the robot's gripper into hole x
