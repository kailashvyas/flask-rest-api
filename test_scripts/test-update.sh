#!/usr/bin/env bash
curl -i -H "Content-Type: application/json" -X PUT -d '{
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

curl -i -H "Content-Type: application/json" -X PUT -d '{
    "base": "pasta",
    "box_type": "gourmet",
    "gousto_reference": 58,
    "marketing_description": "Tamil Nadu is a state on the eastern coast of the southern tip of India. Curry from there is particularly famous and its easy to see why. This one is brimming with exciting contrasting tastes from ingredients like chilli powder, coriander and fennel seed",
    "origin_country": "Great Britain",
    "recipe_cuisine": "italian",
    "title": "bhindi bhajee 21",
    "recipe_diet_type_id": "fish"
  }' http://localhost:5000/gousto/api/v1.0/recipes/9