

"""

from util import load_image, save_image, get_screen, is_number, color_text

def check_function(obj1, obj2, relation):
    """
    Checks if objects in obj1 and obj2 are related in the way
    specified by the relation text.
    """
    if relation == "is near":
        return np.linalg.norm(np.array(obj1) - np.array(obj2)) < 0.2
    elif relation == "is not near":
        return np.linalg.norm(np.array(obj1) - np.array(obj2)) > 0.2
    elif relation == "is not above":
        return np.array(obj1)[1] - np.array(obj2)[1] < -0.15
    elif relation == "is not below":
        return np.array(obj1)[1] - np.array(obj2)[1] > 0.15
    elif relation == "is not right of":
        return np.array(obj1)[0] - np.array(obj2)[0] < -0.1
    elif relation == "is not left of":
        return np.array(obj1)[0] - np.array(obj2)[0] > 0.1
    elif relation == "is vertically aligned with":
        return np.abs(np.array(obj1)[1] - np.array(obj2)[1]) < 0.1
    elif relation == "is not vertically aligned with":
        return np.abs(np.array(obj1)[1] - np.array(obj2)[1]) > 0.1
    elif relation == "is above":
        return np.abs(np.array(obj1)[0] - np.array(obj2)[0]) < 0.15 and np.array(obj1)[1] - np.array(obj2)[1] > 0.05
    elif relation == "is below":
        return np.abs(np.array(obj1)[0] - np.array(obj2)[0]) < 0.15 and np.array(obj1)[1] - np.array(obj2)[1] < -0.05
    elif relation == "is left of":
        return np.array(obj1)[0] - np.array(obj2)[0] > 0.05
    elif relation == "is right of":
        return np.array(obj1)[0] - np.array(obj2