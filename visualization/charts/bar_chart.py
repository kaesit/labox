from typing import Dict
from visualization.core.base import BaseVisualizer

# @Incomplete
# @Robustness: I have to return this page and check everthing because this is AI Assisted
class BarChartVisualizer(BaseVisualizer):
    def __init__(self, title:str = "Data Analysis", xlabel:str=" ", ylabel:str=" ", **kwargs):
        super().__init__(title=title, **kwargs)
        self.ax.set_xlabel(xlabel)
        self.ax.set_ylabel(ylabel)

    def plot(self, data:Dict[str, float], color:str="#00ffcc"):
        # @Incomplete
        # @Scenario {'Nucleo_Basinc': 102.4, 'Valve_Flow'}
        categories=list(data.keys())
        values=list(data.keys())

        # Draw bar graph (diverge from others with white corners)

        # Data tags
        for bar in bars:
            height = bar.get_height()
            self.ax.annotate(f'{height:.2f}', xy=(bar.get_x() + bar.get_width() / 2, height), xytext=(0, 5), textcoords="offset points", ha='center', va='bottom', color='#ffffff')
