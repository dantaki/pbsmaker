#!/usr/bin/env python
'''
Copyright <2018> <Danny Antaki>
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
from argparse import RawTextHelpFormatter
import argparse,os,sys
__version__='0.0.3'
__usage__="""

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
Version {}
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
	 
""".format(__version__)
def header(part,nodes,cpu,wall,jobid,err,out):
    a = [
        '#!/bin/bash',
        '#PBS -q {}'.format(part),
        '#PBS -l nodes={}:ppn={}'.format(nodes,cpu),
        '#PBS -l walltime={}'.format(wall),
        '#PBS -N {}'.format(jobid),
        '#PBS -o {}'.format(out),
        '#PBS -e {}'.format(err),
	]
    return a
def main():
    parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter, usage=__usage__, add_help=False)
    pbs_args = parser.add_argument_group('pbs arguments')
    pbs_args.add_argument('-i',type=str,default=None,required=True)
    pbs_args.add_argument('-q',type=str,default='hotel',required=False)
    pbs_args.add_argument('-c',type=int,default=1,required=False)
    pbs_args.add_argument('-t',type=str,default='08:00:00',required=False)
    pbs_args.add_argument('-x',type=int,default=1,required=False)
    pbs_args.add_argument('-r',type=str,default=None,required=False)
    pbs_args.add_argument('-A',type=str,default=None,required=False)
    pbs_args.add_argument('-m',type=str,default=None,required=False)
    pbs_args.add_argument('-M',type=str,default=None,required=False)
    pbs_args.add_argument('-d',type=str,default=None,required=False)
    pbs_args.add_argument('-D',type=str,default='afterany',choices=['afterany','afterok','afternotok','after','before','beforeok','beorenotok','beforeany'],required=False)
    pbs_args.add_argument('-n',type=str,default='foo',required=False)
    pbs_args.add_argument('-o',type=str,default=os.getcwd(),required=False)
    pbs_args.add_argument('-T',type=str,default=None,required=False)
    pbs_args.add_argument('-B',type=int,default=None,required=False)
    pbs_args.add_argument('-rc',type=str,required=False,default=None)
    pbs_args.add_argument('-E',type=str,required=False,default=None)
    pbs_args.add_argument('-j',default=False,action="store_true",required=False)
    pbs_args.add_argument('-h', '-help', required=False, action="store_true", default=False)
    
    args = parser.parse_args()
    cmd, part, cpu, wall, mem, nodes, depend, direct, jobid, odir = args.i, args.q, args.c, args.t, args.r, args.x, args.d, args.D, args.n, args.o
    acc, mail, addr = args.A, args.m, args.M 
    arr, arrby = args.T, args.B
    rc, conda_env, join, _help = args.rc, args.E, args.j, args.h
    if (_help==True or len(sys.argv)==1):
        print(__usage__)
        sys.exit(0)
    ############################################################################
    if not os.path.isfile(cmd):
        sys.stderr.write('FATAL ERROR: {} NOT A FILE\n'.format(cmd))
        sys.exit(1)
    if cpu < 0:
        sys.stderr.write('FATAL ERROR: {} CAN NOT BE LESS THAN 0\n'.format(cpu))
        sys.exit(1)
    if rc != None and not os.path.isfile(rc):
        sys.stderr.write('FATAL ERROR: {} NOT A FILE\n'.format(rc))
        sys.exit(1)
    if mail!= None and addr == None or mail==None and addr!=None:
        sys.stderr.write('FATAL ERROR: both -m and -M must defined\n')
        sys.exit(1)
    ############################################################################
    if not odir.endswith('/'): odir=odir+'/'
    depends = None
    if depend!=None: depends = "#PBS -W depend={}:{}".format(direct,depend)
    err,out = odir+jobid+'_err', odir+jobid+'_out'
    head = header(part,nodes,cpu,wall,jobid,err,out)
    sys.stdout.write('{}\n'.format('\n'.join(head)))
    if depends!=None: sys.stdout.write('{}\n'.format(depends))
    if arr!=None: sys.stdout.write('#PBS -t {}%{}\n'.format(arr,arrby))
    if acc!=None: sys.stdout.write('#PBS -A {}\n'.format(acc))
    if mail!=None: sys.stdout.write('#PBS -m {}\n#PBS -M {}\n'.format(mail,addr))
    if mem!=None:  sys.stdout.write('#PBS -l mem={}\n'.format(mem))
    if join==True: sys.stdout.write('#PBS -j oe\n')
    ############################################################################
    if rc != None: sys.stdout.write('source {}\n'.format(rc))
    if conda_env != None: sys.stdout.write('conda activate {}\n'.format(conda_env))
    if arr==None:
        _cmd=[]
        with open(cmd,'r') as f: _cmd = [l.rstrip() for l in f]
        sys.stdout.write('{}\n'.format('\n'.join(_cmd)))
    else:
        sys.stdout.write('SEED=$(cat {} | head -n $PBS_ARRAYID | tail -n 1 | awk "{{print $1}}")\n$SEED\n'.format(cmd))
