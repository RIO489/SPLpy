from .figure import Figure


class Cube(Figure):
    def __init__(self, center, size,scale):
        super().__init__(center)
        self.size = size
        self.scale = scale
        self.colors = {
            'front': '*',
            'back': ' ',
            'left': ' ',
            'right': ' ',
            'top': ' ',
            'bottom': ' ',
        }
        self._construct_cube()

    def apply_shadow(self):
        # Припустимо, що тінь падає на праву та нижню грань куба.
        shadow_chars = {
            'right': ':',  # Темніший символ для правої грані
            'bottom': '.',  # Темніший символ для нижньої грані
        }
        self.colors.update(shadow_chars)

    
    def _determine_shadow(self, edge):
        # Припустимо, що тінь падає з лівої верхньої сторони, 
        # тому права і нижня ребра будуть темніші
        shadow_edges = [(2, 6), (3, 2), (2, 0)]
        return edge in shadow_edges

    def _construct_cube(self):
        x, y, z = self.center
        s = self.size
        self.vertices = [
            [x - s, y - s, z - s], [x - s, y - s, z + s],
            [x - s, y + s, z - s], [x - s, y + s, z + s],
            [x + s, y - s, z - s], [x + s, y - s, z + s],
            [x + s, y + s, z - s], [x + s, y + s, z + s],
        ]
        self.edges = [
            (0, 1), (1, 3), (3, 2), (2, 0),
            (4, 5), (5, 7), (7, 6), (6, 4),
            (0, 4), (1, 5), (2, 6), (3, 7),
        ]

    def set_color(self, face, char):
        """Sets the character for a specific face of the cube."""
        valid_faces = ['front', 'back', 'left', 'right', 'top', 'bottom']
        if face not in valid_faces:
            raise ValueError(f"{face} is not a valid face of the cube. Valid faces are: {valid_faces}")
        if not isinstance(char, str) or len(char) != 1:
            raise ValueError("Color character must be a single character string.")
        self.colors[face] = char

    def isometric_projection(self):
    # Ізометрична проекція зі збільшенням масштабу для 3D координат
        projected_2d = []
        for vertex in self.vertices:
            x, y, z = vertex
            # Проекція з використанням ізометричних кутів
            iso_x = (x - z) * self.scale
            iso_y = ((x + 2 * y + z) / 2) * self.scale
            projected_2d.append((iso_x, iso_y))
        return projected_2d

    def draw_line(self, canvas, start, end, char='*'):
        # Bresenham's Line Algorithm для малювання лінії між двома точками на canvas
        x0, y0 = start
        x1, y1 = end
        dx = abs(x1 - x0)
        dy = -abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx + dy  # Помилка

        while True:
            canvas[y0][x0] = char
            if x0 == x1 and y0 == y1:
                break
            e2 = 2 * err
            if e2 >= dy:
                err += dy
                x0 += sx
            if e2 <= dx:
                err += dx
                y0 += sy

    def draw(self):
        # Створюємо полотно для малювання куба
        projection = self.isometric_projection()  # Задайте бажаний масштаб тут
        min_x = min(x for x, y in projection)
        max_x = max(x for x, y in projection)
        min_y = min(y for x, y in projection)
        max_y = max(y for x, y in projection)

        width = int(max_x - min_x) + 1
        height = int(max_y - min_y) + 1

        canvas = [[' ' for _ in range(width)] for _ in range(height)]

        # Малюємо кожне ребро куба
        for edge in self.edges:
            start = projection[edge[0]]
            end = projection[edge[1]]
            # Determine the face this edge belongs to (simplified example logic)
            face = self._determine_face(edge)
            if self._determine_shadow(edge):
                char = ':'  # Темніший символ для тіні
            else:
                char = self.colors[face]
            self.draw_line(canvas, (int(start[0] - min_x), int(start[1] - min_y)),
                           (int(end[0] - min_x), int(end[1] - min_y)), char)

        # Перетворюємо полотно у рядок для відображення
        return "\n".join("".join(row) for row in canvas)
    
    def _determine_face(self, edge):
        # Simplified logic to determine the face based on edge indices
        if edge in [(4, 5), (5, 7), (6, 7), (4, 6)]:
            return 'front'
        # Assign 'top' to top edges
        elif edge in [(0, 1), (1, 3), (2, 3), (0, 2)]:
            return 'top'
        # Assign 'left' to vertical edges on the left side of the cube
        elif edge in [(0, 4), (2, 6)]:
            return 'left'
        # Default to 'right' for other edges, assuming right side is not visible
        else:
            return 'right'
    
    def draw_2d(self):
        size = self.size * 2
        square = [[' ' for _ in range(size)] for _ in range(size)]

        # Draw the top border of the square
        for i in range(size):
            square[0][i] = self.colors['top']

        # Draw the bottom border of the square
        for i in range(size):
            square[-1][i] = self.colors['bottom']

        # Draw the left border of the square
        for i in range(1, size - 1):
            square[i][0] = self.colors['left']

        # Draw the right border of the square
        for i in range(1, size - 1):
            square[i][-1] = self.colors['right']

        # Convert the 2D array into a string for display
        return "\n".join(" ".join(row) for row in square)


    def project_to_2d(self):
        # Ізометрична проекція зі збільшенням масштабу для 3D координат
        projected_2d = []
        for vertex in self.vertices:
            x, y, z = vertex
            # Проекція з використанням ізометричних кутів
            iso_x = (x - z) * self.scale
            iso_y = ((x + 2 * y + z) / 2) * self.scale 
            projected_2d.append((iso_x, iso_y))
        return projected_2d

