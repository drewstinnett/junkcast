#!/usr/bin/env python3
import sys
import argparse
import yaml
from podgen import Podcast


def parse_args():
    """Parse the arguments."""
    parser = argparse.ArgumentParser(
        description="This is my super sweet script")
    parser.add_argument("-i",
                        "--input",
                        required=True,
                        help="Input file to read config and episodes from",
                        type=argparse.FileType('r'))
    parser.add_argument("-v",
                        "--verbose",
                        help="Be verbose",
                        action="store_true",
                        dest="verbose")

    return parser.parse_args()


def main():
    args = parse_args()
    data = yaml.load(args.input.read(), Loader=yaml.FullLoader)
    p = Podcast()
    p.name = data["name"]
    p.website = data["website"]
    p.image = data["image"]
    p.description = data["description"]
    p.explicit = False

    rssfeed = p.rss_str()
    print(rssfeed)
    return 0


if __name__ == "__main__":
    sys.exit(main())
