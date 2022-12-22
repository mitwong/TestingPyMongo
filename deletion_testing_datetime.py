from pymongo_get_database import get_database
dbname = get_database()

from datetime import datetime
deletion_cutoff_utc = datetime(year = 2022, month = 1, day = 10)

filter = {"create_date_utc": {"$lt" : deletion_cutoff_utc}}
deleted_return = dbname["delete_by_date_testing"].delete_many(filter)

# run this to delete all
# deleted_return = dbname["delete_by_date_testing"].delete_many({})

print(f"Count deleted: {deleted_return.deleted_count}")

from pandas import DataFrame
current_documents = dbname["delete_by_date_testing"].find()
print(DataFrame(current_documents))

