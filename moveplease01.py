#!/usr/bin/env python3
import shutil, os
os.chdir('/Users/waldrer/Desktop/PythonLab/mycode/')
shutil.move('raynor.obj','ceph_storage/')
xname=input('What is the new name for kerrigan.obj? ')
shutil.move('ceph_storage/kerrigan.obj','ceph_storage/' + xname)
