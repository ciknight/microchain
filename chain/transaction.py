# -*- coding: utf-8 -*-
from typing import List, Optional
from decimal import Decimal
from chain import Hash


class TxType:
    Regular = "regular"
    Coinbase = "coinbase"

    All = (Regular, Coinbase)


class TxIn:
    def __init__(
        self, tx_hash: str, tx_index: int, value: Decimal, pubkey: str, signature: str
    ):
        self.tx_hash = tx_hash
        self.tx_index = tx_index
        self.value = value
        self.pubkey = pubkey
        self._signature = signature
        self._hash = self.calculate_hash()

    def __hash__(self) -> int:
        return int(self.hash, 16)

    def __eq__(self, other) -> bool:
        if not isinstance(other, TxIn):
            return False

        return self.hash == other.hash

    @property
    def hash(self):
        return self._hash

    @property
    def signature(self) -> str:
        return self._signature

    def calculate_hash(self) -> str:
        s: bytes = f"{self.tx_index}{self.tx_hash}{self.value}{self.pubkey}".encode()
        return Hash(s).hexdigest()


class TxOut:
    def __init__(self, amount: Decimal, address: str) -> None:
        self._amount = amount
        self._address = address

    def __eq__(self, other) -> bool:
        if not isinstance(other, TxOut):
            return False

        return (self.amount, self.address) == (other.amount, other.address)

    @property
    def amount(self) -> Decimal:
        return self._amount

    @property
    def address(self) -> str:
        return self._address


class Transaction:
    # Wiki https://en.bitcoin.it/wiki/Transaction

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
