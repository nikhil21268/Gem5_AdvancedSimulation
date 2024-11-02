from m5.params import *
from m5.SimObject import SimObject

class MathsOperations(SimObject):
    type = 'MathsOperations'
    cxx_header = "sim/maths_operations.hh"
    cxx_class = "gem5::MathsOperations"
