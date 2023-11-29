from abc import abstractmethod,ABC

class Figure(ABC):
    def __init__(self, center):
        self.center = center

    def set_color(self, color):
        self.color = color

    @abstractmethod
    def project_to_2d(self):
        pass

    @abstractmethod
    def draw(self):
        pass
