
'''


def check(conditions, time_elapsed):
    for i in range(5):
        if check_step(conditions, time_elapsed):
            # print(conditions)
            # print('true')
            return True
    return False


def check_step(conditions, time_elapsed):
    conditions = conditions.split(" and ")
    for i in range(len(conditions)):
        conditions[i] = conditions[i].split()
    conditions = np.array(conditions)
    print('time', time_elapsed)

    print(conditions)
    objs = []
    for cond in conditions:
        for i in range(len(cond) - 1):
            if cond[i] not in ['not', 'the', 'above', 'below', 'above', 'behind', 'near', 'in front of', 'around',
                              'left of', 'right of', 'forward aligned with', 'vertically aligned with',
                              'horizontally aligned with', 'to the side of', 'in the center of']:
                objs.append(cond[i])

    for i in range(len(objs) - 1):
        if len(objs) == 0:
            return True
        dist_x = np.linalg.norm(objs[i].position[0] - objs[i + 1].position[0])
        dist_y = np.linalg.norm(objs[i].position[1] - objs[i + 1].position[1])
        print(objs[i], dist_x, dist_y)
        if objs[i].position[2] > objs[i + 1].position[2]:
            above = True
        else:
            above = False
        if dist_x < 0.15 and dist_y < 0.15:
            if above:
                if objs[i].position[0] < objs[i + 1].position[0]:
                    if objs[i].position[1] > objs[i + 1].position[1]:
                        print("robot's gripper is around " + str(objs[i + 1]))
                        return True
                elif objs[i].position[0] > objs[i + 1].position[0]:
                    if objs[i