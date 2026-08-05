import numpy as np

class Visualizer3D:
        def __init__(self):
            self.fig = plt.figure()
            self.ax = self.fig.add_subplot(111, projection='3d')

        def ascii_cube(self):
            try:
                # Simple ASCII representation of a cube
                print("-----")
                print("|   |")
                print("|   |")
                print("-----")
            except Exception as e:
                print(f"Error: {e}")

        def cube(self, size=1.0):
            try:
                # Coordinates for the vertices of a cube
                vertices = np.array([
                    [-size/2, -size/2, -size/2],
                    [size/2, -size/2, -size/2],
                    [size/2, size/2, -size/2],
                    [-size/2, size/2, -size/2],
                    [-size/2, -size/2, size/2],
                    [size/2, -size/2, size/2],
                    [size/2, size/2, size/2],
                    [-size/2, size/2, size/2]
                ])
                edges = [
                    [0, 1], [1, 2], [2, 3], [3, 0],
                    [4, 5], [5, 6], [6, 7], [7, 4],
                    [0, 4], [1, 5], [2, 6], [3, 7]
                ]
                for edge in edges:
                    self.ax.plot3D(vertices[edge, 0], vertices[edge, 1], vertices[edge, 2])
                plt.show()
            except Exception as e:
                print(f"Error: {e}")


        def sphere(self, radius=1.0):
            try:
                u = np.linspace(0, 2 * np.pi, 50)
                v = np.linspace(0, np.pi, 50)
                x = radius * np.outer(np.cos(u), np.sin(v))
                y = radius * np.outer(np.sin(u), np.sin(v))
                z = radius * np.outer(np.ones(np.size(u)), np.cos(v))

                self.ax.plot_surface(x, y, z, color='b')
                plt.show()
            except Exception as e:
                print(f"Error: {e}")


        def torus(self, R=2.0, r=1.0):
            try:
                u = np.linspace(0, 2 * np.pi, 50)
                v = np.linspace(0, 2 * np.pi, 50)
                x = (R + r * np.cos(v)) * np.cos(u)
                y = (R + r * np.cos(v)) * np.sin(u)
                z = r * np.sin(v)

                self.ax.plot_surface(x, y, z, color='g')
                plt.show()
            except Exception as e:
                print(f"Error: {e}")


        def spiral(self):
            try:
                t = np.linspace(0, 10 * np.pi, 50)
                x = t * np.cos(t)
                y = t * np.sin(t)
                z = t

                self.ax.plot3D(x, y, z)
                plt.show()
            except Exception as e:
                print(f"Error: {e}")


        def save_png(self, filename='output.png'):
            try:
                self.fig.savefig(filename)
            except Exception as e:
                print(f"Error: {e}")


        def menu(self):
            try:
                while True:
                    print("\n3D Visualizer Menu:")
                    print("1. Cube")
                    print("2. Sphere")
                    print("3. Torus")
                    print("4. Spiral")
                    print("5. Save PNG")
                    print("6. ASCII Cube")
                    print("0. Exit")

                    choice = input("Enter your choice: ")

                    if choice == '1':
                        size = float(input("Enter cube size: "))
                        self.cube(size)
                    elif choice == '2':
                        radius = float(input("Enter sphere radius: "))
                        self.sphere(radius)
                    elif choice == '3':
                        R = float(input("Enter torus major radius (R): "))
                        r = float(input("Enter torus minor radius (r): "))
                        self.torus(R, r)
                    elif choice == '4':
                        self.spiral()
                    elif choice == '5':
                        filename = input("Enter filename to save PNG: ")
                        self.save_png(filename)
                    elif choice == '6':
                        self.ascii_cube()
                    elif choice == '0':
                        print("Exiting...")
                        break
                    else:
                        print("Invalid choice. Please try again.")
            except Exception as e:
                print(f"Error: {e}")
