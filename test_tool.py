import unittest
from tool import breaking,diff
class ContractTests(unittest.TestCase):
 def test_diff(self):
  result=diff({'fields':{'a':{'type':'str','required':False},'b':{'type':'int'}}},{'fields':{'a':{'type':'int','required':True},'c':{'type':'str'}}});self.assertEqual(result['removed'],['b']);self.assertEqual(result['type_changed'],['a']);self.assertTrue(breaking(result))
if __name__=='__main__':unittest.main()
