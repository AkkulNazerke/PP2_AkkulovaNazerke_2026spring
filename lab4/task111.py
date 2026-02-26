import math
R = float(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

def distance(a, b):
    return math.hypot(a[0]-b[0], a[1]-b[1])

def angle(x, y):
    return math.atan2(y, x)

def shortest_path(R, A, B):
    # Check if line intersects circle
    def line_circle_intersection(A, B):
        # Circle at origin
        ax, ay = A
        bx, by = B
        dx, dy = bx - ax, by - ay
        a = dx**2 + dy**2
        b = 2*(ax*dx + ay*dy)
        c = ax**2 + ay**2 - R**2
        disc = b**2 - 4*a*c
        if disc < 0:
            return False
        t1 = (-b - math.sqrt(disc))/(2*a)
        t2 = (-b + math.sqrt(disc))/(2*a)
        return (0 < t1 < 1) or (0 < t2 < 1)
    
    if not line_circle_intersection(A,B):
        return distance(A,B)
    
    # Distances from points to origin
    DA = distance(A, (0,0))
    DB = distance(B, (0,0))
    
    # Tangent lengths
    LA = math.sqrt(DA**2 - R**2)
    LB = math.sqrt(DB**2 - R**2)
    
    # Angles to points
    alphaA = angle(A[0], A[1])
    alphaB = angle(B[0], B[1])
    
    # Angle of tangent line from point
    thetaA = math.acos(R/DA)
    thetaB = math.acos(R/DB)
    
    # Arc angle
    dphi = abs(alphaB - alphaA) - thetaA - thetaB
    # Normalize to [0,2pi]
    while dphi < 0:
        dphi += 2*math.pi
    
    arc_length = R * dphi
    
    return LA + LB + arc_length

length = shortest_path(R, (x1,y1), (x2,y2))
print(f"{length:.10f}")

