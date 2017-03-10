     _____                     ______      _ _  ______                           _        ______       _   
    |_   _|                    | ___ \    | | | | ___ \                         | |       | ___ \     | |  
      | | ___  __ _ _ __ ___   | |_/ /   _| | | | |_/ /___  __ _ _   _  ___  ___| |_ ___  | |_/ / ___ | |_ 
      | |/ _ \/ _` | '_ ` _ \  |  __/ | | | | | |    // _ \/ _` | | | |/ _ \/ __| __/ __| | ___ \/ _ \| __|
      | |  __/ (_| | | | | | | | |  | |_| | | | | |\ \  __/ (_| | |_| |  __/\__ \ |_\__ \ | |_/ / (_) | |_ 
      \_/\___|\__,_|_| |_| |_| \_|   \__,_|_|_| \_| \_\___|\__, |\__,_|\___||___/\__|___/ \____/ \___/ \__|
                                                              | |                                          
                                                              |_|                                          

# What it does
Utilizes the github organization webhook, in order to notify your team mates on slack, whenever a team mate opens up a pull request.

# Running it on Heroku

1. Login to heroku (FreshBooks employees ask IT for heroku access via OKTA)
2. Follow this link [![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)
3. Add a slack [incoming webhook](https://freshbooks.slack.com/services/new/incoming-webhook)
4. Copy the `Webhook URL` into the Heroku config `SLACK_HOOK_URL`
5. Copy the usernames of the people on your team exactly as they appear in Github into the Heroku config `TEAM_MEMBERS` field
separated by commas
6. Enter in the channel you want the bot to slack into the Heroku config `SLACK_CHANNEL` field
7. Click Deploy for Free

Optionally Connect the Application to Github
============================================

1. Requires that you have access to the Github repository (FreshBooks employees as in #dev)
2. From the application Deploy->GitHub page click `Connect to GitHub`
3. Grant the heroku app access to freshbooks/team-pull-requests-bot

# Running it locally

```
  export SLACK_CHANNEL=bunnies'
  export SLACK_HOOK_URL='https://hooks.slack.com/services/T024K32LX/B060UFKPE/SNIP'
  export TEAM_MEMBERS='antonnguyen,markstory'
  gunicorn app:app --log-file=-
```
