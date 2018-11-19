# -*- coding: utf-8 -*-
from typing import List

from microchain.block import Block

__all__ = ['Chain']


class Chain():

    def __init__(self, blocks: List[Block] = None) -> None:
        self.blocks = blocks or [Chain.genesis()]

    def __len__(self):
        return self.length

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
        args = (0, '0', 'Genesis Block')
        nonce = 0
        target = '0x0000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'
        while True:
            block = Block(*args, nonce=nonce, target=target)
            if block.valid is True:
                break
            else:
                nonce += 1

        return block

    def retarget(self) -> str:
        return '0x00000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'

    def generate_next(self, data: str) -> Block:
        prev_block = self.latest_block
        args = (prev_block.index + 1, prev_block.hash, data)
        nonce = 0
        target = self.retarget()
        while True:
            new_block = Block(*args, nonce=nonce, target=target)
            if new_block.valid is True:
                break
            else:
                nonce += 1

        return new_block

    def mine(self, data: str = 'null') -> bool:
        next_block = self.generate_next(data)
        return self.add_block(next_block)
