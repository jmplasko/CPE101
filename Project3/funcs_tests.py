import unittest
import solver_funcs

class TestSolver(unittest.TestCase):

   def test_col_1(self):
      puzzel = [[1,1,1,1,1],[2,2,2,2,2],[3,3,3,3,3],[4,4,4,4,4],[5,5,1,5,5]]
      self.assertEqual(solver_funcs.check_columns_valid(puzzel), False)

   def test_col_2(self):
      puzzel = [[1,1,1,1,1],[2,2,2,2,2],[3,3,3,3,3],[4,4,4,4,4],[5,5,5,5,5]]
      self.assertEqual(solver_funcs.check_columns_valid(puzzel), True)

   def test_col_3(self):
      puzzel = [[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
      self.assertEqual(solver_funcs.check_columns_valid(puzzel), True)


   def test_row_1(self):
      puzzel = [[1,2,3,4,5],[1,3,2,4,5],[5,4,3,2,1],[5,1,2,3,4],[3,4,2,5,1]]
      self.assertEqual(solver_funcs.check_rows_valid(puzzel), True)

   def test_row_3(self):
      puzzel = [[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
      self.assertEqual(solver_funcs.check_rows_valid(puzzel), True)


   def test_row_2(self):
      puzzel = [[1,2,3,4,5],[1,3,2,4,5],[5,4,3,2,1],[5,1,2,3,4],[3,4,2,5,2]]
      self.assertEqual(solver_funcs.check_rows_valid(puzzel), False)

   def test_cageval__1(self):
      puzzel = [[4,1,2,5,3],[1,5,4,3,2],[2,3,5,4,1],[3,4,1,2,5],[5,2,3,1,4]]
      cage = [[5,2,0,5],[8,3,1,2,6],[8,2,3,8],[6,3,4,9,14],[13,3,7,12,13],[5,2,10,15],[14,4,11,16,20,21],[6,3,17,18,22],[10,3,19,23,24]]
      self.assertEqual(solver_funcs.check_cages_valid(puzzel,cage), True)

   def test_cageval__2(self):
      puzzel = [[4,1,2,5,3],[1,5,4,3,2],[2,3,5,4,1],[3,4,1,2,5],[5,2,3,1,5]]
      cage = [[5,2,0,5],[8,3,1,2,6],[8,2,3,8],[6,3,4,9,14],[13,3,7,12,13],[5,2,10,15],[14,4,11,16,20,21],[6,3,17,18,22],[10,3,19,23,24]]
      self.assertEqual(solver_funcs.check_cages_valid(puzzel,cage), False)

   def test_cageval__3(self):
      puzzel = [[4,1,2,4,3],[1,5,4,3,2],[2,3,5,4,1],[3,4,1,2,5],[5,2,4,1,3]]
      cage = [[5,2,0,5],[8,3,1,2,6],[8,2,3,8],[6,3,4,9,14],[13,3,7,12,13],[5,2,10,15],[14,4,11,16,20,21],[6,3,17,18,22],[10,3,19,23,24]]
      self.assertEqual(solver_funcs.check_cages_valid(puzzel,cage), False)

   def test_cageval__4(self):
      puzzel = [[4,1,2,5,3],[1,5,4,3,3],[2,3,5,4,0],[3,4,1,2,5],[5,2,3,1,4]]
      cage = [[5,2,0,5],[8,3,1,2,6],[8,2,3,8],[6,3,4,9,14],[13,3,7,12,13],[5,2,10,15],[14,4,11,16,20,21],[6,3,17,18,22],[10,3,19,23,24]]
      self.assertEqual(solver_funcs.check_cages_valid(puzzel,cage), False)

   def test_cageval__5(self):
      puzzel = [[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
      cage = [[5,2,0,5],[8,3,1,2,6],[8,2,3,8],[6,3,4,9,14],[13,3,7,12,13],[5,2,10,15],[14,4,11,16,20,21],[6,3,17,18,22],[10,3,19,23,24]]
      self.assertEqual(solver_funcs.check_cages_valid(puzzel,cage), True)

   def test_check__1(self):
      puzzel = [[1,2,3,4,5],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
      cage = [[5,2,0,5],[8,3,1,2,6],[8,2,3,8],[6,3,4,9,14],[13,3,7,12,13],[5,2,10,15],[14,4,11,16,20,21],[6,3,17,18,22],[10,3,19,23,24]]
      self.assertEqual(solver_funcs.check_valid(puzzel,cage), True)  

   def test_check__2(self):
      puzzel = [[4,1,2,5,3],[4,5,4,3,2],[2,3,5,4,1],[3,4,1,2,5],[5,2,3,1,4]]
      cage = [[5,2,0,5],[8,3,1,2,6],[8,2,3,8],[6,3,4,9,14],[13,3,7,12,13],[5,2,10,15],[14,4,11,16,20,21],[6,3,17,18,22],[10,3,19,23,24]]
      self.assertEqual(solver_funcs.check_valid(puzzel,cage), False)

if __name__ == '__main__':
   unittest.main()
