
# COMBO CFG SYS 1

# The number of MPI processes
# Note that 2 processes are reserved for Swift/EMEMS
# The default of 4 gives you 2 workers, i.e., 2 concurrent Keras runs
export PROCS=${PROCS:-402}

# MPI processes per node
# Cori has 32 cores per node, 128GB per node
export PPN=${PPN:-1}

#export QUEUE=${QUEUE:-regular}
export WALLTIME=${WALLTIME:-10:00:00}
#export PROJECT=Candle_ECP

# Benchmark run timeout: benchmark run will timeouT
# after the specified number of seconds. -1 is no timeout.
BENCHMARK_TIMEOUT=${BENCHMARK_TIMEOUT:-3600}

