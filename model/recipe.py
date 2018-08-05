import datetime


class Recipe:

    """ Recipe Model class which gets result from database
    """

    def __init__(self, Db):

        """ Initialise database and select which table needs to be accessed
        Args:
            Db (Db): Db object is passed
        """

        self.db = Db
        self.db.select_table('recipe')

    def get_recipes_by_cuisine(self, cuisine, offset, limit, fields='*'):

        """ Get results by cuisine
        Args:
            cuisine (string): Cuisine to get records for
            offset (int): Offset of results to start record from
            limit (int): No of records to return
            fields (string): Comma seperated fields
        Returns:
             dict: Returns results in dictionary object
        """

        # build select query
        query = self.db.query('recipe_cuisine', cuisine, fields)
        # get total counts
        counts = self.db.get_counts(query)
        # get results
        results = self.db.get_results(query, offset, limit)
        # build pagination and return results
        data = {'paging': {
                    'records': counts,
                    'offset': offset,
                    'limit': limit
                },
                'data': results
                }

        return data

    def get_recipe_by_id(self, id, fields='*'):

        """ Get recipe by id
         Args:
             id (int): Id to get recipe
             fields (string): Comma seperated fields
         Returns:
             dict: Returns results in dictionary object
         """

        # build query
        query = self.db.query('id', id, fields)

        return self.db.get_row(query)

    def rate_recipe(self, id, rating):

        """ Rate recipe
         Args:
             id (int): Id to get recipe
             rating (dict): rating to update recipe
         Returns:
             dict: Returns results in dictionary object
         """

        self.db.add_column_if_not_exists('rating')
        # add updated_at
        rating['updated_at'] = self.get_date()

        return self.db.update(id, rating)

    def update_recipe(self, id, data):

        """ Update recipe
         Args:
             id (int): Id to update recipe
             data (dict): dictionary object with data
         Returns:
             dict: Returns row in dictionary object
         """

        data['slug'] = self.generate_slug(data['title'])
        data['updated_at'] = self.get_date()

        return self.db.update(id, data)

    def add_recipe(self, data):

        """ Add recipe
         Args:
             data (dict): dictionary object with data
         Returns:
             dict: Returns row added in dictionary object
         """

        data['slug'] = self.generate_slug(data['title'])
        data['created_at'] = self.get_date()
        data['updated_at'] = self.get_date()

        return self.db.save(data)

    def generate_slug(self, title):

        """ Add recipe
         Args:
             title (string): Title to create slug from
         Returns:
             string: Returns generated slug
         """

        return title.lower().replace(' ', '-')

    def get_date(self):

        """ Format and return date
         Returns:
             datetime: Returns formatted datetime
         """
        return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

