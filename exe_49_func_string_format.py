def message(dct):
    name = dct['name']
    role = dct['role']
    movie = dct['movie'] 
    print(f'In {movie}, {name} is a {role}')

message(
    {
    "name": "Han Solo",
    "role": "smuggler",
    "movie": "Star Wars"
    }
)
