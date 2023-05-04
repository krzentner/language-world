

and then insert code to perform the task, given this situation:

"""
import matplotlib.pyplot as plt

def display(robot, title=None):
    # Render the image
    fig = plt.figure(figsize=(6, 6), facecolor='white')
    ax = fig.add_subplot(111, projection='3d')

    # Draw the table
    table_x, table_y, table_z = robot.get_table_coordinates()
    ax.plot_wireframe(table_x, table_y, table_z, color=(.5,.5,.5))

    # Draw the robot
    robot.draw(ax)
    ax.set_xlim(0, robot.table_size)
    ax.set_ylim(0, robot.table_size)
    ax.set_zlim(0, robot.table_height)
    ax.view_init(30, -160)
    ax.dist = 10

    plt.axis('off')
    if title is not None:
        plt.title(title)
    plt.show()

class Robot:

    def __init__(self):
        self.grip_width = 0.13
        self.grip_thickness = 0.04

    def draw(self, ax):
        grip_x, grip_y, grip_z = self.get_gripper_coordinates()
        grip_center_x, grip_center_y, grip_center_z = 0.5 * (grip_x[0] + grip_x[1]), \
            0.5 * (grip_y[0] + grip_y[1]), 0.5 * (grip_z[0] + grip_z[1])
        ax.plot(grip_x[0], grip_y[0], grip_z[0], color=(1,0,0))
        ax.plot(grip_x[1], grip_y[1], grip_z[1], color=(0,0,1))
        ax.plot([grip_center_x] * 2, [grip_center_y] * 2, [grip_center_z] * 2, color=(0,1,0))

    def get_table_coordinates(self):
        table_x = [[-0.5] * 4,