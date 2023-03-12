from flask import Flask, render_template
import nbformat
from nbconvert import HTMLExporter

app = Flask(__name__)

# Load the Jupyter notebook file (.ipynb) using nbformat
with open('Sports_Prediction.ipynb') as f:
    nb = nbformat.read(f, as_version=4)

# Convert the Jupyter notebook to HTML using nbconvert
html_exporter = HTMLExporter()
(body, resources) = html_exporter.from_notebook_node(nb)

# Define a route to render the HTML output of the notebook
@app.route('/')
def index():
    return render_template('index.html', body=body)

app.debug = True

if __name__ == '__main__':
    app.run()
