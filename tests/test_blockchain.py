# -*- coding: utf-8 -*-

from microchain import Block, Chain


def test_block():
    args = (0, '0', '')
    nonce = 0
    target = '0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'
    block = Block(*args, nonce=nonce, target=target)
    assert block.valid is True
    block.index = 100
    assert block.valid is False


def test_genesis_block():
    block = Chain.genesis()
    assert block.valid is True
    block.hash = 'abcdef'
    assert block.valid is False


def test_chain():
    chain = Chain()
    length = 2
    for _ in range(length):
        chain.mine()

    assert len(chain) != length
