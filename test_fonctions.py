import fonctions, unittest

class MyTest(unittest.TestCase):
    def test_moy_qcq(self):
        result = fonctions.calc_moyenne([1,2,3,12])
        self.assertEqual(result,4.5)

    def test_val_sup_qcq(self):
        result = fonctions.calc_val_sup([1,2,3,12],4.5)
        self.assertEqual(result,1)

    def test_val_inf_qcq(self):
        result = fonctions.calc_val_inf([1,2,3,12],4)
        self.assertEqual(result,3)
        

if __name__ == '__main__':
    unittest.main()
