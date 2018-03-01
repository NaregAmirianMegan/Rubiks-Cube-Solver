"""
@author: Nareg
"""

import numpy as np

#allow printing of all of numpy array
np.set_printoptions(threshold=np.inf)

def rotate_matrix(matrix, direction):
    if(direction == "C"):
        #rotate corners
        ##top left to top right
        ##top right to bottom right
        ##bottom right to bottom left
        ##bottom left to top right
        top_right = matrix[0][0]
        bottom_right = matrix[0][len(matrix[0])-1]
        bottom_left = matrix[len(matrix)-1][len(matrix[0])-1]
        top_left = matrix[len(matrix)-1][0]
        matrix[0][0] = top_left
        matrix[0][len(matrix[0])-1] = top_right
        matrix[len(matrix)-1][len(matrix[0])-1] = bottom_right
        matrix[len(matrix)-1][0] = bottom_left

        #rotate side centers
        ##left side to top side
        ##top side to right side
        ##right side to bottom side
        ##bottom side to left side
        top = matrix[int(len(matrix)/2)][0]
        right = matrix[0][int(len(matrix[0])/2)]
        bottom = matrix[int(len(matrix)/2)][len(matrix[0])-1]
        left = matrix[len(matrix)-1][int(len(matrix[0])/2)]
        matrix[int(len(matrix)/2)][0] = left
        matrix[0][int(len(matrix[0])/2)] = top
        matrix[int(len(matrix)/2)][len(matrix[0])-1] = right
        matrix[len(matrix)-1][int(len(matrix[0])/2)] = bottom

    elif(direction == "CC"):
        #rotate corners
        ##top right to top left
        ##top left to bottom left
        ##bottom left to bottom right
        ##bottom right to top right
        top_left = matrix[0][len(matrix[0])-1]
        bottom_left = matrix[0][0]
        bottom_right = matrix[len(matrix)-1][0]
        top_right = matrix[len(matrix)-1][len(matrix[0])-1]
        matrix[0][0] = top_left
        matrix[len(matrix)-1][0] = bottom_left
        matrix[len(matrix)-1][len(matrix[0])-1] = bottom_right
        matrix[0][len(matrix[0])-1] = top_right

        #rotate side centers
        ##top side to left side
        ##left side to bottom side
        ##bottom side to right side
        ##right side to top side
        top = matrix[int(len(matrix)/2)][len(matrix[0])-1]
        left = matrix[0][int(len(matrix[0])/2)]
        bottom = matrix[int(len(matrix)/2)][0]
        right = matrix[len(matrix)-1][int(len(matrix[0])/2)]
        matrix[0][int(len(matrix[0])/2)] = top
        matrix[int(len(matrix)/2)][0] = left
        matrix[len(matrix)-1][int(len(matrix[0])/2)] = bottom
        matrix[int(len(matrix)/2)][len(matrix[0])-1] = right


class Cube():
    def __init__(self):
        #preset = solved cube matrix
        self.state = np.array([[3,3,3, 1,1,1, 4,4,4],
                               [3,3,3, 1,1,1, 4,4,4],
                               [3,3,3, 1,1,1, 4,4,4],

                               [6,6,6, 5,5,5, 2,2,2],
                               [6,6,6, 5,5,5, 2,2,2],
                               [6,6,6, 5,5,5, 2,2,2]])

    def show(self):
        print(self.state)

    def move(self, move):
        if(move == "F"):
            #rotate center clockwise
            tmp = np.array(self.state[0:3,3:6])
            rotate_matrix(tmp, "C")
            self.state[0:3,3:6] = tmp[0:3,0:3]

            #orange right column goes to blue bottom row
            #blue bottom row goes to red left column
            #red left column goes to green top row
            #green top row goes to orange right column
            blue_bottom = np.fliplr([np.array(self.state[0:3,2])])[0]
            red_left = np.array(self.state[5][0:3])
            green_top = np.fliplr([np.array(self.state[0:3,6])])[0]
            orange_right = np.array(self.state[3][3:6])
            self.state[5][0:3] = blue_bottom[0:3]
            self.state[0:3,6] = red_left[0:3]
            self.state[3][3:6] = green_top[0:3]
            self.state[0:3,2] = orange_right[0:3]

        elif(move == "F'"):
            #rotate center clockwise
            tmp = np.array(self.state[0:3,3:6])
            rotate_matrix(tmp, "CC")
            self.state[0:3,3:6] = tmp[0:3,0:3]

            #blue bottom row goes to orange right column
            #orange right column goes to green top row
            #green top row goes to red left column
            #red left column goes to blue bottom row
            blue_bottom = np.array(self.state[0:3,6])
            red_left = np.array(self.state[3][3:6])
            green_top = np.array(self.state[0:3,2])
            orange_right = np.array(self.state[5][0:3])
            self.state[5][0:3] = blue_bottom[0:3]
            self.state[0:3,6] = red_left[0:3]
            self.state[3][3:6] = green_top[0:3]
            self.state[0:3,2] = orange_right[0:3]

        elif(move == "B"):
            #rotate center clockwise
            tmp = np.array(self.state[3:6,6:9])
            rotate_matrix(tmp, "C")
            self.state[3:6,6:9] = tmp[0:3,0:3]

            #blue top row goes to orange left column
            #orange left column goes to green bottom row
            #green bottom row goes to red right column
            #red right column goes to blue top row
            blue_top = np.array(self.state[0:3,8])
            red_right = np.array(self.state[5][3:6])
            green_bottom = np.array(self.state[0:3,0])
            orange_left = np.array(self.state[3][0:3])
            self.state[3][0:3] = blue_top[0:3]
            self.state[0:3,8] = red_right[0:3]
            self.state[5][3:6] = green_bottom[0:3]
            self.state[0:3,0] = orange_left[0:3]

        elif(move == "B'"):
            #rotate center counter-clockwise
            tmp = np.array(self.state[3:6,6:9])
            rotate_matrix(tmp, "CC")
            self.state[3:6,6:9] = tmp[0:3,0:3]

            

cube = Cube()

cube.show()

print("\n")

cube.move("B")

cube.show()
