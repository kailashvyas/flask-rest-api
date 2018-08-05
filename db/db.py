from db import csv


class Db:

    """ Db class
    """

    def __init__(self, type, data_path):
        """ Initialise database
        """
        if type == 'csv':
            self.db = csv.Csv(data_path)
        else:
            raise ValueError('Database type'+str(type)+' not supported')

    def get_db(self):
        """ Get database object
        """

        return self.db