import sys

from pandas import DataFrame
from sklearn.pipeline import Pipeline

from us_visa.exception import USvisaException
from us_visa.logger import logging

class TargetValueMapping:
    def __init__(self):
        self.certified:int = 0
        self.denied :int = 1
    def __asdict(self):
        return self.__dict__
    def reverse_mapping (self):
        mapping_respond = self.__asdict()
        return dict(zip(mapping_respond.values(), mapping_respond.keys()))