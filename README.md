Flask-REST-Api
==============

Api for displaying, adding, updating and rating recipes

Installation
------------

After cloning, Install python 3.6 and pip https://pip.pypa.io/en/stable/installing/. Install dependencies specified in requirements.txt

    $ pip install -r requirements.txt

Running
-------

To run the server use the following command:

    $ python run.py
     * Running on http://127.0.0.1:5000/

Then from a different terminal window or browser you can send requests.

Heroku Deployment
-----------------

- https://salty-bastion-31857.herokuapp.com/gousto/api/v1.0/recipes/cuisine/british (Recipes by cuisine)
- https://salty-bastion-31857.herokuapp.com/gousto/api/v1.0/recipes/1 (Recipes by id)

Application is deployed to heroku and add, update and rating can be tested by running heroku-tests.sh in test_scripts

    $ sh heroku-tests.sh

Tests
-----

To run unit tests run following command

    $ python tests.py

API Documentation
-----------------

- POST **/gousto/api/v1.0/recipes**

    Add a new recipe.
    - The body must contain a JSON object that defines **'id','created_at' 'updated_at' 'box_type' 'title' 'slug' 'short_title' 'marketing_description' 'calories_kcal' 'protein_grams' 'fat_grams' 'carbs_grams' 'bulletpoint1' 'bulletpoint2' 'bulletpoint3' 'recipe_diet_type_id' 'season' 'base' 'protein_source' 'preparation_time_minutes' 'shelf_life_days' 'equipment_needed' 'origin_country' 'recipe_cuisine' 'in_your_box' 'gousto_reference'** fields.
    - Mandatory fields are **'title', 'marketing_description', 'recipe_diet_type_id', 'recipe_cuisine', 'gousto_reference'**. Others are optional
    - Query parameter fields can be passed for field filtering
    - On success a status code 201 is returned. The body of the response contains a JSON object with the newly added recipe.
    - On failure status code 400 (bad request) is returned.

- PUT **/gousto/api/v1.0/recipes/&lt;int:id&gt;**

    Update a recipe.
    - The body must contain a JSON object that defines 'id' 'created_at' 'updated_at' 'box_type' 'title' 'slug' 'short_title' 'marketing_description' 'calories_kcal' 'protein_grams' 'fat_grams' 'carbs_grams' 'bulletpoint1' 'bulletpoint2' 'bulletpoint3' 'recipe_diet_type_id' 'season' 'base' 'protein_source' 'preparation_time_minutes' 'shelf_life_days' 'equipment_needed' 'origin_country' 'recipe_cuisine' 'in_your_box' 'gousto_reference' fields.
    - Mandatory fields are 'title', 'marketing_description', 'recipe_diet_type_id', 'recipe_cuisine', 'gousto_reference'. Others are optional
    - On success a status code 200 is returned. The body of the response contains a JSON object with the newly added recipe.
    - On failure status code 400 (bad request) is returned.

- GET **/gousto/api/v1.0/recipes/&lt;int:id&gt;**

    Return a recipe.
    - Query parameter fields can be passed for field filtering
    - On success a status code 200 is returned. The body of the response contains a JSON object with recipe.
    - On failure status code 400 (bad request) is returned.


- GET **/gousto/api/v1.0/recipes/&lt;int:id&gt;**

    Return recipes.
    - Query parameter **fields** can be passed for field filtering
    - Query parameter **offset** and **limit** can be passed for paging
    - On success a status code 200 is returned. The body of the response contains a JSON object with pagination and recipes.
    - On failure status code 400 (bad request) is returned.

- PUT **/gousto/api/v1.0/recipes/rating/&lt;int:id&gt;**

    Rate a recipe between 0 and 5.
    - The body must contain a JSON object that defines rating.
    - On success a status code 200 is returned. The body of the response contains a JSON object with the recipe.
    - On failure status code 400 (bad request) is returned.

Example
-------

To create new recipe run command given below in terminal. Alternatively run bash script in test_scripts/test-create.sh.
This will create a new recipe

    $ curl -i -H "Content-Type: application/json" -X POST -d '{
        "base": "pasta",
        "box_type": "gourmet",
        "bulletpoint1": "Vibrant & Fresh",
        "bulletpoint2": "Warming, not spicy",
        "bulletpoint3": "Curry From Scratch",
        "calories_kcal": 524,
        "carbs_grams": 0,
        "equipment_needed": "Appetite",
        "fat_grams": 22,
        "gousto_reference": 58,
        "in_your_box": "king prawns, basmati rice, onion, tomatoes, garlic, ginger, ground tumeric, red chilli powder, ground cumin, fresh coriander, curry leaves, fennel seeds",
        "marketing_description": "Tamil Nadu is a state on the eastern coast of the southern tip of India. Curry from there is particularly famous and its easy to see why. This one is brimming with exciting contrasting tastes from ingredients like chilli powder, coriander and fennel seed",
        "origin_country": "Great Britain",
        "preparation_time_minutes": 40,
        "protein_grams": 12,
        "protein_source": "seafood",
        "recipe_cuisine": "italian",
        "recipe_diet_type_id": "fish",
        "season": "all",
        "shelf_life_days": 4,
        "short_title": "",
        "slug": "tamil-nadu-prawn-masala",
        "title": "bhindi bhajee"
      }' http://localhost:5000/gousto/api/v1.0/recipes

To update recipe run command given below in terminal. Alternatively run bash script in test_scripts/test-update.sh
This command will update recipe id 8 and updates title to bhindi bhajee test

    $ curl -i -H "Content-Type: application/json" -X PUT -d '{
        "base": "pasta",
        "box_type": "gourmet",
        "bulletpoint1": "Vibrant & Fresh",
        "bulletpoint2": "Warming, not spicy",
        "bulletpoint3": "Curry From Scratch",
        "calories_kcal": 524,
        "carbs_grams": 0,
        "created_at": "30/06/2015 17:58:00",
        "equipment_needed": "Appetite",
        "fat_grams": 22,
        "gousto_reference": 58,
        "in_your_box": "king prawns, basmati rice, onion, tomatoes, garlic, ginger, ground tumeric, red chilli powder, ground cumin, fresh coriander, curry leaves, fennel seeds",
        "marketing_description": "Tamil Nadu is a state on the eastern coast of the southern tip of India. Curry from there is particularly famous and its easy to see why. This one is brimming with exciting contrasting tastes from ingredients like chilli powder, coriander and fennel seed",
        "origin_country": "Great Britain",
        "preparation_time_minutes": 40,
        "protein_grams": 12,
        "protein_source": "seafood",
        "recipe_cuisine": "italian",
        "recipe_diet_type_id": "fish",
        "season": "all",
        "shelf_life_days": 4,
        "short_title": "",
        "slug": "tamil-nadu-prawn-masala",
        "title": "bhindi bhajee test"
      }' http://localhost:5000/gousto/api/v1.0/recipes/8


To get a recipe open following url.
This will return recipe with id 1

    http://localhost:5000/gousto/api/v1.0/recipes/1


To add a rating to url run following command
This will rate recipe id 8 with rating 5

    $ curl -i -H "Content-Type: application/json" -X PUT -d '{"rating": 5}' http://localhost:5000/gousto/api/v1.0/recipes/rating/8


To get recipes by cuisine.
Gets 10 recipes at a time

    https://salty-bastion-31857.herokuapp.com/gousto/api/v1.0/recipes/cuisine/british

Since we have only 4 records for british we can test by getting 2 records at a time. you should see pagination in json object which provides counts, limit and offset


    https://salty-bastion-31857.herokuapp.com/gousto/api/v1.0/recipes/cuisine/british?offset=0&limit=2 (first 2 records)

    https://salty-bastion-31857.herokuapp.com/gousto/api/v1.0/recipes/cuisine/british?offset=2&limit=2 (next 2 records)

I have also added a field filtering parameter which can be used to add, remove additional fields

    https://salty-bastion-31857.herokuapp.com/gousto/api/v1.0/recipes/cuisine/british?fields=id,slug,title


Faq
---

**How to use your solution?**

- I have provided api documentation regarding rest routes above and provided examples.
- For production I would add a caching layer like varnish in front of api for GET requests. POST requests will remain uncached

**Your reasons for your choice of web application framework?**

- I considered using Laravel, Lumen or Symfony but choose Flask. Since we  want to avoid using database I ended using Flask microframework on python.
- I used Pandas Python library as it is very good for processing CSV file the preferred source of the application

**Explain how your solution would cater for different API consumers that require different recipe data e.g. a mobile app and the front-end of a website**

- For Frontend website I would set limit to 10 to get 10 records at a time.
- For Mobile application I would use limit to 5 to reduce no of records at a time. Also I would add fields parameter to limit fields required.
- For example for getting recipes I can pass just id and title to  https://salty-bastion-31857.herokuapp.com/gousto/api/v1.0/recipes/cuisine/british?offset=0&limit=5&fields=id,title if we don't need any other fields
- We can also add field filtering while getting row https://salty-bastion-31857.herokuapp.com/gousto/api/v1.0/recipes/1?fields=id,title
- This would reduce bandwidth consumption on mobile and only load what is required for mobile application.


**Anything else you think is relevant to your solution?**

Ideally we should consider using a realtime database like Google Cloud Firebase which provides REST Api, Authentication, Hosting, ML kit, User notifications for mobile which is ideal for this Project

Todo
----

- Add more unit tests
- Add error handling
- Add oauth2 authentication
- Add docker file




