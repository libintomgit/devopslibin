#!/usr/bin/python
# -*- coding: utf-8 -*-
## This script will collect cost details of from the AWS and sends it to Slack channel

import boto3
import operator
import datetime
from slack import WebClient

client = boto3.client('ce')
slack_client = WebClient(token='xxxx')


start_date = datetime.date.today()
end_date = start_date - datetime.timedelta(days=30)

aws_accounts = ['122','456']




def send_slack_notification(cost_formatted):

    slack_client.chat_postMessage(channel='#aws-notifications',text=cost_formatted,icon_emoji=":money_heist:",username="CostUsageReport")

# def get_daily_cost_by_service():
#     result = \
#         client.get_cost_and_usage(TimePeriod={'Start': str(end_date),
#                                   'End': str(start_date)},
#                                   Granularity='DAILY',
#                                   Filter={'And': [{'Dimensions': {'Key': 'LINKED_ACCOUNT'
#                                   , 'Values': aws_accounts}},
#                                   {'Not': {'Dimensions': {'Key': 'RECORD_TYPE'
#                                   , 'Values': ['Credit', 'Refund'
#                                   ]}}}]}, Metrics=['UNBLENDED_COST'],
#                                   GroupBy=[{'Type': 'DIMENSION',
#                                   'Key': 'SERVICE'}])
#     result['ResultsByTime'].reverse()

#     return result

def get_daily_cost():
    result = \
        client.get_cost_and_usage(TimePeriod={'Start': str(end_date),
                                  'End': str(start_date)},
                                  Granularity='DAILY',
                                  Filter={'And': [{'Dimensions': {'Key': 'LINKED_ACCOUNT'
                                  , 'Values': aws_accounts}},
                                  {'Not': {'Dimensions': {'Key': 'RECORD_TYPE'
                                  , 'Values': ['Credit', 'Refund'
                                  ]}}}]}, 
                                  Metrics=['UNBLENDED_COST'])
    result['ResultsByTime'].reverse()

    return result




def get_top_cost_by_services(top, day, result_service,result_total):
    time_start = result_service['ResultsByTime'][day]['TimePeriod']['Start']
    time_end = result_service['ResultsByTime'][day]['TimePeriod']['End']
    cost = {}

    for group in result_service['ResultsByTime'][day]['Groups']:
        cost[group['Keys'][0]] = float(group['Metrics']['UnblendedCost'
                ]['Amount'])

    sorted_cost = dict(sorted(cost.items(), key=operator.itemgetter(1),
                      reverse=True)[:top])
   
    total_cost = result_total['ResultsByTime'][day]['Total']['UnblendedCost']['Amount']

    slack_out = get_formatted_cost(sorted_cost,total_cost,time_start,time_end,day)
    return slack_out


def get_formatted_cost(sorted_cost,total_cost,time_start,time_end,day):

    title = (f"AWS Cost Usage by Service on {time_start} - Last {day+1} days back  ")

    message = ""

    for (service, cost) in sorted_cost.items():
        message = message + (f"{service} - {cost} \n")

    formanted_message = (f"*{title}* \n\n *Total Cost:* `{total_cost}` ```{message}```")

    slack_result = send_slack_notification(formanted_message)

    return slack_result


def get_cost():
    result_service = get_daily_cost_by_service()
    result_total = get_daily_cost()

    return result_service,result_total


result_service,result_total = get_cost()

get_top_cost_by_services(5, 1, result_service,result_total)
get_top_cost_by_services(5, 6, result_service,result_total)
get_top_cost_by_services(5, 29, result_service,result_total)