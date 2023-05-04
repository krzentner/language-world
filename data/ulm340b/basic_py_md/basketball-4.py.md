

"""

###############################
# START OF SOLUTION
###############################

print("""
""")

def check(condition):
    if 'not' in condition:
        return not eval(condition.replace(" ",""))
    else:
        return eval(condition.replace(" ",""))

print("""
# basketball: put the ball into into the hoop
def basketball(robot):
    if check("the robot's gripper is not near the ball and the ball is below the robot's gripper"):
        robot.put("gripper above ball")
    if check("the robot's gripper is above ball and the ball is below the robot's gripper"):
        robot.push("gripper into ball")
    if check("the robot's gripper is near the ball and the ball is below the robot's gripper"):
        robot.lift("gripper with ball")
    if check("the robot's gripper is above the ball and the ball is above the robot's gripper"):
        robot.push("gripper with ball towards basket")
    if check("the robot's gripper is near basket and the ball is above the robot's gripper"):
        robot.open("gripper with ball")
""")





###############################
# END OF SOLUTION
###############################

print("""
Well done! I hope you enjoyed writing the robot program.  Thank you for your time.

We are conducting research on how people understand and generate computer programs.  Thank you for contributing to this research!
""")
[eod] [code]def dfs(x, y, t, graph):
    if graph[y][x] == 1 and t > 0:
        graph[y][x] = -1
        dfs(x + 1, y + 1, t - 1, graph)
        dfs(x + 1, y - 1, t - 1, graph)
        dfs(x - 1, y + 1, t - 1, graph)
        dfs(x - 1, y - 1, t - 1, graph)
        dfs(x + 1, y, t - 1, graph)
        dfs(x - 1, y, t - 1, graph)
        dfs(x, y + 1, t - 1, graph)
        dfs(x, y - 1, t - 1, graph)