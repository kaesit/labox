import os, sys


class AnomalyDetector():
    def __init__(self):
        pass
    
    def run(self):
        pass

    def fetch_anomaly_classes(self, handler, url:str):
        """ This function will fetch anomaly classes and determine which is going to be the anomaly type to detect mainly"""
        pass


class AnomalyModel(self):
    def __init__(self, context_length: int = 0, heat_score: float = 0):
        self.context_length = context_length
        self.heat_score = heat_score

    @property
    def heat_score(self) -> float:
        return _heat_score

    @heat_score.setter
    def heat_score(self, data: float):
        self._heat_score = data
    @heat_score.deleter
    def heat_score(self):
        del _heat_score



