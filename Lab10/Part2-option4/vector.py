from math import hypot, acos, degrees, cos, sin, radians

class Vector:
    '''The class of a vector in two-dimensional space'''
    def __init__(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord

    def is_null_vector(self):
        if self.x_coord == 0 and self.y_coord == 0:
            return True
        return False

    def get_x_angle(self):
        '''Angle with x axis'''
        if self.is_null_vector():
            return 0
        return degrees(acos(self.x_coord / hypot(self.x_coord, self.y_coord)))
    
    def get_y_angle(self):
        '''Angle with y axis'''
        if self.is_null_vector():
            return 0
        return degrees(acos(self.y_coord / hypot(self.x_coord, self.y_coord)))
    
    def get_angle_between(self, vector):
        '''Angle between vectors'''
        if self.is_null_vector() or vector.is_null_vector() or\
                self.x_coord * vector.y_coord == vector.x_coord * self.y_coord:
            return 0
        return degrees(acos((vector.x_coord*self.x_coord + vector.y_coord*self.y_coord) / 
                            (hypot(vector.x_coord, vector.y_coord)*hypot(self.x_coord, self.y_coord))))
    
    def get_scalar_product(self, vector):
        '''Scalar product between vectors'''
        print(cos(radians(self.get_angle_between(vector))))
        return hypot(vector.x_coord, vector.y_coord)*hypot(self.x_coord, self.y_coord)*cos(radians(self.get_angle_between(vector)))
    
    def get_vector_product(self, vector):
        '''Vector product between vectors'''
        return hypot(vector.x_coord, vector.y_coord)*hypot(self.x_coord, self.y_coord)*sin(radians(self.get_angle_between(vector)))
    