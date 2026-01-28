# Core classes 
#
# AUTHOR Sven Schrodt
# SINCE 2026-01-21
from dataclasses import dataclass
from typing import Dict


class Updatable(object):
    '''
    Updateable base class - to be used esp. with dataclass instances by inheritance
    - only setting existing dataclass attributes
    '''
    def update(self, new: Dict):
        for key, value in new.items():
            if hasattr(self, key):
                setattr(self, key, value)