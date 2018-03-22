# EdX Analysis

This is an analysis of EdX student data done on Jupyter Notebook using the Plotly Dash framework.

## Getting Started

These instructions will help you to install a working copy of the notebook on your machine.

### Setting up the environment:


1. First, you will need to **download** this master file onto your computer. Do this by clicking on the green **'Clone or download'** button above and then hitting **'Download ZIP'**.

2. You should be able to locate the edx_analysis-master folder in your recent downloads. I recommend moving the folder to your desktop for ease of access. You will need to create a **virtual environment** for the project. If you have never used python on your computer, I recommend following the steps below. Otherwise, you can jump ahead to step 3. 

To install pip, you will need to run the get-pip.py script. To do this, open your terminal window and type the following command:

```
sudo python get-pip.py
```

Then, you will need to install the virtual environments package:

```
sudo pip install virtualenv
```


3. To run the program, you must be in your working directory. To do this, move into the edx_analysis-master folder using the cd command: 

```
cd Desktop/edx_analysis-master
```

You are now in your working directory. You will need to create a virtual environment:

```
virtualenv env
```

And activate this environment:

```
source env/bin/activate
```

3. Next, you will need to install the necessary packages. They are all listed in the requirements.txt file, so you just need to type the following into the command window:

```
pip install -r requirements.txt
```

### Running the notebook

1. To run the notebook, type:

```
jupyter notebook
```

Along with the /env folder that you have just created, you should see this README.md file, three notebooks (.ipynb files), a requirements.txt file, and a sample_dataset.csv file. If you have no prior jupyter notebook experience, I recommend starting by opening the **startup_notebook.ipynb** file and running through the steps. Otherwise, the **dash_analysis.ipynb** notebook is the best place to start.

## Built With

* [Dash by Plotly](https://plot.ly/products/dash/)






