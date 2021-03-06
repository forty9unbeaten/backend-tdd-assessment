#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = 'Rob Spears (GitHub: Forty9Unbeaten)'


import sys
import argparse


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(
        description='Perform transformation on input text.')
    parser.add_argument('text', help='text to be manipulated')
    parser.add_argument(
        '-u', '--upper', help='convert text to uppercase', action='store_true')
    parser.add_argument(
        '-l', '--lower', help='convert text to lowercase', action='store_true')
    parser.add_argument(
        '-t', '--title', help='convert text to titlecase', action='store_true')
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    return parser


def main():
    """Implementation of echo"""
    nspace = create_parser().parse_args()

    upper = nspace.upper
    lower = nspace.lower
    title = nspace.title
    text = nspace.text

    if upper and not lower and not title:
        print(text.upper())
    elif lower and not upper and not title:
        print(text.lower())
    elif title and not upper and not lower:
        print(text.title())
    elif not upper and not lower and not title:
        print(text)
    else:
        print('Only one optional argument can be supplied.')


if __name__ == '__main__':
    main()
