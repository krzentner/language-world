
'''


def shape_in_shape(a_shape, b_shape):
    for point in a_shape:
        if point not in b_shape:
            return False
    return True


def object_behind_object(o1, o2):
    for point in o1.shape:
        if point in o2.shape:
            return True
    return False


def object_is_above_object(o1, o2):
    top_of_o1 = max([point[1] for point in o1.shape])
    bottom_of_o2 = min([point[1] for point in o2.shape])
    return top_of_o1 < bottom_of_o2


def object_is_left_of_object(o1, o2):
    right_of_o1 = max([point[0] for point in o1.shape])
    left_of_o2 = min([point[0] for point in o2.shape])
    return right_of_o1 < left_of_o2


def object_is_right_of_object(o1, o2):
    left_of_o1 = min([point[0] for point in o1.shape])
    right_of_o2 = max([point[0] for point in o2.shape])
    return left_of_o1 > right_of_o2


def check_object_around_object(o1, o2):
    return object_behind_object(o1, o2)


def check_object_in_front_of_object(o1, o2):
    return check_object_around_object(o2, o1)


def check_object_left_of_object(o1, o2):
    return object_is_left_of_object(o1, o2)


def check_object_right_of_object(o1, o2):
    return object_is_right_of_object(o1, o2)


def check_object_above_object(o1, o2):
    return object_is_above_object(o1, o2)


def check_object_below_object(o1, o2):
    return check_object_above_object(o2, o1)


def check_object_vertically_aligned_with_object(o1, o2):
    top1