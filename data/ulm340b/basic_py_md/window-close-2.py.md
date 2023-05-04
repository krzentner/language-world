

Then, write a series of if-checks, such as:

```
if check("something is true"):
    robot.do("something")
```

For example:

```
if check("the robot's gripper is not vertically aligned with drawer handle"):
    robot.put("gripper above drawer handle")
```

We have recorded some robot trajectories to get started. The robot was trying to perform `window-close`, but couldn't quite figure it out:

```
0: robot.do("close")
1: robot.do("open")
2: robot.do("close")
3: robot.do("close")
4: robot.do("close")
5: robot.do("close")
6: robot.do("open")
7: robot.do("open")
8: robot.do("close")
9: robot.do("close")
10: robot.do("open")
11: robot.do("open")
12: robot.do("close")
13: robot.do("close")
14: robot.do("open")
15: robot.do("open")
16: robot.do("close")
17: robot.do("open")
18: robot.do("open")
19: robot.do("close")
20: robot.do("open")
21: robot.do("close")
22: robot.do("close")
23: robot.do("open")
24: robot.do("open")
25: robot.do("open")
26: robot.do("close")
27: robot.do("close")
28: robot.do("close")
29: robot.do("open")
30: robot.do("close")
31: robot.do("close")
32: robot.do("open")
33: robot.do("close")
34: robot.do("close")
35: robot.do("open")
36: robot.do("open")
37: robot.do("close")
38: robot.do("close")
39: robot.do("open")
40: robot.do("close")
41: robot.do("close")
42: robot.do("open")
43: robot.do("open")
44: robot.do("close")
45: robot.do("close")
46: robot.do("open")
47: robot.do("close")
48: robot.do("close")
49