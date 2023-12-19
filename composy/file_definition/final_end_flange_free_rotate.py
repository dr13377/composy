"""
Composy - Compos API python wrapper
Compos file definition - Restraint Point
"""
__all__ = ['FinalEndFLangeFreeRotate']

from enum import StrEnum

# Design code and Construction type enumerations
class DefValue(StrEnum):
    FREE_TO_ROTATE = 'FREE_TO_ROTATE'
    NOT_FREE_TO_ROTATE = 'NOT_FREE_TO_ROTATE'


class FinalEndFLangeFreeRotate():
    def __init__(self,
                 member_name,
                 value: DefValue,
                 ):
        self.member_name = member_name
        self.value = value


    def __repr__(self) -> str:
        return f"FINAL_END_FLANGE_FREE_ROTATE({self.value})"

    def __str__(self) -> str:
        return f"FINAL_END_FLANGE_FREE_ROTATE,{self.member_name},{self.value}"