from tsp_tour import Tour
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distanceTo(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def __str__(self):
        return f"({self.x}, {self.y})"


# Create a set of points
points = [
    Point(0, 0),
    Point(1, 1),
    Point(2, 2),
    Point(3, 3),
    Point(4, 4)
]

# Create an empty tour
tour = Tour()

# Insert points using the smallest increase insertion heuristic
for point in points:
    tour.insert_smallest(point)

# Print the tour and its distance
tour.show()
print("Total distance:", tour.distance())

# Clear the tour
tour = Tour()

# Insert points using the nearest neighbor heuristic
for point in points:
    tour.insert_nearest(point)

# Print the tour and its distance
tour.show()
print("Total distance:", tour.distance())