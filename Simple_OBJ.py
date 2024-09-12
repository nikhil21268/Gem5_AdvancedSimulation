# import the m5 (gem5) library created when gem5 is built
import m5
# import all of the SimObjects
from m5.objects import *  # Import all objects

import sys
sys.path.append('/home/nikhil-suri/gem5/configs/common')

from Caches import *

# create the system we are going to simulate
system = System()

# Set the clock fequency of the system (and all of its children)
system.clk_domain = SrcClockDomain()
system.clk_domain.clock = '1GHz'
system.clk_domain.voltage_domain = VoltageDomain()

# Set up the system
system.mem_mode = 'timing'               # Use timing accesses
system.mem_ranges = [AddrRange('8192MB')] # Create an address range

# Create a simple CPU
system.cpu = RiscvO3CPU()



# Cache setup
system.cpu.icache = L1_ICache(size='16kB')
system.cpu.icache.response_latency = 2
system.cpu.icache.cpu_side = system.cpu.icache_port

system.cpu.dcache = L1_DCache(size='16kB')
system.cpu.dcache.response_latency = 2
system.cpu.dcache.cpu_side = system.cpu.dcache_port

system.l2bus = L2XBar()
system.cpu.icache.mem_side = system.l2bus.cpu_side_ports
system.cpu.dcache.mem_side = system.l2bus.cpu_side_ports

system.l2cache = L2Cache(size='64kB', assoc=8)
system.l2cache.response_latency = 10
system.l2cache.cpu_side = system.l2bus.mem_side_ports

system.l3bus = L2XBar()

system.l2cache.mem_side = system.l3bus.cpu_side_ports

# Create the simple memory object
system.memobj = SimpleOBJ()

system.membus = SystemXBar()
    
# Connect the memobj
system.memobj.mem_side = system.membus.cpu_side_ports

system.memobj.cpu_side = system.l3bus.mem_side_ports



# create the interrupt controller for the CPU and connect to the membus
system.cpu.createInterruptController()
# system.cpu.interrupts[0].pio = system.membus.mem_side_ports
# system.cpu.interrupts[0].int_master = system.membus.cpu_side_ports
# system.cpu.interrupts[0].int_slave = system.membus.mem_side_ports

# Create a DDR3 memory controller and connect it to the membus
system.mem_ctrl = MemCtrl()
system.mem_ctrl.dram = DDR3_1600_8x8()
system.mem_ctrl.dram.range = system.mem_ranges[0]
system.mem_ctrl.port = system.membus.mem_side_ports

# Connect the system up to the membus
system.system_port = system.membus.cpu_side_ports

"""
# Create a process for a simple "Hello World" application
process = Process()
# Set the command
# grab the specific path to the binary
thispath = os.path.dirname(os.path.realpath(__file__))
binpath = os.path.join(thispath, '../../../', 'tests/test-progs/hello/bin/x86/linux/hello')
# cmd is a list which begins with the executable (like argv)
process.cmd = [binpath]
# Set the cpu to use the process as its workload and create thread contexts
system.cpu.workload = process
system.cpu.createThreads()

system.workload = SEWorkload.init_compatible(binpath)
"""

binary = '/home/nikhil-suri/mibench/automotive/qsort/qsort_small.elf'

system.workload = SEWorkload.init_compatible(binary)

process = Process()
process.cmd = ['/home/nikhil-suri/mibench/automotive/qsort/qsort_small.elf', '/home/nikhil-suri/mibench/automotive/qsort/input_small.dat']
system.cpu.workload = process
system.cpu.createThreads()

# set up the root SimObject and start the simulation
root = Root(full_system = False, system = system)
# instantiate all of the objects we've created above
m5.instantiate()

print("Beginning simulation!")
exit_event = m5.simulate()
print('Exiting @ tick %i because %s' % (m5.curTick(), exit_event.getCause()))
