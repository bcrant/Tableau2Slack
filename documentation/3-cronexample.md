# 3. Cron Example
I. &emsp; Intro  
II.&emsp; Under the Hood  
III.&emsp;Installation

This is tutorial is geared towards beginners that would like to learn how they can deploy this script to run on a schedule. If you are familiar with virtual environments and cron jobs, this won't be anything new for you.  

---  

After you have built the virtual environment on your machine using `virtualenv` and successfully ran the script from the terminal in that directory using something like...

`cd ~/tab2slack && python3.7 Tableau2Slack.py`

...the following code will execute Tableau2Slack.py at 9am on weekdays only, and print the output log to the virtual environment directory. (*Be sure to replace `/{project_path}/` with your own filepath to the project*)

```
0 9 * * 1-5 /{project_path}/tab2slack/venv/bin/python3.7 /{project_path}/tab2slack/Tableau2Slack.py >> /{project_path}/tab2slack/Tableau2Slack-cronlog.txt 2>&1
```

If you are unfamiliar with `crontab`, here is an excellent write up by Ole Michelsen that will get you up to speed:
[Schedule jobs with crontab on Mac OS X](https://ole.michelsen.dk/blog/schedule-jobs-with-crontab-on-mac-osx.html)

Now let's take a closer look at what is going on in that command...


## Under the Hood ##

`0 9 * * 1-5` declares the schedule the command will run on. Following the documentation from `crontab`...
```
* * * * *  command to execute
│ │ │ │ │
│ │ │ │ └─── day of week (0 - 6) (0 to 6 are Sunday to Saturday, or use names; 7 is Sunday, the same as 0)
│ │ │ └──────── month (1 - 12)
│ │ └───────────── day of month (1 - 31)
│ └────────────────── hour (0 - 23)
└─────────────────────── min (0 - 59)
```
...we can see we that the script will run at 0 minutes of the 9th hour on all days of the month for all months on the 1st through 5th day of the week (Mon-Fri).

During testing, I recommend you change the schedule to `* * * * *` to run the job every minute, but hey, it's your life. Go crazy. Take all the time you damn well please.

`/{project_path}/tab2slack/venv/bin/python3.7` specifies the `whereis` Python3.7 install that will run the script.

`/{project_path}/tab2slack/Tableau2Slack.py` is the complete filepath to the script, which we need to specify because by default `crontab` will use the home directory, which varies by machine and operating system. On MacOS this is `/Users`, but on Linux for instance the default home directory would be `/home`, but could also be somewhere under `/var` or `/usr`.

`>> /{project_path}/tab2slack/Tableau2Slack-cronlog.txt` tells the machine that when it executes Tableau2Slack.py, to redirect the output `>>` to a text file in the same directory as the script called `Tableu2Slack-cronlog.txt`.

`2>&1` says that since we redirected the standard output to that text file, we also want to print the standard error there as well. This is out of the scope of this project, but [here is a real page turner](https://www.brianstorti.com/understanding-shell-script-idiom-redirect/) explaining why 1 is `stdout` and 2 is `stderr` in this command.


## Installation ##

From your Mac OS terminal enter `$ crontab -e`

This will open `crontab` in edit mode.

Hit `i` on your keyboard to enter INSERT mode. If you already have cron jobs installed you can hit `a` to enter APPEND mode and skip to the end of the line.

Edit the filepaths in the command at the top of this document and paste them in. Each row and * is a separate `crontab` job.

To save, hit `esc` on your keyboard to exit INSERT mode, then type `:wq` and press ENTER on your keyboard to close the vim terminal.

If the command is accepted, you will receive the output: "crontab: installing new crontab".

To check what `crontab` jobs you have installed on your machine, you can run `$ crontab -l`.
