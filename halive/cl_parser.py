# -*- encoding: utf-8 -*-
# halive v0.1.0
# An http/s prober, to check which URLs are alive.
# Copyright © 2019, gnc.
# See /LICENSE for licensing information.

"""
Command Line Parsing Module for halive

:Copyright: © 2019, gnc.
:License: BSD (see /LICENSE).
"""

__all__ = ()

import argparse




def parse_args(args):
    """
    This function parses the arguments which have been passed from the command
    line, these can be easily retrieved for example by using "sys.argv[1:]".
    It returns a parser object as with argparse.

    Arguments:
    args -- the list of arguments passed from the command line as the sys.argv
            format

    Returns: a parser with the provided arguments, which can be used in a
            simpler format
    """
    parser = argparse.ArgumentParser(prog='halive',
            description='An http/s prober, to check which URLs are alive.')

    parser.add_argument(
        "inputfiles",
        help="input file with one url per line",
        type=argparse.FileType('r'),
        nargs='+',
        )
    parser.add_argument(
        "-o","--output",
        help="output file name for the report",
        type=argparse.FileType('w'),
        nargs='?',
        )
    parser.add_argument(
        "-t","--concurrency",
        help="number of concurrent http requests",
        default=20,
        type=int,
        )
    parser.add_argument(
        "-s","--onlysuccess",
        help="show only responses which are not 4XX errors",
        action='store_true',
        default=False,
        )
    parser.add_argument(
        "-r","--redirect",
        help="enables redirect following",
        action='store_true',
        default=False,
        )


    return parser.parse_args(args)
