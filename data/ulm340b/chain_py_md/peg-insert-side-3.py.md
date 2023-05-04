

In this task, the robot should grab the peg from the side, and insert it into the hole, without dropping it.
You can find all of the functions and checks available here:

<table>
<tr><th>functions</th><th>checks</th></tr>
<tr><td><p><ul>
<li><code>robot.move(place)</code>: move the robot's gripper, where <code>place</code> is a string like <code>"left"</code>, <code>"right"</code>, <code>"forward"</code>, or <code>"backward"</code></li>
<li><code>robot.place(place)</code>: place the robot's gripper, where <code>place</code> is a string like <code>"left"</code>, <code>"right"</code>, <code>"forward"</code>, or <code>"backward"</code></li>
<li><code>robot.drop(place)</code>: drop the robot's gripper, where <code>place</code> is a string like <code>"left"</code>, <code>"right"</code>, <code>"forward"</code>, or <code>"backward"</code></li>
<li><code>robot.grab(object)</code>: grab <code>object</code>, where <code>object</code> is a string like <code>"puck"</code> or <code>"drawer handle"</code></li>
<li><code>robot.reach(location)</code>: reach <code>location</code>, where <code>location</code> is a string like <code>"the goal"</code> or <code>"to the button"</code></li>
<li><code>robot.slide(object)</code>: slide <code>object</code>, where <code>object</code> is a string like <code>"the puck"</code> or <code>"window closed"</code></li>
<li><code>robot.push(object)</code>: push <code>object</code>, where <code>object</code> is a string like <code>"the puck"</code> or <code>"the button"</code></li>
<li><code>robot.pull(object)</code>: pull <code>object</code>, where <code>object</code> is a string like <code>"door open"</code> or <code>"the button"</code></li>