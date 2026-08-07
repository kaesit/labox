from typing import Dict, Any, Callable, Optional
from quality_control.core.base import BaseQualityModel, QualityTask, Status


class QualityTestPipeline():
    
    def __init__(self, quality_test:BaseQualityModel) -> None:
        self.quality_test = quality_test
        run(quality_test)

    def run (self, quality_test: BaseQualityModel, *args, **kwargs):
        

    def cancel(self) -> None:
        BaseQualityModel.cancel()

