#!/usr/bin/python3

""" Run test for test pdbs """

from subprocess import call
import os, re

pdbs = [
        '1HPX'
        ]

for pdb in pdbs:
  print('')
  print('RUNNING '+pdb)

  # Run pka calculation
  call(['../propka.py','pdb/'+pdb+'.pdb'], stdout = open(pdb+'.out', 'w+'))

  # Test pka predictiona
  result = open('results/'+pdb+'.dat','r')
  atpka = False
  for line in open(pdb+'.pka', 'r').readlines():
    if not atpka:
      if "model-pKa" in line:
        # test pka
        atpka = True
        continue
      else:
        continue
    if "-" in line:
      # done testing
      atpka = False
      continue

    r = float(result.readline())
    m = re.search('([0-9]+\.[0-9]+)', line)

    if(float(m.group(0)) != r):
      print(" ERR:")
      print(line)
      print(" "+"should be: "+str(r))






