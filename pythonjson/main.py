import json

# opening a json file
file = open('sample_data.py')
# load data from file to python object
content = json.load(file)
file.close()

outer_dict = {}
parameter_content = content["parametersList"]
for one in parameter_content:
    inner_dict = {}
    key = one["parameterName"]
    inner_dict["min"] = one["min"]
    inner_dict["max"] = one["max"]
    inner_dict["avg"] = one["avg"]
    outer_dict[key] = inner_dict
json_obj = json.dumps(outer_dict, indent=4)
print(json_obj)
# closing file

# json.dump(outer_dict, file)
