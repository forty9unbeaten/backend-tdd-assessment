#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "Rob Spears (GitHub: Forty9Unbeaten)"


import sys
import argparse


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(
        description='Manipulate text and print to command line')
    parser.add_argument('text', help='The text to be manipulated')
    parser.add_argument(
        '-u', '--upper', help='Convert text to uppercase', action='store_true')
    parser.add_argument(
        '-l', '--lower', help='Convert text to lowercase', action='store_true')
    parser.add_argument(
        '-t', '--title', help='Convert text to titlecase', action='store_true')
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    return parser.parse_args()


def main():
    """Implementation of echo"""
    nspace = create_parser()


if __name__ == '__main__':
    main()
