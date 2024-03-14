# importing libraries
# importing libraries
from flask import Flask, render_template  # to load html templates
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import io  # to convert the plot into an image that can be displayed on web page
import base64  # to convert image to string format for embedding in html

# create an instance of flask class
app = Flask(__name__)


# defining a function to load dataset
def load_data():
    df = sns.load_dataset('iris')
    return df


# creating visualization function
def plot(df):
    fig, ax = plt.subplots()
    # draw scatterplot using Seaborn library
    sns.scatterplot(x='petal_width', y="sepal_length", hue='species', data=df)
    # set title of the plot
    ax.set_title("Scatter Plot of Petal Width vs Sepal Length")
    # save the plot to bytes objects
    img = io.BytesIO()
    plt.savefig(img, format='png')
    # reset the file pointer to start
    img.seek(0)
    # converting the plot into Base64 encoded string so it could be embedded directly in HTML
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')

    return plot_url


@app.route('/')  # homepage route
def home():
    """Home Page"""
    df = load_data()
    plot_url = plot(df)
    return render_template('index.html', df=df, plot_div=plot_url)


if __name__ == '__main__':
    app.run(debug=True)
