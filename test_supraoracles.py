# test_supraoracles.py
"""
Tests for SupraOracles module.
"""

import unittest
from supraoracles import SupraOracles

class TestSupraOracles(unittest.TestCase):
    """Test cases for SupraOracles class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SupraOracles()
        self.assertIsInstance(instance, SupraOracles)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SupraOracles()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
