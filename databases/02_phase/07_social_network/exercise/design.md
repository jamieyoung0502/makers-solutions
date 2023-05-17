# Single Table Design Recipe Template

_Copy this recipe template to design and create a database table from a specification._

## 1. Extract nouns from the user stories or specification

```
As a food lover,
So I can stay organised and decide what to cook,
I'd like to keep a list of all my recipes with their names.

As a food lover,
So I can stay organised and decide what to cook,
I'd like to keep the average cooking time (in minutes) for each recipe.

As a food lover,
So I can stay organised and decide what to cook,
I'd like to give a rating to each of the recipes (from 1 to 5).
```

```
Nouns: recipes, name, average cooking time, rating


```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record | Properties                  |
| ------ | --------------------------- |
| recipe | title, cooking_time, rating |

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask yoid ur peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
id: SERIAL
title: text
cooking_time: int
rating: int
```

## 4. Write the SQL

```sql

CREATE TABLE recipes (
  id SERIAL PRIMARY KEY,
  title text,
  cooking_time int,
  rating int
);

```

## 5. Create the table

```bash
psql -h 127.0.0.1 recipes < recipes_table.sql
```

### Recipe Tests

```python
"""
Creates an instance of Recipe with an id, time and rating
"""

"""
We can format recipes to look nice
"""

"""
We can compare two identical recippes
And have them be equal
"""
```

### Recipe Repository Tests

```python
"""
When we call RecipeRepository#all
We get a list of Recipe objects reflecting the seed data.
"""

"""
When we call RecipeRepository#find
We get a single Recipe object reflecting the seed data.
"""

# """
# When we call RecipeRepository#create
# We get a new record in the database.
# """

# """
# When we call RecipeRepository#update
# We update a record in the database.
# """

# """
# When we call RecipeRepository#delete
# We remove a record from the database.
# """
```
