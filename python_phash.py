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
module_logger = logging.getLogger("pyphash")
coloredlogs.install(level="DEBUG", fmt="%(asctime)s %(name)s %(levelname)s %(message)s")
module_logger.setLevel(logging.DEBUG)

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
    hash = imagehash.phash(the_image)
    module_logger.info(f"phash: {hash}")

@cli.command("compare")
@click.argument("target_1", required=True)
@click.argument("target_2", required=True)
def compare(target_1: str, target_2: str):
    """
    calculate hamming distance of two image phash hashes
    """

    image_1 = Image.open(target_1)
    hash_1 = imagehash.phash(image_1)
    module_logger.info(f"phash: {hash_1}")

    image_2 = Image.open(target_2)
    hash_2 = imagehash.phash(image_2)
    module_logger.info(f"phash: {hash_2}")

    module_logger.info(f"hamming difference: {hash_2 - hash_1}")

if __name__ == "__main__":
    sys.argv[0] = "pyphash"
    cli(sys.argv[1:])
