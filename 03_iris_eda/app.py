from flask import Flask, render_template
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import io
import base64
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

app = Flask(__name__)

@app.route('/')
def index():
    # Download the Iris dataset using Seaborn
    iris = sns.load_dataset('iris')
    
    # Perform EDA on the dataset
    num_species = len(iris['species'].unique())
    mean_sepal_length = iris[['species', 'sepal_length']].groupby('species').mean()
    mean_petal_width = iris[['species', 'petal_width']].groupby('species').mean()

    # Create plots based on EDA results
    fig1, ax1 = plt.subplots()
    ax1.bar(mean_sepal_length.index, mean_sepal_length['sepal_length'])
    ax1.set_ylabel("Mean Sepal Length")
    ax1.set_xticklabels(ax1.get_xticks(), rotation=90)

    fig2, ax2 = plt.subplots()
    ax2.bar(mean_petal_width.index, mean_petal_width['petal_width'])
    ax2.set_ylabel("Mean Petal Width")
    ax2.set_xticklabels(ax2.get_xticks(), rotation=90)

    # Convert plot to bytes format
    buf1 = io.BytesIO()
    fig1.savefig(buf1, format='png')
    buf1.seek(0)
    string1 = base64.b64encode(buf1.read()).decode()

    buf2 = io.BytesIO()
    fig2.savefig(buf2, format='png')
    buf2.seek(0)
    string2 = base64.b64encode(buf2.read()).decode()

    return  render_template('index.html', species_count=num_species,
                       sepal_plot_base64=string1, petal_plot_base64=string2)

if __name__ == '__main__':
    app.run(debug=True)