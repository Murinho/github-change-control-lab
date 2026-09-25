import unittest

from policy import allows_internet_egress


class PolicyTests(unittest.TestCase):

    def test_edge_allows_internet(self):
        self.assertTrue(
            allows_internet_egress("edge")
        )

    def test_internal_blocks_internet(self):
        self.assertFalse(
            allows_internet_egress("internal")
        )
        
    def test_nat_allows_internet(self):
        self.assertTrue(
            allows_internet_egress("nat")
        )