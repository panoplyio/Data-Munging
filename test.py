import unittest
from Part_Three import *

class TestDataMunging(unittest.TestCase):

    def test_compare_difference(self):
        objBigger = PartThree_Shared_Functionality.SharedObject('obj1', 10, 0)
        objSmaller = PartThree_Shared_Functionality.SharedObject('obj2', 0, 0)

        result = compare_difference(objBigger, objSmaller)
        self.assertEqual(result, objSmaller)


    # tests for csv football data
    def test_check_validity_of_the_object_soccerTrue(self):
        result = PartThree_SoccerLeagueTable.check_validity_of_the_object('10', '2', 'Arsenal')
        self.assertTrue(result)


    def test_check_validity_of_the_object_soccerFalseChar(self):
        result = PartThree_SoccerLeagueTable.check_validity_of_the_object('c', '2', 'Arsenal')
        self.assertFalse(result)


    # tests for jason wheather data
    def test_check_validity_of_the_object_weatherTrue(self):
        obj = {u'MxT': u'88', u'MnT': u'59', u'Dy': u'1'}
        result = PartThree_WeatherData.check_validity_of_the_object(obj, '1', '88', '59')
        self.assertTrue(result)


    def test_check_validity_of_the_object_weatherFalseObj(self):
        obj = {u'MxT': u'88', u'Dy': u'1'}
        result = PartThree_WeatherData.check_validity_of_the_object(obj, '1', '88', '59')
        self.assertFalse(result)


    def test_check_validity_of_the_object_weatherFalseDay(self):
        jsonObj = {u'MxT': u'88', u'MnT': u'59', u'Dy': u'1'}
        result = PartThree_WeatherData.check_validity_of_the_object(jsonObj, '-1', '88', '59')
        self.assertFalse(result)


    def test_object_decoder(self):
        validLine = '{ "Dy": "1", "MxT": "88", "MnT": "59" }'
        obj = PartThree_Shared_Functionality.SharedObject('1', 88, 59)
        result = PartThree_WeatherData.object_decoder(validLine)
        return obj.__dict__ == result.__dict__



if __name__ == '__main__':
    unittest.main()
