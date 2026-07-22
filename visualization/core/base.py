from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
from typing import Dict, Any

class BaseVisualizer(ABC):
    # Base Class for All Visualization in LABOX
    def __init__(self, title: str = "Labox Telemetry", width: float = 10.0, height: float = 6.0):
        self.title = title
        plt.style.use("dark_background")
        plt.rcParams.update({
            "font.family": "monospace",
            "font.monospace": ["JetBrains Mono", "Cascadia Code", "Consolas", "Courier New"],
            "axes.facecolor": "#0a0a0a",
            "figure.facecolor": "#050505",
            "axes.edgecolor": "#333333",
            "axes.labelcolor": "#cccccc",
            "axes.grid": True,
            "grid.color": "#1f1f1f",
            "grid.linestyle": "--",
            "text.color": "#e0e0e0",
            "xtick.color": "#888888",
            "ytick.color": "#888888",
        })
        
        self.fig, self.ax = plt.subplots(figsize=(width, height))
        self.ax.set_title(self.title, color="#ffffff", pad=15, weight='bold')

    @abstractmethod
    # @Override
    def plot(self, data: Dict[str, Any], **kwargs):
        pass

    def save(self, filepath: str, dpi: int = 300):
        # Writes the produced graph on disc (for storage module integration).
        self.fig.savefig(filepath, dpi=dpi, bbox_inches='tight')

    def render(self):
        # Shows the Grahp on Screen, for CLI and Development Tests
        plt.tight_layout()
        plt.show()
