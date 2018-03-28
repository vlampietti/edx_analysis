# EdX Analysis

This is an analysis of EdX student data done on Jupyter Notebook using the Plotly Dash framework.

## Getting Started

These instructions will help you to install a working copy of the notebook on your machine.

### Setting up the environment:


1. First, you will need to **download** this master file onto your computer. Do this by clicking on the green **'Clone or download'** button above and then hitting **'Download ZIP'**.

2. You should be able to locate the edx_analysis-master folder in your recent downloads. I recommend moving the folder to your desktop for ease of access. Once you have moved the folder onto your desktop, you can move into the folder by opening your terminal window and typing the following command:

```
cd Desktop/edx_analysis-master
```

3. You will need to create a **virtual environment** for the project. If you have never used Python on your computer, I recommend following the steps below. Otherwise, you can jump ahead to step 4. 


To install pip, you will need to run the get-pip.py script. To do this, open your terminal window and type the following command:

```
sudo python get-pip.py
```

Installing pip is often dependent on the version of python running on your computer as well as what other programs might be operating in the background. You may encounter some errors, so we have included the source file [here](https://pip.pypa.io/en/stable/installing/) as well as some [additional documentation](https://stackoverflow.com/questions/17271319/how-do-i-install-pip-on-macos-or-os-x).  

**Note:** the sudo command is a super user command. It allows you to run commands not executable by a regular user. The first time you use the sudo command, it will likely prompt you to enter your computer password. 

4. After installing pip, you will need to install the virtual environments package:

```
sudo pip install virtualenv
```

Create a virtual environment:

```
virtualenv env
```

And activate this environment:

```
source env/bin/activate
```

5. Next, you will need to install the necessary packages. They are all listed in the requirements.txt file, so you just need to type the following into the command window:

```
pip install -r requirements.txt
```

### Running the notebook and dashboard

If you would like to run the notebook as well as the dashboard, I recommend starting with step 1. This will install the notebook and give you access to all of the code. If you are only interested in running the dashboard application without the jupyter notebook, skip ahead to step 2.

1. To run the notebook, type:

```
jupyter notebook
```

Along with the /env folder that you have just created, you should see this README.md file, three notebooks (.ipynb files), a requirements.txt file, and a sample_dataset.csv file. If you have no prior jupyter notebook experience, I recommend starting by opening the **startup_notebook.ipynb** file and running through the steps. Otherwise, the **dash_analysis.ipynb** notebook is the best place to start.

2. To run the dashboard application, make sure your environment is activated (env) and type the following command:

```
python app.py
```

## Built With

* [Dash by Plotly](https://plot.ly/products/dash/)

