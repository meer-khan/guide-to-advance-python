import pickle

# Pickling an object
data = {'name': 'Alice', 'age': 30}
with open('data', 'wb') as f:
    print(f)
    pickle.dump(data, f)


# Unpickling the object
with open('data', 'rb') as f:
    print(f)
    loaded_data = pickle.load(f)

print(loaded_data)