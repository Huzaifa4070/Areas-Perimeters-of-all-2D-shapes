#Program for Areas and Perimeters for all two-dimentaional shapes
#This code covers the following 2D shapes: 
#SQUARE
#RECTANGLE
#TRIANGLE
#CIRCLE
#RHOMBUS
#PARALLELOGRAM
#KITE
#TRAPEZIUM




#SQAURE

#Input
length_of_square = 7

#Code
area_of_square = length_of_square ** 2
perimeter_of_square = 4 * length_of_square
print('Area of the Square = ' + str(area_of_square))
print('Perimeter of the Square = ' + str(perimeter_of_square))
print(' ')




#RECTANGLE

#Input
length_of_rectangle = 4
width_of_rectangle = 6

#Code
area_of_rectangle = length_of_rectangle * width_of_rectangle
perimeter_of_rectangle = 2 * (length_of_rectangle + width_of_rectangle)
print('Area of the Rectangle = ' + str(area_of_rectangle))
print('Perimeter of the Rectangle = ' + str(perimeter_of_rectangle))
print(' ')




#TRIANGLE

#Input
base_of_triangle = 3
height_of_triangle = 4
hypotenuse_of_triangle = 5 

#Code
area_of_triangle = 0.5 * base_of_triangle * height_of_triangle
perimeter_of_triangle = base_of_triangle + height_of_triangle + hypotenuse_of_triangle 
print('Area of the Triangle = ' + str(area_of_triangle))
print('Perimeter of the Triangle = ' + str(perimeter_of_triangle))
print(' ')




#CIRCLE

#Input 
radius_of_circle = 7

#Code
import math 
area_of_circle = math.pi * radius_of_circle ** 2
rounded_area_of_circle = round(area_of_circle)
circumference_of_circle = 2 * math.pi * radius_of_circle
rounded_circumference_of_circle = round(circumference_of_circle)
print('Area of the Circle = ' + str(rounded_area_of_circle))
print('Circumference of the Circle = ' + str(rounded_circumference_of_circle))
print(' ')




#RHOMBUS

#Input
side_of_rhombus = 10
first_diagonal_of_rhombus = 16
second_diagonal_of_rhombus = 12 

#Code
area_of_rhombus = (first_diagonal_of_rhombus * second_diagonal_of_rhombus) / 2
perimeter_of_rhombus = 4 * side_of_rhombus
print('Area of the Rhombus = ' + str(area_of_rhombus))
print('Perimeter of the Rhombus = ' + str(perimeter_of_rhombus))
print(' ')




#PARALLELOGRAM

#Input
length_of_parallelogram = 5
base_of_parallelogram = 7
height_of_parallelogram = 9

#Code
area_of_parallelogram = base_of_parallelogram * height_of_parallelogram
perimeter_of_parallelogram = 2 * (base_of_parallelogram + length_of_parallelogram)  
print('Area of the Parallelogram = ' + str(area_of_parallelogram))
print('Perimeter of the Parallelogram = ' + str(perimeter_of_parallelogram))
print(' ')




#KITE

#Input
shorter_side_of_kite = 14.1
longer_side_of_kite = 22.4
shorter_diagoal_of_kite = 20
longer_diagonal_of_kite = 30

#Code
area_of_kite = 0.5 * shorter_diagoal_of_kite * longer_diagonal_of_kite
perimeter_of_kite = 2 * (shorter_side_of_kite + longer_side_of_kite)
print('Area of the Kite = ' + str(area_of_kite))
print('Perimeter of the Kite = ' + str(perimeter_of_kite))
print(' ')




#TRAPEZIUM

#Input
shorter_parallel_side_of_trapezium = 4
longer_parallel_side_of_trapezium = 7
third_side_of_trapezium = 5
fourth_side_of_trapezium = 6
height_of_trapezium = 4

#Code
area_of_trapezium = 0.5 * (shorter_parallel_side_of_trapezium + longer_parallel_side_of_trapezium) * height_of_trapezium
perimeter_of_trapezium = shorter_parallel_side_of_trapezium + longer_parallel_side_of_trapezium + third_side_of_trapezium + fourth_side_of_trapezium
print('Area of the Trapezium = ' + str(area_of_trapezium))
print('Perimeter of the Trapezium = ' + str(perimeter_of_trapezium))
print(' ')
