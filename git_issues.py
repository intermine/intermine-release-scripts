#!/usr/bin/env python

import requests
import json

issues = {}

response = requests.get('https://api.github.com/repos/intermine/intermine/issues?direction=asc&state=all&milestone=48&per_page=1000')

issues = response.json()
for issue in issues:
	if 'pull_request' not in issue:		
		print("#" + str(issue['number']) + " - " + str(issue['title']))


print("\n --------------------- \n")
                
milestones = {}

response = requests.get('https://api.github.com/repos/intermine/intermine/milestones')

milestones = response.json()
for milestone in milestones:
        print("#" + str(milestone['number']) + " - " + str(milestone['title']))


# https://developer.github.com/v3/issues/

