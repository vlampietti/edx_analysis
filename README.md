# EdX Analysis

This is an analysis of EdX student data done on Jupyter Notebook using the [Plotly Dash](https://plot.ly/products/dash/) framework.

## Getting Started

These instructions will help you install a working copy of the notebook on your machine. The datasets are not included in this repository, so you will have to either a) link your application to a cloud database (I use Google BigQuery) or b) load csv files into your application folder.

### Setting up the environment:

1. First, you will need to install pip. (You can skip this step if you already have pip). Open your terminal window and type the following command:

```
sudo easy_install pip
```

This step is crucial, so if you are encountering errors we recommend looking through [this documentation](https://stackoverflow.com/questions/17271319/how-do-i-install-pip-on-macos-or-os-x). 

**Note:** the sudo command is a super user command. It allows you to run commands not executable by a regular user. The first time you use the sudo command, it will likely prompt you to enter your computer password. 

2. Next, you will need to create a **virtual environment** for the project. 

A virtual environment allows you to keep a separate copy of python and whatever other modules you need for a specific project. These modules have their own dependencies that may clash with one another. Virtual environments allow for you to work in one project's environment without affecting the rest of your computer's python modules. More documentation on this can be found [here](https://www.quora.com/Why-do-I-need-a-virtual-environment-in-Python-and-who-do-I-set-it-up) and [here](https://stackoverflow.com/questions/9410800/do-i-need-virtualenv).

```
sudo pip install virtualenv
```

3. Next, you will need to **download** this master file onto your computer. Do this by clicking on the green **'Clone or download'** button at the top of the page and then hitting **'Download ZIP'**.

4. You should be able to locate the **edx_analysis-master** folder in your recent downloads. I recommend moving the folder to your desktop for ease of access. Once you have moved the folder onto your desktop, you can move into the folder by opening your terminal window and typing the following command:

```
cd Desktop/edx_analysis-master
```

5. Once you are in your working directory, you will need to create and activate a virtualenv. In this case we have called our virtualenv 'env' but you can name it whatever you'd like.

Create the virtual environment:

```
virtualenv env
```

Activate this environment:

```
source env/bin/activate
```

**Note:** Activating an environment is something you will need to do each time you close the terminal window. You will know your environment is activated when you see '(env)' to the right of your prompt in the terminal window.

### Running the notebook and dashboard

1. You will need to install the necessary packages. After making sure your virtualenv is activated, to install a single package (for example the **numpy** package) you would type the following command in the terminal:

```
pip install numpy
```

However, this notebook has all of the packages listed in one requirements.txt file, so you can just type the following command into the terminal window:

```
pip install -r requirements.txt
```

If you would like to run the notebook as well as the dashboard, I recommend starting with step 2. This will install the notebook and give you access to all of the code. If you are only interested in running the dashboard application without the jupyter notebook, skip ahead to step 3.

2. To run the notebook, type:

```
jupyter notebook
```

Along with the /env folder that you have just created, you should see this README.md file, three notebooks (.ipynb files), two python scripts (.py files), a requirements.txt file, and a sample_dataset.csv file. If you have no prior jupyter notebook experience, I recommend starting by opening the **startup_notebook.ipynb** file and running through the steps. Otherwise, the **dash_analysis.ipynb** notebook is the best place to start.

3. To run the dashboard application, make sure your environment is activated (env) and type the following command:

```
python app.py
```

There is also a simple dash application under startup_dash.py that you can run by typing:

```
startup_dash.py
```

This is a simple way of understanding the backend of dash without all of the additional code. 

## Built With

* [Dash by Plotly](https://plot.ly/products/dash/)

