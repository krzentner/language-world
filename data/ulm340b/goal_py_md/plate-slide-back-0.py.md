

"""


# plate-slide-back: slide the plate back into the target location
def plate_slide_back(robot):
    # Steps:
    #  1. Put gripper on plate
    #  2. Line up gripper above plate
    #  3. Push plate back into the target location
    # Put gripper on plate
    if check("the robot's gripper is not above plate"):
        robot.move_gripper("vertically aligned with plate")
    # Line up gripper above plate
    if check("the robot's gripper is above plate"):
        robot.move_gripper("forward aligned with plate")
    # Push plate back into the target location
    if check("the robot's gripper is forward aligned with plate"):
        robot.move_gripper("left of the plate")[eod] [code]import numpy as np
import matplotlib.pyplot as plt
from scipy import io

def read_data(data_path):
    data_mat=io.loadmat(data_path)
    return data_mat

def read_data_info(info_path):
    info_mat=io.loadmat(info_path)
    return info_mat

def write_data(data,file_path,format_='.mat'):
    if format_=='.mat':
        io.savemat(file_path,{'data':data})
    elif format_=='.txt':
        file=open(file_path,'w')
        for i in range(len(data)):
            for j in range(len(data[0])):
                file.write('%f \t'%(data[i][j]))
            file.write('\n')
        file.close()

def write_plot(x_data,y_data,file_path,is_label=True,format_='.pdf',
               title=None,x_label=None,y_label=None,color='k',style='-',
               save_data=False,save_data_path=None):
    num_fig=plt.figure(1)
    plt.clf()
    plt.plot(x_data,y_data,color,style)
    if title is not None:
        plt.title(title)
    if x_label is not None:
        plt.xlabel(x_label)
 