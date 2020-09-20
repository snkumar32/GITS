import os
import sys
import argparse
from gits_hello import gits_hello_world
from gits_profile import gits_set_profile

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

gits_hello_subparser = subparsers.add_parser('hello_world')
gits_hello_subparser.set_defaults(func=gits_hello_world)

gits_profile_subparser = subparsers.add_parser('profile', help='profie help')
gits_profile_subparser.set_defaults(func=gits_set_profile)
gits_profile_subparser.add_argument('--email', required=True)
gits_profile_subparser.add_argument('--name', required=True)
#print(gits_profile_subparser.parse_args(['--email']))

args = parser.parse_args()
args.func(args)
