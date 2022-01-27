#!/bin/bash

#SBATCH --job-name=w_bary
#SBATCH --output=baryon_lsst.out
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4
#SBATCH --cpus-per-task=8
#SBATCH --partition=standard
#SBATCH --qos=user_qos_timeifler
#SBATCH --account=timeifler
#SBATCH --mem-per-cpu=4GB
#SBATCH --time=12:00:00
#SBATCH --export=none

echo Running on host `hostname`
echo Time is `date`
echo Directory is `pwd`
echo Slurm job NAME is $SLURM_JOB_NAME
echo Slurm job ID is $SLURM_JOBID

cd /home/u7/ssarmabo/cocoa_emulator/cocoa/Cocoa/
source start_cocoa

export OMP_PROC_BIND=close
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
mpirun -n ${SLURM_NTASKS} --mca btl tcp,self --bind-to core --rank-by core --map-by numa:pe=${OMP_NUM_THREADS} cobaya-run ./projects/lsst_y1/template_yamls/mcmc/MCMC_W_BARYONS.yaml -r
