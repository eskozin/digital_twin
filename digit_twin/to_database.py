from django.conf import settings
import sqlite3

user = settings.DATABASES['default']['evgeniy']
password = settings.DATABASES['default']['digit1234']
database_name = settings.DATABASES['default']['VehicleProfile']

database_url = 'sqlite3://{user}:{password}@localhost:8000/{database_name}'.format(
    user=user,
    password=password,
    database_name=database_name,
)

mileage_per_day = 3
engine = create_engine(database_url, echo=False)
mileage_per_day.to_sql(name='mileage_per_day', con=engine)