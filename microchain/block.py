# -*- coding: utf-8 -*-
import time
from microchain import Hash

__all__ = ['Block']


class Block():

    def __init__(
            self, index: int, nonce: int, previous_hash: str, hash: str = None,
            data: str = None, timestamp: int = None) -> None:
        self.index = index
        self.nonce = nonce
        self.previous_hash = previous_hash
        self.data = data or ''
        self.timestamp = timestamp or time.time()
        self.hash = hash or self._calculate_hash()

    def __eq__(self, other) -> bool:
        if (self.index == other.index
                and self.previous_hash == other.previous_hash
                and self.hash == other.hash):

            return True
        return False

    def __repr__(self) -> str:
        return 'Block({})'.format(self.hash)

    def _calculate_hash(self) -> str:
        original_str: bytes = '{0}{1}{2}{3}{4}'.format(
            self.index,
            self.previous_hash,
            self.timestamp,
            self.data,
            self.nonce).encode('utf-8')

        return Hash(original_str).hexdigest()

    @staticmethod
    def genesis():
        args = (0, 0, '0')
        kwargs = {'data': 'Genesis Block'}
        return Block(*args, **kwargs)

    def serialize(self) -> dict:
        return {
            'index': self.index,
            'previous_hash': self.previous_hash,
            'timestamp': self.timestamp,
            'data': self.data,
            'nonce': self.nonce,
            'hash': self.hash
        }
