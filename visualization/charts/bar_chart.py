from typing import Dict
from visualization.core.base import BaseVisualizer

# @Incomplete
# @Robustness: I have to return this page and check everthing because this is AI Assisted
class BarChartVisualizer(BaseVisualizer):
    def __init__(self, title:str = "Data Analysis", xlabel:str=" ", ylabel:str=" ", **kwargs):
        super().__init__(title=title, **kwargs)
        self.ax.set_xlabel(xlabel)
        self.ax.set_ylabel(ylabel)
