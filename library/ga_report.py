"""Google Analytics Reporting API V4."""

import argparse

from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

import httplib2
from oauth2client import client
from oauth2client import file
from oauth2client import tools

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
DISCOVERY_URI = ('https://analyticsreporting.googleapis.com/$discovery/rest')
KEY_FILE_LOCATION = 'aws_key.p12'
SERVICE_ACCOUNT_EMAIL = 'quickstart@erudite-wind-134818.iam.gserviceaccount.com'

def initialize_analyticsreporting():
  """Initializes an analyticsreporting service object.

  Returns:
    analytics an authorized analyticsreporting service object.
  """

  credentials = ServiceAccountCredentials.from_p12_keyfile(
    SERVICE_ACCOUNT_EMAIL, KEY_FILE_LOCATION, scopes=SCOPES)

  http = credentials.authorize(httplib2.Http())

  # Build the service object.
  analytics = build('analytics', 'v4', http=http, discoveryServiceUrl=DISCOVERY_URI)

  return analytics


def get_report(analytics, VIEW_ID = '116151777', time = 'today'):
  # Use the Analytics Service Object to query the Analytics Reporting API V4.
  return analytics.reports().batchGet(
      body={
        'reportRequests': [
        {
          'viewId': VIEW_ID,
          'dateRanges': [{'startDate': time, 'endDate': time}],
          'dimensions':[{"name": "ga:date"},
                        #{"name": "ga:hour"},
                        {"name": "ga:channelGrouping"},
                       ],
          'metrics': [
                      #{"expression": "ga:pageviews"},
                      {"expression": "ga:users"},
                      ]
        }]
      }
  ).execute()


def print_response(response):
  """Parses and prints the Analytics Reporting API V4 response"""
  print (response)
  print(type(response))
  for report in response.get('reports', []):
    columnHeader = report.get('columnHeader', {})
    dimensionHeaders = columnHeader.get('dimensions', [])
    metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
    rows = report.get('data', {}).get('rows', [])

    for row in rows:
      dimensions = row.get('dimensions', [])
      dateRangeValues = row.get('metrics', [])

      for header, dimension in zip(dimensionHeaders, dimensions):
        print (header + ': ' + dimension)

      for i, values in enumerate(dateRangeValues):
        print ('Date range (' + str(i) + ')')
        for metricHeader, value in zip(metricHeaders, values.get('values')):
          print (metricHeader.get('name') + ': ' + value)



def main():

  analytics = initialize_analyticsreporting()
  response = get_report(analytics)
  print_response(response)

if __name__ == '__main__':
  main()
