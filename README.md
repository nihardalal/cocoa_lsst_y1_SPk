## Running Cosmolike projects <a name="running_cosmolike_projects"></a> 

In this tutorial, we assume the user installed Cocoa via the *Conda installation* method, and the name of the Conda environment is `cocoa`. We also presume the user's terminal is in the folder where Cocoa was cloned.

 **Step :one:**: activate the cocoa Conda environment, go to the `projects` folder and clone the Cosmolike LSST-Y1 project:
    
      conda activate cocoa
      cd ./cocoa/Cocoa/projects
      git clone --depth 1 https://github.com/CosmoLike/cocoa_lsst_y1.git lsst_y1 

By convention, the Cosmolike Organization hosts a Cobaya-Cosmolike project named XXX at `CosmoLike/cocoa_XXX`. However, our scripts and YAML files assume the removal of the `cocoa_` prefix when cloning the repository.

📚📚 *Additional Information for experts and developers* 📚📚: Cocoa developers should drop the shallow clone option `--depth 1`, which prevents git from downloading the entire repository history. Developers should also authenticate to GitHub via SSH keys:

      $CONDA_PREFIX/bin/git clone git@github.com:CosmoLike/cocoa_lsst_y1.git lsst_y1
      
 **Step :three:**: go back to the Cocoa main folder, and activate the private Python environment
    
      cd ../
      source start_cocoa
 
:warning::warning: Remember to run the start_cocoa script only **after cloning** the project repository. 

The script *start_cocoa* creates symbolic links so cobaya can see the likelihood and data files. It also adds the *Cobaya-Cosmolike interface* of all projects to `LD_LIBRARY_PATH` and `PYTHONPATH` paths.

**Step :four:**: compile the project
 
      source ./projects/lsst_y1/scripts/compile_lsst_y1

**Step :five:**: select the number of OpenMP cores (below, we set it to 4), and run a template YAML file
    
      export OMP_PROC_BIND=close; export OMP_NUM_THREADS=4
      mpirun -n 1 --oversubscribe --mca btl vader,tcp,self --bind-to core:overload-allowed --rank-by core --map-by numa:pe=${OMP_NUM_THREADS} cobaya-run ./projects/lsst_y1/EXAMPLE_EVALUATE1.yaml -f
 
MCMC:

        $(cocoapy38)(.local) mpirun -n 4 --oversubscribe --mca btl vader,tcp,self --bind-to core:overload-allowed --rank-by core --map-by numa:pe=${OMP_NUM_THREADS} cobaya-run ./projects/lsst_y1/EXAMPLE_MCMC1.yaml -f

## Deleting Cosmolike projects <a name="running_cosmolike_projects"></a>

:warning::warning: Never delete the `lsst_y1` folder from the project folder without running `stop_cocoa` first; otherwise, Cocoa will have ill-defined soft links at `Cocoa/cobaya/cobaya/likelihoods/`, `Cocoa/external_modules/code/` and `Cocoa/external_modules/data/`

## MCMC Convergence Criteria <a name="running_cosmolike_projects"></a>

  We are strict in our convergence criteria on `EXAMPLE_MCMC[0-9].YAML` MCMC examples.
  
    Rminus1_stop: 0.005
    # Gelman-Rubin R-1 on std deviations
    Rminus1_cl_stop: 0.15
    
For most applications, these settings are overkill, except when computing some tension and goodness of fit metrics. Please adjust these settings to your needs. 
