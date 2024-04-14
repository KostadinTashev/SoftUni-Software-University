import importlib

mod = importlib.import_module('test_1')
print(mod.__dict__)
for (key, value) in mod.__dict__.items():
    if key.startswith('Create') and key.endswith('View'):
        print(key)
        print(value)
