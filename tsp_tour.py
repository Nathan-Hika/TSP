class Tour:
    class Node:
        def __init__(self, p):
            self.p = p
            self.next = None

    def __init__(self):
        self.first = None
    # Print the tour to standard output
    def show(self):
        current = self.first
        while current.next != self.first:
            print(current.p)
            current = current.next
        print(current.p)

    # Draw the tour using standard draw
    def draw(self):
        current = self.first
        while current.next != self.first:
            current.p.drawTo(current.next.p)
            current = current.next
        current.p.drawTo(self.first.p)

    # Return the total distance of the tour
    def distance(self):
        total_distance = 0.0
        current = self.first
        while current.next != self.first:
            total_distance += current.p.distanceTo(current.next.p)
            current = current.next
        total_distance += current.p.distanceTo(self.first.p)
        return total_distance

    # Insert a new point using the smallest increase insertion heuristic
    def insert_smallest(self, p):
        if self.first is None:
            new_node = Tour.Node(p)
            new_node.next = new_node  # Set the next node to itself for a circular tour
            self.first = new_node
            return

        best_node = None
        min_increase = float("inf")

        current = self.first
        while True:
            increase = current.p.distanceTo(p) + p.distanceTo(current.next.p) - current.p.distanceTo(current.next.p)
            if increase < min_increase:
                best_node = current
                min_increase = increase
            current = current.next
            if current == self.first:
                break

        new_node = Tour.Node(p)
        new_node.next = best_node.next
        best_node.next = new_node

    def insert_nearest(self, p):
        new_node = Tour.Node(p)
        if self.first is None:
            new_node.next = new_node  # Set the next node to itself for a circular tour
            self.first = new_node
            return

        closest_node = None
        min_distance = float("inf")

        current = self.first
        while True:
            distance = current.p.distanceTo(p)
            if distance < min_distance:
                closest_node = current
                min_distance = distance
            current = current.next
            if current == self.first:
                break

        new_node.next = closest_node.next
        closest_node.next = new_node

    # Insert a new point using the nearest neighbor heuristic
    def insert_nearest(self, p):
        new_node = Tour.Node(p)
        if self.first is None:
            new_node.next = new_node  # Set the next node to itself for a circular tour
            self.first = new_node
            return

        closest_node = None
        min_distance = float("inf")

        current = self.first
        while current.next != self.first:
            distance = current.p.distanceTo(p)
            if distance < min_distance:
                closest_node = current
                min_distance = distance
            current = current.next
        if closest_node is None:
            closest_node = self.first

        new_node.next = closest_node.next 
        closest_node.next = new_node