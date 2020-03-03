#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
from subprocess import Popen, PIPE, check_output

# Your test case class goes here


class TestEcho(unittest.TestCase):
    def test_help(self):
        """ Test the help interface functionality """
        process = Popen(['python', 'echo.py', '-h'], stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        stdout = stdout.decode().strip()
        with open('USAGE', 'r') as f:
            help_output = f.read().strip()
        self.assertEqual(stdout, help_output)

    def test_upper(self):
        """ Test the --upper / -u functionality """
        upper_out = check_output(
            ["python", "echo.py", "heLLo wOrld", "-u"]).decode().strip()
        self.assertEqual(upper_out, 'HELLO WORLD')

    def test_lower(self):
        """ Test the --lower / -u functionality """
        lower_out = check_output(
            ["python", "echo.py", "heLLo wOrld", "-l"]).decode().strip()
        self.assertEqual(lower_out, 'hello world')

    def test_title(self):
        title_out = check_output(
            ["python", "echo.py", "heLLo wOrld", "-t"]).decode().strip()
        self.assertEqual(title_out, 'Hello World')


if __name__ == '__main__':
    unittest.main()
