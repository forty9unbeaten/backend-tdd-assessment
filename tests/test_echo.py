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
        help_display = stdout.decode().strip()
        with open('USAGE', 'r') as f:
            help_output = f.read().strip()
        self.assertEqual(help_display, help_output)

    def test_upper(self):
        """ Test the --upper / -u functionality """
        upper_output = check_output(
            ["python", "echo.py", "heLLo wOrld", "-u"]).decode().strip()
        self.assertEqual(upper_output, 'HELLO WORLD')

    def test_lower(self):
        """ Test the --lower / -u functionality """
        lower_output = check_output(
            ["python", "echo.py", "heLLo wOrld", "-l"]).decode().strip()
        self.assertEqual(lower_output, 'hello world')

    def test_title(self):
        """ Test the --title / -t functionality """
        title_output = check_output(
            ["python", "echo.py", "heLLo wOrld", "-t"]).decode().strip()
        self.assertEqual(title_output, 'Hello World')

    def test_all_args(self):
        """ Test functionality when all optional arguments are supplied """
        all_args_output = check_output(
            ["python", "echo.py", "heLLo wOrld", "-ult"]).decode().strip()
        self.assertEqual(
            all_args_output, 'Only one optional argument can be supplied.')

    def test_no_args(self):
        """ Test help display when no arguments are supplied """
        process = Popen(["python", "echo.py"], stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        no_args_output = stdout.decode().strip()
        with open('USAGE', 'r') as f:
            help_output = f.read().strip()
        self.assertEqual(no_args_output, help_output)


if __name__ == '__main__':
    unittest.main()
