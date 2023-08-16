import matplotlib
import numpy as np

matplotlib.use('TkAgg')
from matplotlib import pyplot as plt


class LineFittingFromClosedFormSolution:
    def __init__(self):
        self.points = []
        self.current_line = None
        self.fig = plt.figure(figsize=(8, 8), num='Linear regression closed form solution demonstration')
        grid = plt.GridSpec(1, 1)
        self.ax = self.fig.add_subplot(grid[:, :])
        self.fig.canvas.mpl_connect("button_press_event", self.on_click)
        self.ax.axis('off')
        self.ax.set_title('Linear regression: click anywhere to input data')
        self.ax.set_xlim([-5, 5])
        self.ax.set_ylim([-5, 5])
        self.ax.set_aspect(1)
        self.fig.set_tight_layout(True)
        plt.show()

    def on_click(self, event):
        if event.xdata and event.ydata:
            self.points.append([round(event.xdata, 2), round(event.ydata, 2)])
            self.ax.scatter(event.xdata, event.ydata, marker='x', color='green', linewidth=2)
            if len(self.points) > 1:
                w, b = self.get_line_parameters_w_and_b(self.points)
                x = np.array([-50, 50])
                y = w * x + b
                if self.current_line is not None:
                    self.current_line[0].remove()
                self.current_line = self.ax.plot(x, y, color='red', linewidth=2)
            self.fig.canvas.draw()

    @staticmethod
    def get_line_parameters_w_and_b(points):
        X_matrix = []
        Y_matrix = []
        for point in points:
            X_matrix.append([point[0], 1])
            Y_matrix.append([point[1]])

        X_matrix = np.asarray(X_matrix)  # m x 2
        Y_matrix = np.asarray(Y_matrix)  # m x 1
        theta = np.linalg.inv(X_matrix.T.dot(X_matrix)).dot(X_matrix.T.dot(Y_matrix))

        return theta.T[0]


if __name__ == "__main__":
    LineFittingFromClosedFormSolution()