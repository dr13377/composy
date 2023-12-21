"""
Composy - Compos API python wrapper
Compos file definition - Restraint Point
"""
__all__ = ['FinalRestraintPoint']

from enum import StrEnum

# Final restraint points
class DefRestraintType(StrEnum):
    STANDARD = 'STANDARD'
    USER_DEFINED = 'USER_DEFINED'


class FinalRestraintPoint():
    def __init__(self,
                 member_name,
                 restraint_type: DefRestraintType,
                 num: int,
                 index: int,
                 x: float,
                 ):
        self.member_name = member_name
        self.restraint_type = restraint_type
        self.num = num
        self.index = index
        self.x = x

    def __repr__(self) -> str:
        return f"FINAL_RESTRAINT_POINT({self.restraint_type},{self.num},{self.index},{self.x})"

    def __str__(self) -> str:
        return f"FINAL_RESTRAINT_POINT,{self.member_name},{self.restraint_type},{self.num},{self.index},{self.x}"