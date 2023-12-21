"""
Composy - Compos API python wrapper
Compos file definition - Restraint Point
"""
__all__ = ['FinalRestraintNostud']

from enum import StrEnum

# Final restraint no stud section
class DefRest(StrEnum):
    NOSTUD_ZONE_LATERAL_FIXED = 'NOSTUD_ZONE_LATERAL_FIXED'
    NOSTUD_ZONE_LATERAL_FREE = 'NOSTUD_ZONE_LATERAL_FREE'


class FinalRestraintNostud():
    def __init__(self,
                 member_name,
                 rest: DefRest,
                 ):
        self.member_name = member_name
        self.rest = rest


    def __repr__(self) -> str:
        return f"FINAL_RESTRAINT_NOSTUD({self.rest},{self.num})"

    def __str__(self) -> str:
        return f"FINAL_RESTRAINT_NOSTUD,{self.member_name},{self.rest},{self.num}"