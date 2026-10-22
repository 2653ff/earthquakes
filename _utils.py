"""This file contains some supporting utility functions for the `earthquakes.py` script.

In general, if you are finding that you need to split up your scripts into multiple files
because they're too long, or they use the same individual "pieces" of code, you would
consider writing a package containing the common functionality.
We will see how to do this later in the course (and in the assignment)!.

Since this repository is fairly small, we'll just use a couple of auxiliary files - like
this one - to store our 'helper' functions.
This is mainly so tha the `earthquakes.py` file only contains code that's actually
relevant to what we want to do in the exercises / homework / pre-reading.

This file contains the functionality to have the earthquake data be saved to the local
machine, and also outlines the structure of the data so Python can give typehints.
"""

import argparse
from pathlib import Path


def read_cli_args() -> argparse.Namespace:
    """Creates the command-line interface for the `earthquakes.py` script,
    and parses the arguments.

    The CLI just adds an option to have the script save the data to a `.json` file
    when it fetches it from the internet.
    """
    parser = argparse.ArgumentParser(
        description="Fetches US geological survey earthquake data from 2000-01-01 to 2018-10-11."
    )
    parser.add_argument("-s", "--save", nargs=1, type=str, default=None)

    args = parser.parse_args()
    if args.save is not None:
        args.save = Path(args.save)

    return args
