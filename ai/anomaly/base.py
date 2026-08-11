import os, sys
from typing import Dict, Optional, Any, 
import time

# @Metric, it is 120K miliseconds which equals to 2 minutes
# 2 minutes is determined and final time for to spend to detect or diagnose each anomaly, this variable can be modified depends on amount of anomalies the platform deals with, but in use case of average 2 anomalies, should be detected/diagnosed maximumly in 4 minutes that is the limit 
AVERAGE_TIME = 1200000

class AnomalyDetector():
    def __init__(self, cases: Dict[str, Any]):
        self.cases = cases
        amnt_cases = len(self.cases) # This detects amount of cases to diagnose anomalies
        print(amnt_cases)
        # @Incomlpete, runner function is not completed, but i have to write a function that can run a lightweight anomaly detector model i have from a publication, it should be done maximumly in 4 minutes and output the results very clear and compact
        run()
    
    def run(self):
        """ This function will run the main diagnoses to detect potential anomalies happened by custom or third party models"""
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



