# -*- coding: utf-8 -*-
from functools import partial
from hashlib import blake2b

__all__ = ['Hash', 'Block', 'Chain']

Hash = partial(blake2b, digest_size=32)

from microchain.block import Block  # isort:skip # noqa: E402
from microchain.chain import Chain  # isort:skip # noqa: E402
