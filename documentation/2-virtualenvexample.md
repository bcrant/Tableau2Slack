# 2. Virtual Environment Example
I. &emsp; Intro  
II.&emsp; virtualenv Installation  
III.&emsp;virtualenv Set Up  
IV.&emsp;Environment Variables

This is tutorial is geared towards beginners that would like to learn how they can deploy this script to run on a schedule. If you are familiar with virtual environments and cron jobs, this won't be anything new for you.  

---  

We are going to use a Python package called `virtualenv` to create an isolated Python environment on our Mac OS. This means we will be able to run the script away from our global Python install and configurations, and therefore will not have to worry about dependencies or upgrades breaking our script in the future. If you have never heard of a virtual environment, I would recommend you begin by watching this video on [why you should use virtual environments](https://www.youtube.com/watch?v=N5vscPTWKOk_).

After we create the virtualenv, we will use a built-in Mac OS utility called `cron` to schedule the script to run in the virtual environment we have built at a frequency of our choosing. Cron is a powerful tool with minimal overhead and it will take you two minutes to learn -- more on that later.

## `virtualenv` Installation
Start by installing `virtualenv` to your global Python install. I will be demonstrating using Python3.7, if you use a different version some things may not hold true so be sure to adjust accordingly.

Install command: `pip install virtualenv`

Check the installation: `virtualenv --version`

Create a project folder for this virtual environment. Let's put it on your desktop and name it `tab2slack` (adjust your filepath).

`cd /Users/brian/Desktop && mkdir tab2slack`

Make sure you are in the directory we just created and double check where your Python3.7 installation is so that we can clone it in the virtual environment:
```
$ cd /Users/brian/Desktop/tab2slack

$ which python3.7
/usr/local/bin/python3.7
```

## `virtualenv` Set Up  
Time to create the environment. You can reference the [virtualenv documentation](https://virtualenv.pypa.io/en/stable/user_guide.html) for greater detail but here's the quick start. Be sure to change out the filepath for your python3.7 installation that we just grabbed above:

`virtualenv -p /usr/local/bin/python3.7 venv`

Take a peek inside the folder so you can see the results, then go back to terminal and activate the environment:

`source venv/bin/activate`

The name of the virtual environment should now appear to the left in your terminal. We'll go ahead and upgrade `pip` in the virtual environment:

`pip install --upgrade pip`


Next we need to install the packages required for this project. Download the `requirements.txt` from the Tableau2Slack repository on Github and put it in your local `tab2slack` project folder. While you're there download `Tableau2Slack.py` and do the same.

## Environment Variables  
I use the package `dotenv` to manage environment variables. This is where you hide your API keys ect by creating a `.env` file in the project folder to store the key pairs. They remain private by adding that file to your `.gitignore`.  

There are explanations and examples of these key pair values inline in the `Tableau2Slack.py` script and I have included a sample `.env` for you in repository with the variable names. You just need to add your own keys. If the file is not visible when you make or download it, on a Mac hit `Command + Shift + .` to show hidden files in your directories. /sidenote  

In your terminal, with the virtual environment activated and `requirements.txt` in your project folder, we will hop into the `site-packages` directory and install all of the package dependencies there:

`cd /{project_path}/tab2slack/venv/lib/python3.7/site-packages && pip install -r /{project_path}/tab2slack/requirements.txt -t .`

You can run `pip list` to double check that all the requirements are installed. Almost there! Head over to `cronexample.md` to schedule this script to run on your machine.
