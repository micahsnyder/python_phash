#!/usr/bin/env python3
'''
Use imagehash lib to get phash
For comparison w/ the rust lib
'''

import logging
from pathlib import Path
import sys
from PIL import Image

import click
import coloredlogs
import imagehash

logging.basicConfig()
module_logger = logging.getLogger("PIL.PngImagePlugin")
module_logger.setLevel(logging.INFO)

from colorama import Fore, Back, Style

#
# CLI Interface
#
@click.group(
    epilog=Fore.BLUE
    + __doc__ + "\n"
    + Style.RESET_ALL
)
def cli():
    pass

@cli.command("calc")
@click.argument("target", required=True)
def calc(target: str):
    """
    calculate phash using imagehash lib
    """

    the_image = Image.open(target)
    hash = imagehash.phash_simple(the_image)
    print(f"{hash}")

@cli.command("compare")
@click.argument("target_1", required=True)
@click.argument("target_2", required=True)
def compare(target_1: str, target_2: str):
    """
    calculate hamming distance of two image phash hashes
    """

    image_1 = Image.open(target_1)
    hash_1 = imagehash.phash_simple(image_1)
    print(f"phash 1: {hash_1}")

    image_2 = Image.open(target_2)
    hash_2 = imagehash.phash_simple(image_2)
    print(f"phash 2: {hash_2}")

    print(f"hamming difference: {hash_2 - hash_1}")

if __name__ == "__main__":
    sys.argv[0] = "pyphash"
    cli(sys.argv[1:])
