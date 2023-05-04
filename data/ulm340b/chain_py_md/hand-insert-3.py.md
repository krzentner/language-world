

"""

class Workspace():
    def __init__(self):
        self._objects = {}
        self._gripper = {
            "x": 0.0,
            "y": 0.0,
            "is_grasped": False,
        }
    
    def objects(self):
        return self._objects
    
    def gripper(self):
        return self._gripper

    def check_is_near_object(self, object_name, object_x, object_y):
        print("check is near object: " + object_name + ", " + str(object_x) + ", " + str(object_y))
        objects = self._objects
        gripper = self._gripper
        return objects[object_name]["x"] == gripper["x"] and objects[object_name]["y"] == gripper["y"]
    
    def check_is_left_of_object(self, object_name):
        print("check is left of object: " + object_name)
        objects = self._objects
        gripper = self._gripper
        return objects[object_name]["x"] + objects[object_name]["width"] == gripper["x"] and objects[object_name]["y"] == gripper["y"]
    
    def check_is_right_of_object(self, object_name):
        print("check is right of object: " + object_name)
        objects = self._objects
        gripper = self._gripper
        return gripper["x"] == objects[object_name]["x"] + objects[object_name]["width"] and objects[object_name]["y"] == gripper["y"]
    
    def check_is_above_object(self, object_name):
        print("check is above object: " + object_name)
        objects = self._objects
        gripper = self._gripper
        return gripper["y"] == objects[object_name]["y"] + objects[object_name]["height"]
    
    def check_is_around_object(self, object_name):
        print("check is around object: " + object_name)
        objects = self._objects
        gripper = self._gripper
        return self.check_is_above_object(object_name) and (self.check_is_left_of_object(object_name) or self.check_is_right_of_object(object_name))
    
    def check_is_near_goal(