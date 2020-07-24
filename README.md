# **Tableau2Slack**
![img](https://badges.frapsoft.com/os/v1/open-source.svg?v=103) ![img](https://img.shields.io/badge/Free%3F-✅-534.svg) ![img](https://img.shields.io/badge/Maintained%3F-✅-534.svg) ![img](https://img.shields.io/badge/Stable%3F-✅-534.svg) ![img](https://img.shields.io/badge/Beginner%20Friendly%3F-✅-534.svg)
![img](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) ![img](https://img.shields.io/badge/style-API-E97627?label=Tableau&logo=Tableau) ![img](https://img.shields.io/badge/style-API-4A154B?label=Slack&logo=Slack)

As a data lover in a meme world, it can be challenging to command the attention of peers with things like sales updates, forecasts, and projections. I built Tableau2Slack to make our data visualizations more easily accessible to my colleagues; by sharing updates to them directly in Slack. Now you can too!

This repository includes detailed documentation and a beginner friendly step-by-step tutorial on how to deploy this script and automate sharing updates to Slack. I am happy to help if you have any problems getting started and am always open to feedback, collaboration, and additional contributions.

<img src="/documentation/NinaInAction.png" width=500px>  
<br/><br/>

_To learn more about this project check out [the Medium article.](https://medium.com/@briancrant/sharing-data-visualizations-to-slack-with-python-b6404eb5a535?source=friends_link&sk=dad9ab8fa333cd79302ed9705145f8be)_

## Contents  
[Tableau2Slack.py](https://github.com/bcrant/Tableau2Slack/blob/master/Tableau2Slack.py)  
requirements.txt  
.env (example for `dotenv` package. Read virtualenvexample.md)  
LICENSE  
README.md  
1-gettingstarted.md  
2-virtualenvexample.md  
3-cronexample.md  

## Documentation  
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

## Installation Preview / Summary
1. Clone the Tableau2Slack repository
2. Create and install a Slack bot to your Slack workspace as outlined in [Getting Started](https://github.com/bcrant/Tableau2Slack/blob/master/documentation/1-gettingstarted.md)
3. Replace the example variables in the `.env` file (pictured below) with your corresponding Tableau and Slack account information
<br/><img src="/documentation/QuickStart.png" width=300px>  
4. (Optional) Edit the JSON message body in Tableau2Slack.py to customize the Slack message and username/icon.

## Contributing  
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.  

Would love to create adaptations for other data visualization tools like Looker, Domo, and Power BI in the future.  

## License  
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://choosealicense.com/licenses/mit/)  

## Authors
Main authors:  
&emsp;&emsp;Brian Crant < brian@briancrant.com >

Special thanks to [Dylan Yile Wu](https://www.linkedin.com/in/yilewu/) for the inspiration. Even if it not used directly, [his work](https://github.com/DylanYileWu/slack_tableau_dashboard/blob/master/slack_tableau_dashboard.py) with the Tableau REST API heavily influenced the functionality of this project.

Many thanks to [John McDonald](https://www.linkedin.com/in/john-mcdonald-dev) for giving freely of his time and expertise to review drafts of the super duper scintillating documentation in this repository for public consumption. Not all heroes wear capes.
