import sys, unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'examples'))
import numpy as np
from core import prepare_data

class WindowTests(unittest.TestCase):
    def test_alignment_and_final_available_window(self):
        X,y=prepare_data(np.arange(12),4,2)
        self.assertEqual(X.shape,(7,4)); self.assertEqual(y.shape,(7,2))
        np.testing.assert_array_equal(X[0],[0,1,2,3])
        np.testing.assert_array_equal(y[0],[4,5])
        np.testing.assert_array_equal(y[-1],[10,11])
        self.assertTrue(np.all(X[:,-1]<y[:,0]))
    def test_exact_and_insufficient_history(self):
        self.assertEqual(len(prepare_data(np.arange(6),4,2)[0]),1)
        self.assertEqual(len(prepare_data(np.arange(5),4,2)[0]),0)
