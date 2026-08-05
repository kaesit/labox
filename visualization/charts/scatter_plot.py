from typing import Dict
from visualization.core.base import BaseVisualizer

# @Incomplete

class ScatterPlot(BaseVisualizer):
    def __init__(self, title: str = "Data Analysis", xlabel:str=" ", ylabel:str=" ", **kwargs):
        super()__init(title=title, **kwargs)
        self.ax.set_xlabel(xlabel)
        self.ax.set_ylabel(ylabel)

    def plot(self, data:Dict[str, float], color="#00ffcc"):
        # @Incomplete
        categories = list(data.keys())
        values = list(data.values())
        
