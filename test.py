from flask import jsonify
data = {}
age = 34
if age > 20:
    data["Age"] = age
print(jsonify(data))
