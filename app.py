from flask import Flask, render_template, request
import pandas as pd
#from bokeh.charts import Histogram
#from bokeh.embed import components

app = Flask(__name__)

# Load the Iris Data Set
iris_df = pd.read_csv("data/data_1.txt", 
    names=["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Species"])
feature_names = iris_df.columns[0:-1].values.tolist()


# Index page
@app.route('/')
def index():
	# Determine the selected feature
	current_feature_name = request.args.get("feature_name")
	if current_feature_name == None:
		current_feature_name = "Sepal Length"


# With debug=True, Flask server will auto-reload 
# when there are code changes
if __name__ == '__main__':
	app.run(port=5000, debug=True)