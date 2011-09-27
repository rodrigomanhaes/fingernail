#!/usr/bin/env python
import os
import glob
from run_examples import run

def all_examples():
    doctests_path = os.path.join('doctests')
    doctests = list(map(lambda f: os.path.join(doctests_path, f),
        filter(lambda f: f.endswith('.txt'), os.listdir(doctests_path))))
    return doctests

if __name__ == '__main__':
    run(all_examples())

