import sys

from pandas import DataFrame
from sklearn.pipeline import Pipeline

from us_visa.exception import USvisaException
from us_visa.logger import logging

class TargetValueMapping:
    def __init__(self):
        # Mapping 0 → Not Exited, 1 → Exited
        self.mapping = {0: "Not Exited", 1: "Exited"}

    def reverse_mapping(self):
        return self.mapping
