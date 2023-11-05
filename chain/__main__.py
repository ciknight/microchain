# -*- coding: utf-8 -*-
import argparse
import asyncio

from chain.p2p import P2PServer


parser = argparse.ArgumentParser()

parser.add_argument("-p", "--port", type=int, help="Listening port")

parser.add_argument(
    "-b",
    "--bootnodes",
    type=str,
    help="Starting by bootstrapping node, can specify multiple IPs, split by comma",
)

parser.add_argument("-m", "--mine", action="store_true", help="Mining blocks")

if __name__ == "__main__":
    args = parser.parse_args()
    server = P2PServer(mining=args.mining)
    loop = asyncio.get_event_loop()
