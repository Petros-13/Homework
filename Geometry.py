import math

def trigonometry_calculator(angle_degrees):
    angle_radians = math.radians(angle_degrees)
    
    sine = math.sin(angle_radians)
    cosine = math.cos(angle_radians)
    tangent = math.tan(angle_radians)
    
    print(f"Angle: {angle_degrees}°")
    print(f"Sine: {sine}")
    print(f"Cosine: {cosine}")
    print(f"Tangent: {tangent}")

angle = float(input("Enter an angle in degrees: "))
trigonometry_calculator(angle)
