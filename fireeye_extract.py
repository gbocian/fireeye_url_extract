#!/usr/bin/env python3
from sys import exit
from urllib.parse import parse_qs, urlsplit
import argparse


def main():
    arg_parser = argparse.ArgumentParser(
        description="Extract url from fireeye protect url"
    )

    arg_parser.add_argument(
        "--fe",
        default="https://some_domain.com/param/?a=a&u=[!] sample_here",
        help="Url encoded by fireeye"
    )

    args = arg_parser.parse_args()

    print(parse_qs(urlsplit(args.fe).query).get("u", ["[!] unable to find param (e.g. &u=...)"])[0])
    exit(1)


if __name__ == "__main__":
    main()
