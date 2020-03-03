#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
from subprocess import Popen, PIPE

# Your test case class goes here


class TestEcho(unittest.TestCase):
    def test_help(self):
        """ Test the uppercase functionality """
        process = Popen(['python', 'echo.py', '-h'], stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        stdout = stdout.decode()
        with open('USAGE', 'r') as f:
            help_output = f.read()
        self.assertEqual(stdout, help_output)


if __name__ == '__main__':
    unittest.main()
