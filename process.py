#!/usr/bin/env python3
import json
from os import listdir, getcwd
from os.path import join

def process(directory):
    onlyfiles = [f for f in listdir(directory)]
    return onlyfiles

if __name__ == '__main__':
    directory = join(getcwd(), "files")
    print(process(directory))
