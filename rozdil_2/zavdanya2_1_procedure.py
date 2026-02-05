import math

def calculate_rectangle_area(width, height):
    return width * height

def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

rect_w, rect_h = 10, 5
circle_r = 7

print("--- Процедурний підхід ---")
area1 = calculate_rectangle_area(rect_w, rect_h)
print(f"Площа прямокутника: {area1}")

area2 = calculate_circle_area(circle_r)
print(f"Площа кола: {area2:.2f}")