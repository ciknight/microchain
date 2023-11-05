# -*- coding: utf-8 -*-
import time
from typing import Optional

from chain import Hash

__all__ = ["Block"]


class Block:
    def __init__(
        self,
        index: int,
        prev_hash: str,
        data: str,
        *,
        nonce: int,
        target: str,
        timestamp: Optional[int] = None,
        hash: Optional[str] = None,
    ) -> None:
        self.index = index
        self.prev_hash = prev_hash
        self.data = data
        self.nonce = nonce
        self.target = target
        self.timestamp = timestamp or time.time()
        self.hash = hash or self._calculate_hash()

    def __eq__(self, other) -> bool:
        if not isinstance(other, Block):
            return False

        if self.index != other.index:
            return False

        if self.hash != other.hash:
            return False

        return True

    def __repr__(self) -> str:
        return f"Block({repr(self.hash)})"

    def _calculate_hash(self) -> str:
        s: bytes = f"{self.index}{self.prev_hash}{self.data}{self.nonce}{self.target}{self.timestamp}".encode(
            "utf-8"
        )
        return Hash(s).hexdigest()

    @property
    def valid(self) -> bool:
        return self._is_valid_difficulty() and self._is_valid_hash()

    def _is_valid_hash(self) -> bool:
        return self.hash == self._calculate_hash()

    def _is_valid_difficulty(self) -> bool:
        return Block.valid_difficulty(self.hash, self.target)

    @staticmethod
    def valid_difficulty(hash: str, target: str) -> bool:
        return int(hash, 16) <= int(target, 16)

    @staticmethod
    def deserialize(other: dict) -> "Block":
        return Block(**other)

    def serialize(self) -> dict:
        return {
            "index": self.index,
            "prev_hash": self.prev_hash,
            "data": self.data,
            "nonce": self.nonce,
            "target": self.target,
            "timestamp": self.timestamp,
            "hash": self.hash,
        }
