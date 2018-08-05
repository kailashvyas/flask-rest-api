import os
import pandas as pd
import numpy as np


class Csv:

    """ Csv class to handle database operations for csv file
    """

    def __init__(self, data_dir):
        """ Initialise Csv database
        Args:
            data_dir (string): data directory where csv file is stored
        """
        self.data_dir = data_dir
        self.table = pd.DataFrame()
        self.file_path = ''

    def select_table(self, table):
        self.file_path = os.path.dirname(os.path.realpath(__file__))+"/../"+self.data_dir+"/"+table+".csv"
        self.table = pd.read_csv(self.file_path)

    def get_columns(self):

        """ Get csv columns
        Returns:
            array: Returns array with column names
        """

        return self.table.columns.values

    def get_row(self, data_frame):

        """ Get Single Row
        Args:
            data_frame (DataFrame): dataframe object
        Returns:
            dict: Returns dictionary object
        """

        data_frame = data_frame.fillna('')

        records = data_frame.to_dict('records')

        if len(records) > 0:
            row = records[0]
        else:
            row = {}

        return row

    def query(self, field_name, field_value, fields='*'):

        """ Query Csv file
        Args:
            field_name (string): fieldname
            field_name (int/string): fieldvalue
            fields (string): comma seperated fields
        Returns:
            DataFrame: Returns data_frame
        """

        data_frame = self.table[self.table[field_name] == field_value]
        if fields != '*':
            data_frame = data_frame[fields.split(',')]

        return data_frame

    def get_counts(self, data_frame):

        """ Get total counts
        Args:
            data_frame (DataFrame): dataframe object
        Returns:
            int: Returns total counts
        """

        return len(data_frame)

    def get_results(self, data_frame, offset=0, limit=2):

        """ Get results from query
        Args:
            data_frame (DataFrame): dataframe object
            offset (int): Offset of results to start record from
            limit (int): No of records to return
        Returns:
             array: Returns results in array object
        """

        data_frame = data_frame.fillna('')

        return data_frame[offset:offset+limit].to_dict('records')

    def save(self, row):

        """ Save row
        Args:
            row (dict): dictionary object
        Returns:
            dict: Returns saved row as a dictionary object
        """

        row['id'] = int(self.table['id'].max()+1)
        columns = self.get_columns()
        data = {}
        for column in columns:
            if column in row.keys():
                data[column] = row[column]
            else:
                if self.table[column].dtype == 'int64' or self.table[column].dtype == 'float64':
                    data[column] = np.nan
                else:
                    data[column] = ''

        self.table.loc[len(self.table)] = data
        self.table.to_csv(self.file_path, index=False)

        return data

    def update(self, id, row):

        """ Update row
         Args:
             id (int): Id to update
             row (dict): dictionary object
         Returns:
             dict: Returns updated row as a dictionary object
         """

        row['id'] = id
        columns = self.get_columns()
        for column in columns:
            if column in row.keys():
                self.table.loc[self.table['id'] == id, column] = row[column]

        self.table.to_csv(self.file_path, index=False)

        return self.table[self.table['id'] == id].to_dict('records')

    def add_column_if_not_exists(self, column):

        """ Add column to Csv file if not exists
         Args:
             column (string): Column to add
         """
        columns = self.get_columns()

        if column not in columns:
            self.table[column] = np.nan
            self.table.to_csv(self.file_path, index=False)