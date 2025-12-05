from sqlalchemy import create_engine

# engine = create_engine("postgresql://mypassword:myuser@localhost:5432/ny_taxi")
# Change 'localhost' to '127.0.0.1'
# engine = create_engine("postgresql://myuser:mypassword@127.0.0.1:5432/ny_taxi")
engine = create_engine("postgresql://postgres:root@127.0.0.1:5432/ny_taxi")

engine.connect()
print("Connected!")
