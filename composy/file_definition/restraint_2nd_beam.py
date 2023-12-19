"""
Composy - Compos API python wrapper
Compos file definition - Restraint Point
"""
__all__ = ['Restraint2ndBeam']

from enum import StrEnum

# Secondary beam restraint type enumerations
class DefRest(StrEnum):
    SEC_BEAM_AS_REST = 'SEC_BEAM_AS_REST'
    SEC_BEAM_NOT_AS_REST = 'SEC_BEAM_NOT_AS_REST'


class Restraint2ndFlange():
    def __init__(self,
                 member_name,
                 rest: DefRest,
                 ):
        self.member_name = member_name
        self.rest = rest


    def __repr__(self) -> str:
        return f"RESTRAINT_2ND BEAM({self.rest})"

    def __str__(self) -> str:
        return f"RESTRAINT_2ND BEAM,{self.member_name},{self.rest}"