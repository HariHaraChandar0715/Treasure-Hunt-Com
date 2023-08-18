from flask import Flask
from flask import request
from flask import jsonify
import pandas as pd

data = {"sales": [470, 560, 670, 2000, 450, 770]}
df = pd.DataFrame(data)

app = Flask(__name__)


@app.route("/api/get_independent", methods=['GET', 'POST'])
def display():
    try:
        df_json = df.to_dict(orient='records')
        return jsonify(df_json)
    except Exception as e:
        return jsonify({"Error": str(e)})


if __name__ == '__main__':
    app.run(debug=True)
