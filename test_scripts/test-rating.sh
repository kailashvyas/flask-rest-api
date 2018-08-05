#!/usr/bin/env bash
curl -i -H "Content-Type: application/json" -X PUT -d '{
    "rating": 3
  }' http://localhost:5000/gousto/api/v1.0/recipes/rating/8