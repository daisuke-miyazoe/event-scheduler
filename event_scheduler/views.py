import os
from django.shortcuts import render
from datetime import datetime
from zoneinfo import ZoneInfo
from dotenv import load_dotenv
import slackweb
from .models import Event


class EventScraping():
    def import_event(
        self, 
        event_title=None, 
        start_date=None, 
        end_date=None
    ):
        try:
            naive_date = datetime.strptime(start_date, "%Y/%m/%d %H:%M")
            start_date = naive_date.replace(tzinfo=ZoneInfo("Asia/Tokyo"))
        except ValueError:
            print("Invalid date format")
        Event.objects.get_or_create(
            title=event_title,
            start_date=start_date,
            end_date=end_date
        )

        load_dotenv()
        env = os.environ
        slack = slackweb.Slack(url=env['SLACK_WEBHOOK_URL'])
        slack.notify(text=f'タイトル:{ event_title }, 開催日時:{ start_date }')
        return '成功'
    