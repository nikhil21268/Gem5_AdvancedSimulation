from m5.params import *
from m5.proxy import *
from m5.SimObject import SimObject

class SimpleOBJ(SimObject):
    type = 'SimpleOBJ'
    cxx_header = "/home/nikhil-suri/gem5/src/learning_gem5/Simple_OBJ.hh"
    
    # inst_port = SlavePort("CPU side port, receives requests")
    # data_port = SlavePort("CPU side port, receives requests")
    cpu_side = SlavePort("CPU side port, receives requests")
    mem_side = MasterPort("Memory side port, sends requests")