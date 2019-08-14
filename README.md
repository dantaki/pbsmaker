## Make PBS submission scripts with ease
---------------------------------------

### Install

```
pip install https://github.com/dantaki/pbsmaker/releases/download/0.0.4/pbsmaker-0.0.4.tar.gz
```

-------------------------------------

```
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
Version 0.0.3
About:  construct PBS submission scripts with ease
Usage:  pbsmaker [-h] <-i command file> [options]

Author: Danny Antaki dantaki at ucsd dot edu
	
Required Arguments:
  -i        FILE        file containing commands, one per line

Options:
  -q        STR         queue                              [default: hotel]
  -c        INT         cores                              [default: 1]
  -t        STR         walltime                           [H:M:S default: 08:00:00]
  -n        STR         job name                           [default: foo]
  -o        PATH        stdout and stderr log directory    [default: cwd]
  -x        INT         nodes                              [default: 1]
  -r        STR         requested memory in bytes
  -A        STR         account
  -m        STR         email options
  -M        STR         email address
  -d        STR         dependency jobid
  -D        STR         dependency directive               [default: afterany]
  -T        STR         job array argument                 [LINE-START-LINE-END]
  -B        INT         parallel jobs
  -rc       FILE        bashrc file to source
  -E        STR         conda environment to load
  -j                    join output and error log files
  -h        show this message and exit
	 
```
