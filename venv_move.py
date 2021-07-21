#!/usr/bin/python3
'''

This script needs to be activated when virtual environment has been moved to another path.
It replaces all shebangs and venv paths references in files that are significant for 
proper venv activation.

'''


import os


workdir = os.getcwd()


filenames = [
    'django-admin',
    'django-admin.py',
    'easy_install',
    'easy_install-3.7',
    'pip',
    'pip3',
    'pip3.7',
    'sqlformat'
]

for name in filenames:
    with open(name) as f:
        lines = f.readlines()
    lines[0] = '#!' + workdir + '/python3' + '\n'
    with open(name, 'w') as f:
        f.writelines(lines)

with open('activate') as f:
    lines = f.readlines()
lines[39] = 'VIRTUAL_ENV=' + '"' + workdir[:-4] + '"' + '\n'
with open('activate', 'w') as f:
        f.writelines(lines)
