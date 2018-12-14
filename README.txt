Make PBS submission scripts with ease

usage: 

8888888b. 888888b.   .d8888b. 888b     d888       d8888888    d8P 88888888888888888b.  
888   Y88b888  "88b d88P  Y88b8888b   d8888      d88888888   d8P  888       888   Y88b 
888    888888  .88P Y88b.     88888b.d88888     d88P888888  d8P   888       888    888 
888   d88P8888888K.  "Y888b.  888Y88888P888    d88P 888888d88K    8888888   888   d88P 
8888888P" 888  "Y88b    "Y88b.888 Y888P 888   d88P  8888888888b   888       8888888P"  
888       888    888      "888888  Y8P  888  d88P   888888  Y88b  888       888 T88b   
888       888   d88PY88b  d88P888   "   888 d8888888888888   Y88b 888       888  T88b  
888       8888888P"  "Y8888P" 888       888d88P     888888    Y88b8888888888888   T88b
                        construct PBS job submission scripts 
--------------------------------------------------------------------------------------
Version 0.0.1
Author: Danny Antaki dantaki at ucsd dot edu
  pbsmaker  -i <command> -a <account> -p <partition> 
           -c <cpu>     -t <walltime> -n <jobname> 
           -o <logdir>  -T <array arg> -B <n_parallel>
	
pbs arguments:
  
  -i        file containing commands
  -q        queue     [default: hotel]
  -c        cores     [default: 1]
  -t        walltime  [H:M:S default: 08:00:00]
  -x        nodes     [default: 1]
  -d        dependency jobid
  -D        dependency directive [default: afterany]

  -n        job name  [default: foo]
  -o        stdout and stderr output directory [default: cwd]

job array arguments:

  -T        array argument [LINE_START-LINE_END]
  -B        parallel jobs

optional arguments:
  -rc       bashrc file to source
  -h        show this message and exit
