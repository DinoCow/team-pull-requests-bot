import random
import logging
import json
import requests
import os
from flask import request
from flask_restful import Resource


class WebhooksResource(Resource):

    def __init__(self):
        self.slack_hook_url = os.environ["SLACK_HOOK_URL"]
        self.team_members = map(lambda member: member.lower().strip(),
                                os.environ['TEAM_MEMBERS'].split(','))
        self.slack_channel = os.environ["SLACK_CHANNEL"]

    def post(self):
        try:
            event = json.loads(request.data)
            if self.should_handle_event(event):
                self.slack(event)
        except Exception:
            logging.exception("An error occured handling the webhook")

        return {}

    def should_handle_event(self, event):
        action = event.get('action')
        pull_request = event.get('pull_request', {})
        author = pull_request.get('user', {}).get('login', '')
        valid_actions = [
            "opened", "reopened"
        ]

        if action.lower() not in valid_actions:
            return False

        if not pull_request:
            return False

        if author not in self.team_members:
            return False

        return True

    def slack(self, event):
        pull_request = event.get('pull_request', {})
        title = pull_request.get('title', '')
        author = pull_request.get('user', {}).get('login', '')
        url = pull_request.get('html_url')
        emoji = self.get_emoji()

        response = requests.post(self.slack_hook_url, json={
            "channel": "#%s" % self.slack_channel,
            "text": '%s *A wild PR from @%s appeared!* %s\n_%s_: %s' % (
                emoji, author, emoji, title, url),
            "username": 'Juanbot',
            "icon_emoji": ':juanbot:',
            "link_names": True,
            "unfurl_links": True,
            "mrkdwn": True
        })

        if response.status_code != 200:
            logging.error(response.text)

    def get_emoji(self):
        emojis = [
            ":boom:",
            ":wow:",
            ":star_mario:",
            ":fire:",
            ":hero:",
            ":ctroup:",
            ":1up_mario:",
            ":antonrainbow:",
            ":awesome:",
            ":carlton:",
            ":dancing-penguin:",
            ":fb_levisays:",
            ":leaf:",
            ":love:",
            ":parrot:",
            ":party:",
            ":tada:",
            ":pika_dance:",
            ":shane:",
            ":yay:",
        ]
        return random.choice(emojis)
