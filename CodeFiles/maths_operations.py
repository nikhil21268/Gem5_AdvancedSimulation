import m5
from m5.objects import *

def setup_events():

    root = Root(full_system = False)

    root.MathsOperationsObject = MathsOperations()

    m5.instantiate()

    print("Beginning simulation!")
    exit_event = m5.simulate()
    print('Exiting @ tick {} because {}'
        .format(m5.curTick(), exit_event.getCause()))

setup_events()
