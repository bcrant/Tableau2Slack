# **Tableau2Slack**
Tableau2Slack is a Python 3.7 script that utilizes the Tableau Server Client Python library to open a specific view on a Tableau Server (including a Tableau Online server), downloads an image of that view to disk, triggers a Slack Bot to post the image to a specific channel in a Slack workspace, then removes the image from disk.

## Contents  
Tableau2Slack.py  
requirements.txt  
.env (example for `dotenv` package. Read virtualenvexample.md)  
LICENSE  
README.md  
1-gettingstarted.md  
2-virtualenvexample.md  
3-cronexample.md  

## Documentation  
For more information about how to customize this script for your workflow, check out the Medium article: link2mediumarticle.com  
1. **[Getting Started](https://github.com/bcrant/Tableau2Slack/blob/master/documentation/1-gettingstarted.md)**
2. **[Virtual Environment Tutorial](https://github.com/bcrant/Tableau2Slack/blob/master/documentation/2-virtualenvexample.md)**
&emsp;&emsp;I. &emsp; Intro  
&emsp;&emsp;II.&emsp; `virtualenv` Installation  
&emsp;&emsp;III.&emsp;`virtualenv` Set Up  
&emsp;&emsp;IV.&emsp; Environment Variables Example
3. **[Cron Tutorial](https://github.com/bcrant/Tableau2Slack/blob/master/documentation/3-cronexample.md)**
&emsp;&emsp;I. &emsp; Intro  
&emsp;&emsp;II.&emsp; Under the Hood  
&emsp;&emsp;III.&emsp;Installation

## Contributing  
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License  
[MIT](https://choosealicense.com/licenses/mit/)

## Authors
Main authors:  
&emsp;&emsp;Brian Crant < brian@briancrant.com >

Special thanks to [Dylan Yile Wu](https://www.linkedin.com/in/yilewu/) for the inspiration. Even if it not used directly, [his work](https://github.com/DylanYileWu/slack_tableau_dashboard/blob/master/slack_tableau_dashboard.py) with the Tableau REST API heavily influenced the functionality of this project.

Many thanks to [John McDonald](https://www.linkedin.com/in/john-mcdonald-dev) for giving freely of his time and expertise, as well as proofing the super duper scintillating documentation in this repository for public consumption. Not all heroes wear capes.
