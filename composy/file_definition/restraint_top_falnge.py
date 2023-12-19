"""
Composy - Compos API python wrapper
Compos file definition - Restraint Point
"""
__all__ = ['RestraintTopFlange']

from enum import StrEnum

# Top Flange Restraint type enumerations
class DefRest(StrEnum):
    TOP_FLANGE_FREE = 'TOP_FLANGE_FREE'
    TOP_FLANGE_FIXED = 'TOP_FLANGE_FIXED'


class RestraintTopFlange():
    def __init__(self,
                 member_name,
                 rest: DefRest,
                 ):
        self.member_name = member_name
        self.rest = rest


    def __repr__(self) -> str:
        return f"RESTRAINT_TOP_FALNGE({self.rest})"

    def __str__(self) -> str:
        return f"RESTRAINT_TOP_FALNGE,{self.member_name},{self.rest}"