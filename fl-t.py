#!/usr/bin/python

"""fl-t.py
Flask templater. Everything you need to get started on a basic
Flask app. 
"""

import urllib
import argparse
import zipfile
import cStringIO
import os
import subprocess

__version__ = "0.2"

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

remotezip = open('/fl-t/kit.zip')

zipfile_in_mem = cStringIO.StringIO(remotezip.read())
z = zipfile.ZipFile(zipfile_in_mem)
z.extractall(unzip_location)

os.rename("/Documents/Programming/untitled", "/Documents/Programming/" + args.project_folder + "")

print "Flask template uploaded into folder called %s" %(args.project_folder)
