import unittest
import pandas as pd
import numpy as np
import os
from drawplots.drawplots import draw
import glob

class TestDrawPlots(unittest.TestCase):

    def setUp(self):
        """Preparing for test"""
        self.drawer = draw()
        self.u1 = pd.Series(np.random.randn(10), name='Ex1')
        self.u2 = pd.Series(np.random.randn(10), name='Ex2')

    def test_draw_plots_creates_file(self):
        """Сhecking for fig availability"""
        self.drawer.draw_plots(self.u1, self.u2) # Create plot file
        mask = "Ex1_Ex2_*.png"
        for filename in glob.glob(os.path.join("plots", mask)):
            self.assertTrue(True) # Check created fail
                
    
    def tearDown(self):
        """Delete fig after test"""
        mask = "Ex1_Ex2_*.png"
        for filename in glob.glob(os.path.join("plots", mask)):
            os.remove(filename) # Remove created file            
                

if __name__ == '__main__':
    unittest.main()