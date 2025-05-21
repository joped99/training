#!/bin/bash

#SBATCH --time=0:05:00   # walltime
#SBATCH --ntasks=1   # number of processor cores (i.e. tasks)
#SBATCH --nodes=1   # number of nodes
#SBATCH --mem-per-cpu=1024M   # memory per CPU core


# Set the max number of threads to use for programs using OpenMP. Should be <= ppn. Does nothing if the program doesn't use OpenMP.
export OMP_NUM_THREADS=$SLURM_CPUS_ON_NODE

# LOAD MODULES, INSERT CODE, AND RUN YOUR PROGRAMS HERE

# looping for all stepsizes
for iter in {0..6}; do
    echo "1e-${iter}" > data/params.dat # update parameter
    ./bin/EulerRun # execute program
    mv "data/output.dat" "data/output${iter}.dat" # renaming output
done

