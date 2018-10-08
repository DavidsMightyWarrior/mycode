#!/usr/bin/env python3
## Import functions to use for os and copy related features
import shutil, os

## Change to mycode directory
os.chdir('/Users/waldrer/Desktop/PythonLab/mycode/')
## Copy sdn_network.txt file to .copy
shutil.copy('5g_research/sdn_network.txt', '5g_research/sdn_network.txt.copy')

## Create backup direcory of 5g_research directory
shutil.copytree('5g_research/', '5g_research_backup')
