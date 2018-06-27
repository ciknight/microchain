# -*- coding: utf-8 -*-
from typing import List
from microchain.block import Block


class Chain():

    def __init__(self, blocks: List[Block] = None) -> None:
        self.blocks = blocks or [Block.genesis()]
        self._difficulty = 5

    def __len__(self):
        return self.length

    @property
    def length(self) -> int:
        return len(self.blocks)

    @property
    def latest_block(self) -> Block:
        return self.blocks[-1]

    def _is_hash_valid(self, hash: str) -> bool:
        return hash[:self._difficulty] == '0' * self._difficulty

    def mine(self, data: str = 'null') -> None:
        previous_block = self.latest_block
        nonce = 0
        while True:
            nonce += 1
            args = (previous_block.index + 1, nonce, previous_block.hash)
            kwargs = {'data': data}
            new_block = Block(*args, **kwargs)
            if self._is_hash_valid(new_block.hash):
                self.blocks.append(new_block)
                break
