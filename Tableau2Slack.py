import logging
import traceback
import os
import requests
from datetime import datetime, timezone
import pytz
import json
from dotenv import load_dotenv
import tableauserverclient as TSC
from slack import WebClient
from slack.errors import SlackApiError
import nest_asyncio

nest_asyncio.apply()


def Tableau2Slack():
    try:
        # Import Tableau environment variables
        load_dotenv()  # EXAMPLE VALUES:
        tabAccount = os.getenv("tabAcct")  # email@email.com
        tabPass = os.getenv("tabPwd")  # password
        tabDomain = os.getenv("tabDomain")  # site-id
        tabServer = os.getenv("tabServer")  # https://10ay.online.tableau.com
        tabView = os.getenv("tabView")  # InvestorUpdate
        tabPath = os.getenv("tabPath")  # ./InvestorUpdate.png
        # For further explanation of Tableau environment variables visit:
        # https://tableau.github.io/server-client-python/docs/api-ref#tableauauth-class
        # Full list of Tableau Online Server Domains for tabServer variable:
        # https://help.tableau.com/current/online/en-us/to_keep_data_fresh.htm#safelist

        print("Talking to Tableau...\n")
        tableau_auth = TSC.TableauAuth(tabAccount, tabPass, tabDomain)
        server = TSC.Server(tabServer)

        # Searching Tableau Online account for the View we declared in env variables
        with server.auth.sign_in(tableau_auth):
            server.use_server_version()
            req_option = TSC.RequestOptions()
            req_option.filter.add(
                TSC.Filter(
                    TSC.RequestOptions.Field.Name,
                    TSC.RequestOptions.Operator.Equals,
                    tabView,
                )
            )
            all_views, pagination_item = server.views.get(req_option)
            # Error catching for bad View names
            if not all_views:
                raise LookupError("View with the specified name was not found.")
            view_item = all_views[0]
            # Force refresh of screenshot if cached image more than one hour old
            max_age = "1"
            if not max_age:
                max_age = "1"
            image_req_option = TSC.ImageRequestOptions(
                imageresolution=TSC.ImageRequestOptions.Resolution.High, maxage=max_age
            )
            server.views.populate_image(view_item, image_req_option)
            # Save bytes as image
            with open(tabPath, "wb") as image_file:
                image_file.write(view_item.image)
            print("Tableau image successfully saved to {0}".format(tabPath), "\n")

        try:
            # Upload and send customized Slack message
            # Import Slack environment variables
            load_dotenv()  # EXAMPLE VALUES:
            slackBotToken = os.getenv(
                "slackBotToken"
            )  # xoxb-1111111111-111111111-111111111
            slackChannel = os.getenv("slackChannel")  # #random
            # for further explanation of Slack environment variables visit:
            # https://slack.dev/python-slackclient/

            # Preparing date to format filename and caption. Change "Sales Analytics" ect. to whatever you like.
            date = datetime.utcnow().strftime("%Y-%m-%d")
            utc_dt = datetime.now(timezone.utc)
            your_tz = pytz.timezone(
                "US/Pacific"
            )  # Replace with your timezone to localize
            imagetitle = "SalesUpdate_{}".format(
                utc_dt.astimezone(your_tz).strftime("%Y-%m-%d_%I:%M%p_%Z")
            )
            caption = "Sales Update as of {}".format(
                utc_dt.astimezone(your_tz).strftime("%Y-%m-%d %I:%M%p %Z")
            )
            captionA = "Sales Analytics Update"
            captionB = " as of {}".format(
                utc_dt.astimezone(your_tz).strftime("%Y-%m-%d %I:%M%p %Z")
            )
            captionC = "\n\n*" + captionA + "*" + captionB

            # Connect to Slack
            print("Talking to Slack...\n")
            sc = WebClient(slackBotToken)

            # Upload Tableau image to burner channel so that we can securely generate a URL from Tableau image.
            img = sc.files_upload(
                channels="#tableau-test",  # You will need to make this channel or another like it.
                file=tabPath,
                title=imagetitle,
                filetype="png",
            )

            # Store private URL to post in message.
            url_private = img["file"]["url_private"]

            # Construct "builder" and "attachments" json payloads.
            blocksjson = [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": ":level_slider:  Queuing up your Daily Dose of Data  :control_knobs:",
                    },
                },
                {
                    "type": "image",
                    "image_url": "https://i.imgur.com/Eg4TjJq.png",
                    "alt_text": "Nina Kravisualization",
                },
                {
                    "type": "context",
                    "elements": [
                        {
                            "type": "mrkdwn",
                            "text": "Want to see more? <https://www.tableau.com/ Insert Your Link to All Dashboards Here>",
                        }
                    ],
                },
                {"type": "section", "text": {"type": "mrkdwn", "text": captionC}},
            ]

            # Note: the use of "attachments" is a work around and may be deprecated in the future.
            attachmentsjson = [
                {"title": "", "text": "", "image_url": url_private, "alt_text": caption}
            ]

            # Post images with custom icon and username
            msg = sc.chat_postMessage(
                channel=slackChannel,
                icon_url="https://i.imgur.com/WpMvRvn.jpg",
                username="Nina Kravisualization",
                blocks=json.dumps(blocksjson),
                attachments=json.dumps(attachmentsjson),
            )

            # Remove the local image file once it is posted
            fileRemoval = "{0}".format(tabPath)
            os.remove(fileRemoval)
            print("Removing image from local machine.")

        # Out of the box Slack error handling
        except SlackApiError as e:
            assert e.response["ok"] is False
            assert e.response["error"]
            print(f"Got an error: {e.response['error']}")
    # Tableau try statement error handling
    except:
        traceback.print_exc()


Tableau2Slack()
