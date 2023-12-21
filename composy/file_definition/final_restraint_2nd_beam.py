"""
Composy - Compos API python wrapper
Compos file definition - Restraint Point
"""
__all__ = ['FinalRestraint2ndBeam']

from enum import StrEnum

# Final Secondary beam restraint type enumerations
class DefRest(StrEnum):
    SECONDARY_AS_REST = '2ND_BEAM_AS_REST'
    SECONDARYE_NOT_REST = '2ND_BEAM_NOT_AS_REST'


class FinalRestraint2ndFlange():
    def __init__(self,
                 member_name,
                 rest: DefRest,
                 ):
        self.member_name = member_name
        self.rest = rest


    def __repr__(self) -> str:
        return f"FINAL_RESTRAINT_2ND BEAM({self.rest})"

    def __str__(self) -> str:
        return f"FINAL_RESTRAINT_2ND BEAM,{self.member_name},{self.rest}"