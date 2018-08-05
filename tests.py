import os
import unittest
import pandas as pd

from db import csv

class CsvTests(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################

    # executed prior to each test
    def setUp(self):
        # create a test database
        list = [{'id':1, 'title':'test db'}]
        df = pd.DataFrame(list)
        df.to_csv('data/test.csv', index=False)
        csv_obj = csv.Csv('data')
        # test with test database
        csv_obj.select_table('test')

        self.csv_obj = csv_obj

    # executed after each test
    def tearDown(self):
        if os.path.exists('data/test.csv'):
            os.remove('data/test.csv')
        pass

    ###############
    #### tests ####
    ###############

    def test_get_columns(self):
        columns = self.csv_obj.get_columns()
        self.assertTrue('title' in columns)

    def test_get_query(self):
        query = self.csv_obj.query('id', 1)
        self.assertTrue(type(query) == pd.core.frame.DataFrame)

    def test_get_counts(self):
        query = self.csv_obj.query('id', 1)
        counts = self.csv_obj.get_counts(query)
        self.assertEqual(counts, 1)

    def test_get_results(self):
        query = self.csv_obj.query('id', 1)
        results = self.csv_obj.get_results(query)
        self.assertTrue(len(results) > 0)
        self.assertEqual(results[0]['id'], 1)

    def test_get_row(self):
        query = self.csv_obj.query('id', 1)
        row = self.csv_obj.get_row(query)
        self.assertEqual(row['id'], 1)

    def test_save(self):
        record = {
            'title': 'test save record'
          }
        self.csv_obj.save(record)
        query = self.csv_obj.query('id', 2)
        row = self.csv_obj.get_row(query)
        self.assertEqual(row['id'], 2)

    def test_update(self):
        record = {
            'id':1,
            'title': 'update test title'
          }
        self.csv_obj.update(1, record)
        query = self.csv_obj.query('id', 1)
        row = self.csv_obj.get_row(query)
        self.assertEqual(row['title'], 'update test title')


if __name__ == "__main__":
    unittest.main()