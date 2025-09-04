import numpy as np
import matplotlib.pyplot as plt # for creating static,animation and interactive visualization

def classify_conic(A, B, C, D, E, F):
    discriminant = B**2 - 4*A*C 
    if discriminant < 0:
        if A == C and B == 0:
            return "Circle"   #if A=C=1
        else:
            return "Ellipse"   #ifb2-4ac<0 and 0<e<1 
    elif discriminant == 0:
        return "Parabola"  #ifb2-4ac=0 and e=1
    else:
        return "Hyperbola" # if b2-4ac>0 and e>1

def plot_conic(A, B, C, D, E, F):
    x_vals = np.linspace(-20, 20, 1000) #Here, 1000 points are generated from -20 to 20 for both x and y.
    y_vals = np.linspace(-20, 20, 1000)
    x, y = np.meshgrid(x_vals, y_vals)# rectangular grid Turns 1D x and y arrays into 2D grid arrays.



    Z = A*x**2 + B*x*y + C*y**2 + D*x + E*y + F
    conic_type = classify_conic(A, B, C, D, E, F)

    plt.figure(figsize=(15,15))
    try:
        contour = plt.contour(x, y, Z, levels=[0], colors='blue')
        if len(contour.allsegs[0]) == 0:
            raise ValueError("No visible contour found")
        plt.title(f"{conic_type}:\n{A}x² + {B}xy + {C}y² + {D}x + {E}y + {F} = 0")
    except Exception as e:
        plt.title(f"Could not plot conic ({conic_type}): {e}")

    plt.axhline(0, color='black', lw=0.5)
    plt.axvline(0, color='black', lw=0.5)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.tight_layout()
    plt.show()
def main():
    print("General equation of sections of conics")
    print("Enter coefficients for the general conic equation:")
    print("-----------------------------------")
    print("Ax² + Bxy + Cy² + Dx + Ey + F = 0")
    print("-----------------------------------")

    try:
        A = float(input("Enter A: "))
        B = float(input("Enter B: "))
        C = float(input("Enter C: "))
        D = float(input("Enter D: "))
        E = float(input("Enter E: "))
        F = float(input("Enter F: "))

        print(f"Equation: {A}x² + {B}xy + {C}y² + {D}x + {E}y + {F} = 0")
        conic_type = classify_conic(A, B, C, D, E, F)
        print(f"Identified conic: {conic_type}")
        plot_conic(A, B, C, D, E, F)

    except ValueError:
        print("Invalid input. Please enter numeric values only.")

main()
