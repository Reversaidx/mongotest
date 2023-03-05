import sqlalchemy
from sqlalchemy import create_engine

engine = create_engine("mongodb:///?Server=127.0.0.1&;Port=27017&Database=someDb")
\