# -*- coding: utf-8 -*-
import logging
from typing import List, Optional

from microchain.block import Block

__all__ = ["Chain"]


class Chain:
    _interval = 10  # second

    def __init__(self, blocks: Optional[List[Block]] = None) -> None:
        self.blocks = blocks or [Chain.genesis()]

    def __len__(self):
        return self.length

    def __repr__(self):
        return f"Chain({repr(self.blocks)})"

    @property
    def interval(self):
        return self._interval

    @property
    def length(self) -> int:
        return len(self.blocks)

    @property
    def latest_block(self) -> Block:
        return self.blocks[-1]

    def add_block(self, block: Block) -> bool:
        if block.valid is True:
            self.blocks.append(block)
            return True

        return False

    @staticmethod
    def genesis() -> Block:
        args = (0, "0", "Genesis Block")
        nonce = 0
        # (difficulty 1): 0x00ffff * 2**(8*(0x1d - 3))
        target = "0x00000000FFFF0000000000000000000000000000000000000000000000000000"
        while True:
            block = Block(*args, nonce=nonce, target=target)
            if block.valid is True:
                break
            else:
                nonce += 1

        return block

    @property
    def difficulty(self) -> float:
        """Difficulty is Calculate the hash of times.
        Url: https://en.bitcoin.it/wiki/Difficulty#How_often_does_the_network_difficulty_change.3F
        """
        difficulty_1_target = (
            "0x00000000FFFF0000000000000000000000000000000000000000000000000000"
        )
        return float(int(difficulty_1_target, 16) / int(self.latest_block.target, 16))

    @property
    def current_target(self) -> str:
        """ReTarget"""
        lb = self.latest_block
        # Every 10 blocks change network difficulty, bitcoin is 2016 blocks.
        block_count = 10
        target_timespan = block_count * self.interval
        if self.length % block_count != 0:
            return lb.target
        else:
            ratio_limit = 4
            actual_timespan = lb.timestamp - self.blocks[-block_count].timestamp
            adjusted_timespan = min(
                max(actual_timespan, target_timespan / ratio_limit),
                target_timespan * ratio_limit,
            )
            assert 1 / ratio_limit <= adjusted_timespan / target_timespan <= ratio_limit
            logging.info(
                f"ReTargeting at {self.length}, difficulty change: {target_timespan/adjusted_timespan:.2%}"
            )
            new_target = int(lb.target, 16) * adjusted_timespan / target_timespan
            return f"{int(new_target):x}".rjust(64, "0")

    def generate_next(self, data: str) -> Block:
        lb = self.latest_block
        args = (lb.index + 1, lb.hash, data)
        nonce = 0
        while True:
            new_block = Block(*args, nonce=nonce, target=self.current_target)
            if new_block.valid is True:
                break
            else:
                nonce += 1

        return new_block

    def mine(self, data: str) -> bool:
        next_block = self.generate_next(data)
        return self.add_block(next_block)
