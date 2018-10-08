# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import argparse
import os
from subprocess import check_call
import twine

DEFAULT_DEST_FOLDER = "../dist"

def test_package(package):
    print("Running unittests for {}...".format(package))
    absdirpath = os.path.abspath(package)
    check_call(['pytest'], cwd=absdirpath) #discovery will find the tests
    print("Unittests passed!")

def build_wheel(package, dest_folder=DEFAULT_DEST_FOLDER):
    print("Building wheel for {}...".format(package))
    absdirpath = os.path.abspath(package)
    check_call(['python', 'setup.py', 'bdist_wheel', '-d', dest_folder], cwd=absdirpath)
    check_call(['python', 'setup.py', 'clean', '--all'], cwd=absdirpath)
    print("Wheel created in {}!".format(os.path.abspath(dest_folder)))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a wheel for a package.')
    parser.add_argument('package', help='The package name.')
    parser.add_argument('--dest', '-d', default=DEFAULT_DEST_FOLDER,
                        help='Destination folder. Relative to the package dir. [default: %(default)s]')
    args = parser.parse_args()
    test_package(args.package)
    build_wheel(args.package, args.dest)
