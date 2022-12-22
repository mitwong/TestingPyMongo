# Insert rows into a testing table "delete_by_date_testing" to fill the table with data we can then test deletion by date on.
from pymongo_get_database import get_database
dbname = get_database()
collection_name = dbname["delete_by_date_testing"]

from datetime import datetime, timedelta
generated_items = []
now = datetime(year = 2022, month = 1, day = 1)
for i in range (0,100):
    item = {
        "id" : i,
        "create_date_utc" : now
    }

    generated_items.append(item)

    now += timedelta(hours = 6)

collection_name.insert_many(generated_items)

# index on creation time
category_index = collection_name.create_index("create_date_utc")

from pandas import DataFrame
items_df = DataFrame(collection_name.find())
print(items_df)