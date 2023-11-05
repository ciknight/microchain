# -*- coding: utf-8 -*-
from kademlia.network import Server

from chain import BlockChain


class P2PServer(Server):
    max_inbound_peers_count = 125
    max_outbound_peers_count = 8

    def __init__(self, ksize=20, alpha=3, node_id=None, storage=None, mining=False):
        super().__init__(ksize, alpha, node_id, storage)
        self.mining = mining
        self.load_blockchain()

    def load_blockchain(self):
        # load blockchain from db or init
        self.blockchain = BlockChain()
