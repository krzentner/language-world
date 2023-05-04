

<details>
    <summary>Step-by-step Instructions</summary>
    <p>
    First, let's put the gripper roughly above the puck to avoid bumping it while trying to grab it:
    </p>
    <ul>
    <li>
        <code>if check(...):</code><br>
        <span style="color: #64B5F6;">The robot's gripper is not above the puck.</span><br>
        <code>robot.put(...);</code><br>
        <span style="color: #64B5F6;">The robot's gripper above the puck.</span>
    </li>
    </ul>
    <p>
    Now we can try to grab the puck. First, put the gripper around the puck, if it is not around it yet:
    </p>
    <ul>
    <li>
        <code>if check(...):</code><br>
        <span style="color: #64B5F6;">The robot's gripper is not around the puck and the robot's gripper is open.</span><br>
        <code>robot.drop(...);</code><br>
        <span style="color: #64B5F6;">The robot's gripper around the puck.</span>
    </li>
    </ul>
    <p>
    As long as the gripper is still near the puck and open, we can close the gripper around the puck:
    </p>
    <ul>
    <li>
        <code>if check(...):</code><br>
        <span style="color: #64B5F6;">The robot's gripper is near the puck and the robot's gripper is open.</span><br>
        <code>robot.close(...);</code><br>
        <span style="color: #64B5F6;">The robot's gripper around the puck.</span>
    </li>
    </ul>
    <p>
    Now that the gripper is around the puck, maybe we grabbed the puck.
    Try to move the puck backwards to the goal, and close the gripper:
    </p>
    <ul>
    <li>
        <code>if check(...):</code><br>
        <span style="color: #64B5F6;">The robot's gripper is above puck and the robot's gripper is closed.</span><br>
        <code