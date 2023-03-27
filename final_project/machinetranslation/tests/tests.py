from machinetranslation.translator import englishToFrench, frenchToEnglish
import unittest
from ibm_cloud_sdk_core.api_exception import ApiException

class TranslatorTest(unittest.TestCase):
    def english2french(self):
        self.assertEqual(englishToFrench('Hello'),'Bonjour')
    def frenchToEnglish(self):
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
    def nulltest1(self):
        self.assertRaises(ApiException, englishToFrench(''))
    def nulltest2(self):
        self.assertRaises(ApiException, frenchToEnglish(''))        

if __name__=='__main__':
    unittest.main()