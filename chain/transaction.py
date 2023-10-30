# -*- coding: utf-8 -*-
from typing import List, Optional


class TxType:
    Regular = "regular"
    Coinbase = "coinbase"

    All = (Regular, Coinbase)


class TxIn:
    pass


class TxOut:
    pass


class Transaction:
    def __init__(
        self,
        type_: str,
        inputs: Optional[List[TxIn]] = None,
        outputs: Optional[List[TxOut]] = None,
    ) -> None:
        self._type = type_
        assert self._type in TxType.All
        self._inputs = inputs or []
        self._outpus = outputs or []
        self._hash = self._calculate_hash()

    def __repr__(self) -> str:
        return f"Transaction({repr(self.hash)})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Transaction):
            return False

        return self.hash == other.hash

    def __hash__(self) -> int:
        return int(self.hash, 16)

    @property
    def hash(self) -> str:
        return self._hash

    @property
    def type(self) -> str:
        return self.type

    @property
    def inputs(self) -> List[TxIn]:
        return self._inputs

    @property
    def outputs(self) -> List[TxOut]:
        return self._outpus

    def _calculate_hash(self) -> str:
        return "Fake hash #TODO"
