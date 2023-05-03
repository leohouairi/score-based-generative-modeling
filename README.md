# Score based generative modelling

Project realized for the "Deep leraning" course (ENSAE last year, DSSA track). 

We aim at applying the method proposed in the paper "Score-based generative modeling through stochastic differential equation" on another data set so as to generate images. 


## Notebooks

You can run these notebooks on Colab :

| Notebook-dataset | path | Colab Link |
| ---- | ---- | ---- |
| letter-emnist (**letter emnist matfile required**) | ./notebooks/letter-mnist/training_sampling_notebook_lettermnist.ipynb | [Colab Link](https://colab.research.google.com/github/leohouairi/score-based-generative-modeling/blob/main/notebooks/letter-mnist/training_sampling_notebook_lettermnist.ipynb)
| icon (**icon matfile required**) | ./notebooks/icon/training_sampling_notebook_icon.ipynb | [Colab Link](https://colab.research.google.com/github/leohouairi/score-based-generative-modeling/blob/main/notebooks/icon/training_sampling_notebook_icon.ipynb)
| notmnist | ./notebooks/notmnist/training_sampling_notebook_notmnist.ipynb  | [Colab Link](https://colab.research.google.com/github/leohouairi/score-based-generative-modeling/blob/main/notebooks/notmnist/training_sampling_notebook_notmnist.ipynb)
| kmnist | ./notebooks/kmnist/training_sampling_notebook_kmnist.ipynb | [Colab Link](https://colab.research.google.com/github/leohouairi/score-based-generative-modeling/blob/main/notebooks/kmnist/training_sampling_notebook_kmnist.ipynb)
| HASYv2 | ./notebooks/HASYv2/training_sampling_notebook_HASYv2.ipynb | [Colab Link](https://colab.research.google.com/github/leohouairi/score-based-generative-modeling/blob/main/notebooks/HASYv2/training_sampling_notebook_HASYv2.ipynb)




## Useful links 
- The paper: https://arxiv.org/abs/2011.13456
- A blogpost explaining the paper: https://yang-song.net/blog/2021/score/
- Yang Song's tutorial implementing the paper (python, torch), **on which our implementation is largely based** : https://colab.research.google.com/drive/120kYYBOVa1i0TD85RjlEkFjaWDxSFUx3?usp=sharing

## Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
