import math

def area_of_circle(radius):
	return math.pi * math.pow(radius, 2)

def area_of_triangle(a, b, c):
	P_half = (a + b + c)/2
	return (P_half*(P_half-a)*(P_half-b)*(P_half-c)) ** 0.5

def area_of_rectangle(a, b):
	return a * b

def area_any_shape(a, b=None, c=None):
	if c is not None:
		return area_of_triangle(a, b, c)
	if b is not None:
		return area_of_rectangle(a, b)
	return area_of_circle(a)
	
def is_right_triangle(a, b, c):
	return (a*a+b*b==c*c) or (c*c+b*b==a*a) or (a*a+c*c==b*b)
