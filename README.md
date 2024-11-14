# Gem5 Simulation Project: MathsOperations and SimpleOBJ

## Overview
This repository contains simulation scripts and source files for two tasks related to Gem5 architecture simulations. The first part of the project, `MathsOperations`, handles mathematical operations at specified simulation ticks using custom SimObjects. The second part, `SimpleOBJ`, involves a memory object that interfaces between the CPU and memory systems, managing requests and incorporating debug support for detailed tracing.

## Installation
### Prerequisites
- Gem5 dependencies (see: [Gem5 Documentation](https://www.gem5.org/documentation/general_docs/building))
- SCons (build system)
- Python 3.x
- GCC or any standard C++ compiler

### Building Gem5
Clone the official Gem5 repository and build the RISCV architecture to use with the simulation scripts:

git clone https://gem5.googlesource.com/public/gem5
cd gem5
scons build/RISCV/gem5.opt -j$(nproc)  # Adjust $(nproc) with the number of cores you want to use

## Usage
To run the simulations, use the following commands from the root of the Gem5 directory:

### For MathsOperations

./build/RISCV/gem5.opt --debug-flags=FIBONACCISEQUENCE ./src/sim/maths_operations.py


### For SimpleOBJ

./build/RISCV/gem5.opt --debug-flags=SimpleOBJ src/learning_gem5/Simple_OBJ.py > outputFileName.txt


## Contributing
Contributions to the project are welcome. Please fork the repository and submit pull requests with your proposed changes.
