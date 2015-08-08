#!/usr/bin/python

"""makeshit.py
Flask templater. Everything you need to get started on a basic
Flask app. 
"""

import urllib
import argparse
import zipfile
import cStringIO
import os
import subprocess
import shutil

__version__ = "0.1"

parser = argparse.ArgumentParser(
    description='Do a Flasky thing.',
    epilog='K.M.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

DEFAULT_PATH = os.path.join('/Users/rhythm/Documents/Programming/', "untitled")

parser.add_argument('project_folder',
                    type=str,
                    help='What to name project folder.')

parser.add_argument('--path',
                    default=DEFAULT_PATH,
                    help='where to create your project directory.')
args = parser.parse_args()


unzip_location = args.path

remotezip = open('/Users/rhythm/Documents/Programming/fl-t/kit.zip')

zipfile_in_mem = cStringIO.StringIO(remotezip.read())
z = zipfile.ZipFile(zipfile_in_mem)
z.extractall(unzip_location)

os.rename("/Users/rhythm/Documents/Programming/untitled", "/Users/rhythm/Documents/Programming/" + args.project_folder + "")

print "Flask template uploaded into folder called %s" %(args.project_folder)
