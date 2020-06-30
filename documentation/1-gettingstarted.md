## 1. Getting Started ##

All you will need is a connection to the internet, a Slack account, and a Tableau account. This script requires you to create and install a Slack Bot to your Slack workspace.

If you are familiar with hiding API keys and passwords by using environment variables in Python, all you need to do is gather the requirements below and plug them into the `.env` file and add that file to your `.gitignore`.

For those of you with limited to no experience with Python, APIs, or automation, the `virtualenvexample.md` and `cronexample.md` documents in this repository are geared towards you and will guide you through setting up and deploying this script using only your Mac OS or Linux machine.

### Gather Tableau Credentials ###
Get your Tableau Online or Server information ready. You can add this to the `.env` as you go or store elsewhere, but keep these handy.

__You will need:__  
Tableau Account Email  
Tableau Account Password  
Tableau Server Domain (list of Tableau Online [server domains here](https://help.tableau.com/current/online/en-us/to_keep_data_fresh.htm#safelist))  
Tableau Site Name (is probably `yourcompanyname`)  
Tableau View Name  
Filename for Image

### Configure Slack ###
You will need some admin permissions for the steps below.

1. Create a new [Slack App](https://api.slack.com/apps) for your workspace configured for `Bots` and `Permissions`.

2. Create a Slack Bot and give it `chat:write`, `chat:write.customize`, and `files:write` Bot Token Scopes.

3. Install your Slack Bot to your workspace.

4. Add the Slack Bot User OAuth Access Token to `.env`

5. Add the channel you want to post to in `.env` (You can use a test one for now and change this later)

6. Create a #tableau-test channel in your Slack account to store the image.

Quick Note about Step 6:  
The Slack Bot sends a multi-part message to include custom formatting. To avoid these parts sending as *multiple posts*, this step creates a private URL to host the image in your Slack workspace, which allows the final message to appear as *one post* with multiple parts using the Slack Block Kit.

Now that you have defined all of your variables in your `.env` file, head to `virtualenvexample.md` to learn how to create an isolated environment for the script to run.
