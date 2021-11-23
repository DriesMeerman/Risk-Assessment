/**
 * 
 * https://github.com/jai2shukla/JIRA-Estimation-Prediction/tree/master/storypoint/IEEE%20TSE2018/dataset
 * File							Rows
 * datamanagement.csv    		4667
 * springxd.csv					3526
 * appceleratorstudio.csv		2919
 * titanium.csv					2251
 * mesos.csv					1680
 * talenddataquality.csv		1381
 * moodle.csv					1166
 * mule.csv						889
 * talendesb.csv				868
 * aptanastudio.csv				829
 * mulestudio.csv				732
 * duracloud.csv				666
 * bamboo.csv					521
 * usergrid.csv					482
 * clover.csv					384
 * jirasoftware.csv				352
 */

const example_response = {
	"expand": "schema,names",
	"startAt": 0,
	"maxResults": 50,
	"total": 31682,
	"issues": [
		{
			"expand": "operations,versionedRepresentations,editmeta,changelog,renderedFields",
			"id": "866362",
			"self": "https://jira.lsstcorp.org/rest/api/2/issue/866362",
			"key": "DM-32540",
			"fields": {
				"customfield_14311": null,
				"customfield_14312": null,
				"customfield_14310": null,
				"resolution": null,
				"customfield_14316": null,
				"customfield_13106": null,
				"customfield_14313": null,
				"customfield_13105": null,
				"customfield_14314": null,
				"customfield_14309": null,
				"customfield_10502": {
					"self": "https://jira.lsstcorp.org/rest/api/2/customFieldOption/12219",
					"value": "Data Facility",
					"id": "12219",
					"disabled": false
				},
				"lastViewed": null,
				"customfield_12000": null,
				"customfield_14301": null,
				"customfield_12002": null,
				"customfield_14304": null,
				"customfield_14305": null,
				"customfield_14302": null,
				"labels": [],
				"customfield_12005": null,
				"customfield_14303": null,
				"customfield_12910": null,
				"aggregatetimeoriginalestimate": null,
				"issuelinks": [],
				"assignee": {
					"self": "https://jira.lsstcorp.org/rest/api/2/user?username=spietrowicz",
					"name": "spietrowicz",
					"key": "spietrowicz",
					"emailAddress": "srp@ncsa.uiuc.edu",
					"avatarUrls": {
						"48x48": "https://jira.lsstcorp.org/secure/useravatar?ownerId=spietrowicz&avatarId=11801",
						"24x24": "https://jira.lsstcorp.org/secure/useravatar?size=small&ownerId=spietrowicz&avatarId=11801",
						"16x16": "https://jira.lsstcorp.org/secure/useravatar?size=xsmall&ownerId=spietrowicz&avatarId=11801",
						"32x32": "https://jira.lsstcorp.org/secure/useravatar?size=medium&ownerId=spietrowicz&avatarId=11801"
					},
					"displayName": "Steve Pietrowicz",
					"active": true,
					"timeZone": "America/Chicago"
				},
				"components": [],
				"customfield_15503": null,
				"customfield_10600": "2|i03i5j:",
				"customfield_12901": null,
				"customfield_12900": null,
				"customfield_12902": null,
				"customfield_12905": null,
				"customfield_12904": null,
				"customfield_12907": null,
				"customfield_12906": null,
				"customfield_12909": null,
				"customfield_12908": null,
				"subtasks": [],
				"customfield_14400": null,
				"reporter": {
					"self": "https://jira.lsstcorp.org/rest/api/2/user?username=spietrowicz",
					"name": "spietrowicz",
					"key": "spietrowicz",
					"emailAddress": "srp@ncsa.uiuc.edu",
					"avatarUrls": {
						"48x48": "https://jira.lsstcorp.org/secure/useravatar?ownerId=spietrowicz&avatarId=11801",
						"24x24": "https://jira.lsstcorp.org/secure/useravatar?size=small&ownerId=spietrowicz&avatarId=11801",
						"16x16": "https://jira.lsstcorp.org/secure/useravatar?size=xsmall&ownerId=spietrowicz&avatarId=11801",
						"32x32": "https://jira.lsstcorp.org/secure/useravatar?size=medium&ownerId=spietrowicz&avatarId=11801"
					},
					"displayName": "Steve Pietrowicz",
					"active": true,
					"timeZone": "America/Chicago"
				},
				"customfield_16702": null,
				"customfield_16701": null,
				"customfield_16700": null,
				"progress": {
					"progress": 0,
					"total": 0
				},
				"votes": {
					"self": "https://jira.lsstcorp.org/rest/api/2/issue/DM-32540/votes",
					"votes": 0,
					"hasVoted": false
				},
				"issuetype": {
					"self": "https://jira.lsstcorp.org/rest/api/2/issuetype/10001",
					"id": "10001",
					"description": "Created by Jira Software - do not edit or delete. Issue type for a user story.",
					"iconUrl": "https://jira.lsstcorp.org/secure/viewavatar?size=xsmall&avatarId=11315&avatarType=issuetype",
					"name": "Story",
					"subtask": false,
					"avatarId": 11315
				},
				"project": {
					"self": "https://jira.lsstcorp.org/rest/api/2/project/10501",
					"id": "10501",
					"key": "DM",
					"name": "Data Management",
					"projectTypeKey": "software",
					"avatarUrls": {
						"48x48": "https://jira.lsstcorp.org/secure/projectavatar?pid=10501&avatarId=10011",
						"24x24": "https://jira.lsstcorp.org/secure/projectavatar?size=small&pid=10501&avatarId=10011",
						"16x16": "https://jira.lsstcorp.org/secure/projectavatar?size=xsmall&pid=10501&avatarId=10011",
						"32x32": "https://jira.lsstcorp.org/secure/projectavatar?size=medium&pid=10501&avatarId=10011"
					},
					"projectCategory": {
						"self": "https://jira.lsstcorp.org/rest/api/2/projectCategory/10001",
						"id": "10001",
						"description": "Projects being actively worked.  These projects have live issues.",
						"name": "Active Projects"
					}
				},
				"customfield_13300": "{summaryBean=com.atlassian.jira.plugin.devstatus.rest.SummaryBean@285fb955[summary={pullrequest=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@5cbfda0[overall=PullRequestOverallBean{stateCount=0, state='OPEN', details=PullRequestOverallDetails{openCount=0, mergedCount=0, declinedCount=0}},byInstanceType={}], build=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@406b751d[overall=com.atlassian.jira.plugin.devstatus.summary.beans.BuildOverallBean@1a97b64d[failedBuildCount=0,successfulBuildCount=0,unknownBuildCount=0,count=0,lastUpdated=<null>,lastUpdatedTimestamp=<null>],byInstanceType={}], review=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@39126ff9[overall=com.atlassian.jira.plugin.devstatus.summary.beans.ReviewsOverallBean@73ecdf34[stateCount=0,state=<null>,dueDate=<null>,overDue=false,count=0,lastUpdated=<null>,lastUpdatedTimestamp=<null>],byInstanceType={}], deployment-environment=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@68b49fc9[overall=com.atlassian.jira.plugin.devstatus.summary.beans.DeploymentOverallBean@4f36694c[topEnvironments=[],showProjects=false,successfulCount=0,count=0,lastUpdated=<null>,lastUpdatedTimestamp=<null>],byInstanceType={}], repository=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@6571baf4[overall=com.atlassian.jira.plugin.devstatus.summary.beans.CommitOverallBean@70f1cc11[count=0,lastUpdated=<null>,lastUpdatedTimestamp=<null>],byInstanceType={}], branch=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@3c775f11[overall=com.atlassian.jira.plugin.devstatus.summary.beans.BranchOverallBean@40773dda[count=0,lastUpdated=<null>,lastUpdatedTimestamp=<null>],byInstanceType={}]},errors=[],configErrors=[]], devSummaryJson={\"cachedValue\":{\"errors\":[],\"configErrors\":[],\"summary\":{\"pullrequest\":{\"overall\":{\"count\":0,\"lastUpdated\":null,\"stateCount\":0,\"state\":\"OPEN\",\"details\":{\"openCount\":0,\"mergedCount\":0,\"declinedCount\":0,\"total\":0},\"open\":true},\"byInstanceType\":{}},\"build\":{\"overall\":{\"count\":0,\"lastUpdated\":null,\"failedBuildCount\":0,\"successfulBuildCount\":0,\"unknownBuildCount\":0},\"byInstanceType\":{}},\"review\":{\"overall\":{\"count\":0,\"lastUpdated\":null,\"stateCount\":0,\"state\":null,\"dueDate\":null,\"overDue\":false,\"completed\":false},\"byInstanceType\":{}},\"deployment-environment\":{\"overall\":{\"count\":0,\"lastUpdated\":null,\"topEnvironments\":[],\"showProjects\":false,\"successfulCount\":0},\"byInstanceType\":{}},\"repository\":{\"overall\":{\"count\":0,\"lastUpdated\":null},\"byInstanceType\":{}},\"branch\":{\"overall\":{\"count\":0,\"lastUpdated\":null},\"byInstanceType\":{}}}},\"isStale\":true}}",
				"customfield_15602": "off",
				"customfield_15600": null,
				"customfield_15601": null,
				"customfield_12206": null,
				"customfield_12205": null,
				"customfield_10700": null,
				"customfield_12208": null,
				"customfield_12207": null,
				"customfield_10702": null,
				"customfield_10703": null,
				"customfield_12209": null,
				"resolutiondate": null,
				"watches": {
					"self": "https://jira.lsstcorp.org/rest/api/2/issue/DM-32540/watchers",
					"watchCount": 1,
					"isWatching": false
				},
				"customfield_16002": null,
				"customfield_16001": null,
				"customfield_16000": null,
				"customfield_12202": null,
				"customfield_12204": null,
				"customfield_14500": null,
				"customfield_12203": null,
				"customfield_11900": null,
				"updated": "2021-11-10T15:11:02.000+0000",
				"timeoriginalestimate": null,
				"description": "Update the Archiver CSCs to use packages used in Cycle 23\r\n\r\n \r\n\r\nhttps://confluence.lsstcorp.org/display/LSSTCOM/Cycle+23+Upgrade",
				"customfield_11101": null,
				"customfield_14605": null,
				"customfield_12304": null,
				"customfield_14724": null,
				"customfield_14603": [],
				"customfield_14725": null,
				"customfield_14604": null,
				"customfield_10800": null,
				"customfield_13519": null,
				"customfield_13518": null,
				"summary": "Update Archiver CSCs to Cycle 23",
				"customfield_14722": null,
				"customfield_14723": null,
				"customfield_14602": null,
				"customfield_14720": null,
				"customfield_14721": null,
				"customfield_14715": null,
				"customfield_14716": null,
				"customfield_14713": null,
				"customfield_14714": null,
				"customfield_14719": null,
				"duedate": null,
				"customfield_14717": null,
				"customfield_14718": null,
				"customfield_15000": null,
				"customfield_15001": null,
				"customfield_15004": null,
				"customfield_15005": null,
				"customfield_10230": null,
				"customfield_15002": null,
				"fixVersions": [],
				"customfield_15003": null,
				"customfield_14711": null,
				"customfield_11200": [],
				"customfield_15008": null,
				"customfield_14712": null,
				"customfield_15006": null,
				"customfield_14710": null,
				"customfield_15007": null,
				"customfield_10225": null,
				"customfield_14704": null,
				"customfield_10226": null,
				"customfield_14705": null,
				"customfield_10227": null,
				"customfield_14703": null,
				"customfield_10229": null,
				"customfield_14708": null,
				"customfield_14709": null,
				"customfield_14706": null,
				"customfield_14707": null,
				"customfield_16200": "2021-11-10",
				"customfield_10220": null,
				"customfield_16201": null,
				"customfield_10221": null,
				"customfield_12400": null,
				"customfield_10222": null,
				"customfield_10101": [
					{
						"self": "https://jira.lsstcorp.org/rest/api/2/user?username=spietrowicz",
						"name": "spietrowicz",
						"key": "spietrowicz",
						"emailAddress": "srp@ncsa.uiuc.edu",
						"avatarUrls": {
							"48x48": "https://jira.lsstcorp.org/secure/useravatar?ownerId=spietrowicz&avatarId=11801",
							"24x24": "https://jira.lsstcorp.org/secure/useravatar?size=small&ownerId=spietrowicz&avatarId=11801",
							"16x16": "https://jira.lsstcorp.org/secure/useravatar?size=xsmall&ownerId=spietrowicz&avatarId=11801",
							"32x32": "https://jira.lsstcorp.org/secure/useravatar?size=medium&ownerId=spietrowicz&avatarId=11801"
						},
						"displayName": "Steve Pietrowicz",
						"active": true,
						"timeZone": "America/Chicago"
					}
				],
				"customfield_10223": null,
				"customfield_10224": null,
				"customfield_11303": null,
				"customfield_15903": null,
				"customfield_11304": null,
				"customfield_11305": null,
				"customfield_14812": null,
				"customfield_15901": null,
				"customfield_15109": null,
				"customfield_11306": null,
				"customfield_15902": null,
				"customfield_11307": null,
				"timeestimate": null,
				"status": {
					"self": "https://jira.lsstcorp.org/rest/api/2/status/3",
					"description": "",
					"iconUrl": "https://jira.lsstcorp.org/images/icons/statuses/inprogress.png",
					"name": "In Progress",
					"id": "3",
					"statusCategory": {
						"self": "https://jira.lsstcorp.org/rest/api/2/statuscategory/4",
						"id": 4,
						"key": "indeterminate",
						"colorName": "yellow",
						"name": "In Progress"
					}
				},
				"customfield_15100": null,
				"customfield_15104": null,
				"customfield_15101": null,
				"customfield_15102": null,
				"customfield_11300": null,
				"customfield_14811": null,
				"customfield_15900": null,
				"customfield_15108": null,
				"customfield_11301": null,
				"customfield_10203": null,
				"customfield_10204": "9223372036854775807",
				"customfield_10205": null,
				"customfield_10206": "DM-24079",
				"aggregatetimeestimate": null,
				"creator": {
					"self": "https://jira.lsstcorp.org/rest/api/2/user?username=spietrowicz",
					"name": "spietrowicz",
					"key": "spietrowicz",
					"emailAddress": "srp@ncsa.uiuc.edu",
					"avatarUrls": {
						"48x48": "https://jira.lsstcorp.org/secure/useravatar?ownerId=spietrowicz&avatarId=11801",
						"24x24": "https://jira.lsstcorp.org/secure/useravatar?size=small&ownerId=spietrowicz&avatarId=11801",
						"16x16": "https://jira.lsstcorp.org/secure/useravatar?size=xsmall&ownerId=spietrowicz&avatarId=11801",
						"32x32": "https://jira.lsstcorp.org/secure/useravatar?size=medium&ownerId=spietrowicz&avatarId=11801"
					},
					"displayName": "Steve Pietrowicz",
					"active": true,
					"timeZone": "America/Chicago"
				},
				"customfield_16303": null,
				"aggregateprogress": {
					"progress": 0,
					"total": 0
				},
				"customfield_14800": null,
				"customfield_10201": null,
				"customfield_10202": null,
				"customfield_15320": null,
				"timespent": null,
				"customfield_15202": null,
				"customfield_15203": null,
				"customfield_15201": null,
				"customfield_15206": null,
				"aggregatetimespent": null,
				"customfield_11401": null,
				"customfield_13700": null,
				"customfield_15204": null,
				"customfield_11400": null,
				"customfield_15205": null,
				"customfield_15318": null,
				"customfield_15319": null,
				"workratio": -1,
				"created": "2021-11-10T14:59:29.000+0000",
				"customfield_15312": null,
				"customfield_15310": null,
				"customfield_16400": null,
				"customfield_15311": null,
				"customfield_15316": null,
				"customfield_10300": null,
				"customfield_15314": null,
				"customfield_15315": null,
				"customfield_15308": null,
				"customfield_15301": null,
				"customfield_15302": null,
				"customfield_15305": null,
				"customfield_15306": null,
				"customfield_15303": null,
				"customfield_15304": null,
				"customfield_13114": null,
				"customfield_11601": null,
				"customfield_14319": null,
				"customfield_11600": null,
				"customfield_14317": null,
				"customfield_14318": null
			}
		},
		{
			"expand": "operations,versionedRepresentations,editmeta,changelog,renderedFields",
			"id": "864125",
			"self": "https://jira.lsstcorp.org/rest/api/2/issue/864125",
			"key": "DM-32537",
			"fields": {
				"customfield_14311": null,
				"customfield_14312": null,
				"customfield_14310": null,
				"resolution": null,
				"customfield_14316": null,
				"customfield_13106": null,
				"customfield_14313": null,
				"customfield_13105": null,
				"customfield_14314": null,
				"customfield_14309": null,
				"customfield_10502": {
					"self": "https://jira.lsstcorp.org/rest/api/2/customFieldOption/10300",
					"value": "Alert Production",
					"id": "10300",
					"disabled": false
				},
				"lastViewed": null,
				"customfield_12000": null,
				"customfield_14301": null,
				"customfield_12002": null,
				"customfield_14304": null,
				"customfield_14305": null,
				"customfield_14302": null,
				"labels": [],
				"customfield_12005": null,
				"customfield_14303": null,
				"customfield_12910": null,
				"aggregatetimeoriginalestimate": null,
				"issuelinks": [
					{
						"id": "105900",
						"self": "https://jira.lsstcorp.org/rest/api/2/issueLink/105900",
						"type": {
							"id": "10003",
							"name": "Relates",
							"inward": "relates to",
							"outward": "relates to",
							"self": "https://jira.lsstcorp.org/rest/api/2/issueLinkType/10003"
						},
						"inwardIssue": {
							"id": "822927",
							"key": "DM-32356",
							"self": "https://jira.lsstcorp.org/rest/api/2/issue/822927",
							"fields": {
								"summary": "Write a phalanx service that defines a Kafka service and users",
								"status": {
									"self": "https://jira.lsstcorp.org/rest/api/2/status/10002",
									"description": "",
									"iconUrl": "https://jira.lsstcorp.org/images/icons/subtask.gif",
									"name": "Done",
									"id": "10002",
									"statusCategory": {
										"self": "https://jira.lsstcorp.org/rest/api/2/statuscategory/3",
										"id": 3,
										"key": "done",
										"colorName": "green",
										"name": "Done"
									}
								},
								"issuetype": {
									"self": "https://jira.lsstcorp.org/rest/api/2/issuetype/10001",
									"id": "10001",
									"description": "Created by Jira Software - do not edit or delete. Issue type for a user story.",
									"iconUrl": "https://jira.lsstcorp.org/secure/viewavatar?size=xsmall&avatarId=11315&avatarType=issuetype",
									"name": "Story",
									"subtask": false,
									"avatarId": 11315
								}
							}
						}
					}
				],
				"assignee": {
					"self": "https://jira.lsstcorp.org/rest/api/2/user?username=swnelson",
					"name": "swnelson",
					"key": "swnelson",
					"emailAddress": "swnelson@uw.edu",
					"avatarUrls": {
						"48x48": "https://jira.lsstcorp.org/secure/useravatar?ownerId=swnelson&avatarId=16100",
						"24x24": "https://jira.lsstcorp.org/secure/useravatar?size=small&ownerId=swnelson&avatarId=16100",
						"16x16": "https://jira.lsstcorp.org/secure/useravatar?size=xsmall&ownerId=swnelson&avatarId=16100",
						"32x32": "https://jira.lsstcorp.org/secure/useravatar?size=medium&ownerId=swnelson&avatarId=16100"
					},
					"displayName": "Spencer Nelson",
					"active": true,
					"timeZone": "UTC"
				},
				"components": [],
				"customfield_15503": null,
				"customfield_10600": "2|i03hvb:",
				"customfield_12901": null,
				"customfield_12900": null,
				"customfield_12902": null,
				"customfield_12905": null,
				"customfield_12904": null,
				"customfield_12907": null,
				"customfield_12906": null,
				"customfield_12909": null,
				"customfield_12908": null,
				"subtasks": [],
				"customfield_14400": null,
				"reporter": {
					"self": "https://jira.lsstcorp.org/rest/api/2/user?username=swnelson",
					"name": "swnelson",
					"key": "swnelson",
					"emailAddress": "swnelson@uw.edu",
					"avatarUrls": {
						"48x48": "https://jira.lsstcorp.org/secure/useravatar?ownerId=swnelson&avatarId=16100",
						"24x24": "https://jira.lsstcorp.org/secure/useravatar?size=small&ownerId=swnelson&avatarId=16100",
						"16x16": "https://jira.lsstcorp.org/secure/useravatar?size=xsmall&ownerId=swnelson&avatarId=16100",
						"32x32": "https://jira.lsstcorp.org/secure/useravatar?size=medium&ownerId=swnelson&avatarId=16100"
					},
					"displayName": "Spencer Nelson",
					"active": true,
					"timeZone": "UTC"
				},
				"customfield_16702": null,
				"customfield_16701": null,
				"customfield_16700": null,
				"progress": {
					"progress": 0,
					"total": 0
				},
				"votes": {
					"self": "https://jira.lsstcorp.org/rest/api/2/issue/DM-32537/votes",
					"votes": 0,
					"hasVoted": false
				},
				"issuetype": {
					"self": "https://jira.lsstcorp.org/rest/api/2/issuetype/10001",
					"id": "10001",
					"description": "Created by Jira Software - do not edit or delete. Issue type for a user story.",
					"iconUrl": "https://jira.lsstcorp.org/secure/viewavatar?size=xsmall&avatarId=11315&avatarType=issuetype",
					"name": "Story",
					"subtask": false,
					"avatarId": 11315
				},
				"project": {
					"self": "https://jira.lsstcorp.org/rest/api/2/project/10501",
					"id": "10501",
					"key": "DM",
					"name": "Data Management",
					"projectTypeKey": "software",
					"avatarUrls": {
						"48x48": "https://jira.lsstcorp.org/secure/projectavatar?pid=10501&avatarId=10011",
						"24x24": "https://jira.lsstcorp.org/secure/projectavatar?size=small&pid=10501&avatarId=10011",
						"16x16": "https://jira.lsstcorp.org/secure/projectavatar?size=xsmall&pid=10501&avatarId=10011",
						"32x32": "https://jira.lsstcorp.org/secure/projectavatar?size=medium&pid=10501&avatarId=10011"
					},
					"projectCategory": {
						"self": "https://jira.lsstcorp.org/rest/api/2/projectCategory/10001",
						"id": "10001",
						"description": "Projects being actively worked.  These projects have live issues.",
						"name": "Active Projects"
					}
				},
				"customfield_13300": "{summaryBean=com.atlassian.jira.plugin.devstatus.rest.SummaryBean@411ce649[summary={pullrequest=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@510053fe[overall=PullRequestOverallBean{stateCount=0, state='OPEN', details=PullRequestOverallDetails{openCount=0, mergedCount=0, declinedCount=0}},byInstanceType={}], build=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@41ae9eff[overall=com.atlassian.jira.plugin.devstatus.summary.beans.BuildOverallBean@1262aa97[failedBuildCount=0,successfulBuildCount=0,unknownBuildCount=0,count=0,lastUpdated=<null>,lastUpdatedTimestamp=<null>],byInstanceType={}], review=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@38cf72f2[overall=com.atlassian.jira.plugin.devstatus.summary.beans.ReviewsOverallBean@6fa93675[stateCount=0,state=<null>,dueDate=<null>,overDue=false,count=0,lastUpdated=<null>,lastUpdatedTimestamp=<null>],byInstanceType={}], deployment-environment=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@5ac50419[overall=com.atlassian.jira.plugin.devstatus.summary.beans.DeploymentOverallBean@5df42bc4[topEnvironments=[],showProjects=false,successfulCount=0,count=0,lastUpdated=<null>,lastUpdatedTimestamp=<null>],byInstanceType={}], repository=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@1eef9a6a[overall=com.atlassian.jira.plugin.devstatus.summary.beans.CommitOverallBean@38d31d5c[count=0,lastUpdated=<null>,lastUpdatedTimestamp=<null>],byInstanceType={}], branch=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@4a443393[overall=com.atlassian.jira.plugin.devstatus.summary.beans.BranchOverallBean@36129b14[count=0,lastUpdated=<null>,lastUpdatedTimestamp=<null>],byInstanceType={}]},errors=[],configErrors=[]], devSummaryJson={\"cachedValue\":{\"errors\":[],\"configErrors\":[],\"summary\":{\"pullrequest\":{\"overall\":{\"count\":0,\"lastUpdated\":null,\"stateCount\":0,\"state\":\"OPEN\",\"details\":{\"openCount\":0,\"mergedCount\":0,\"declinedCount\":0,\"total\":0},\"open\":true},\"byInstanceType\":{}},\"build\":{\"overall\":{\"count\":0,\"lastUpdated\":null,\"failedBuildCount\":0,\"successfulBuildCount\":0,\"unknownBuildCount\":0},\"byInstanceType\":{}},\"review\":{\"overall\":{\"count\":0,\"lastUpdated\":null,\"stateCount\":0,\"state\":null,\"dueDate\":null,\"overDue\":false,\"completed\":false},\"byInstanceType\":{}},\"deployment-environment\":{\"overall\":{\"count\":0,\"lastUpdated\":null,\"topEnvironments\":[],\"showProjects\":false,\"successfulCount\":0},\"byInstanceType\":{}},\"repository\":{\"overall\":{\"count\":0,\"lastUpdated\":null},\"byInstanceType\":{}},\"branch\":{\"overall\":{\"count\":0,\"lastUpdated\":null},\"byInstanceType\":{}}}},\"isStale\":true}}",
				"customfield_15602": "off",
				"customfield_15600": null,
				"customfield_15601": null,
				"customfield_12206": null,
				"customfield_12205": null,
				"customfield_10700": null,
				"customfield_12208": null,
				"customfield_12207": null,
				"customfield_10702": null,
				"customfield_10703": null,
				"customfield_12209": null,
				"resolutiondate": null,
				"watches": {
					"self": "https://jira.lsstcorp.org/rest/api/2/issue/DM-32537/watchers",
					"watchCount": 3,
					"isWatching": false
				},
				"customfield_16002": null,
				"customfield_16001": null,
				"customfield_16000": null,
				"customfield_12202": null,
				"customfield_12204": null,
				"customfield_14500": null,
				"customfield_12203": null,
				"customfield_11900": null,
				"updated": "2021-11-09T21:17:27.000+0000",
				"timeoriginalestimate": null,
				"description": "The INT environment of the Rubin Science Platform's Kubernetes cluster takes a long time to create Services, even simple ones that are just a ClusterIP. As a result, the Strimzi Cluster Operator times out during initialization of a broker.\r\n\r\nThis has been papered over by modifying the Cluster Operator deployment's environment variables passed into its container, but that solution is not durable; if Strimzi is redeployed, the change will be lost. It would also not appear in any new environments.\r\n\r\nThe proper fix is to configure our Strimzi Cluster Operator with a higher timeout through the {{values.yaml}} file in Phalanx for the {{strimzi}} application. But version 0.26.0 of Strimzi (the current latest) does not support that; we need to wait for version 0.27.0 which will add support for configuring the timeout (via https://github.com/strimzi/strimzi-kafka-operator/pull/5859).",
				"customfield_11101": null,
				"customfield_14605": null,
				"customfield_12304": null,
				"customfield_14724": null,
				"customfield_14603": [],
				"customfield_14725": null,
				"customfield_14604": null,
				"customfield_10800": null,
				"customfield_13519": null,
				"customfield_13518": null,
				"summary": "Configure Strimzi with higher Kubernetes client timeout",
				"customfield_14722": null,
				"customfield_14723": null,
				"customfield_14602": null,
				"customfield_14720": null,
				"customfield_14721": null,
				"customfield_14715": null,
				"customfield_14716": null,
				"customfield_14713": null,
				"customfield_14714": null,
				"customfield_14719": null,
				"duedate": null,
				"customfield_14717": null,
				"customfield_14718": null,
				"customfield_15000": null,
				"customfield_15001": null,
				"customfield_15004": null,
				"customfield_15005": null,
				"customfield_10230": null,
				"customfield_15002": null,
				"fixVersions": [],
				"customfield_15003": null,
				"customfield_14711": null,
				"customfield_11200": [],
				"customfield_15008": null,
				"customfield_14712": null,
				"customfield_15006": null,
				"customfield_14710": null,
				"customfield_15007": null,
				"customfield_10225": null,
				"customfield_14704": null,
				"customfield_10226": null,
				"customfield_14705": null,
				"customfield_10227": null,
				"customfield_14703": null,
				"customfield_10229": null,
				"customfield_14708": null,
				"customfield_14709": null,
				"customfield_14706": null,
				"customfield_14707": null,
				"customfield_16200": "2021-11-09",
				"customfield_10220": null,
				"customfield_16201": null,
				"customfield_10221": null,
				"customfield_12400": null,
				"customfield_10222": null,
				"customfield_10101": [
					{
						"self": "https://jira.lsstcorp.org/rest/api/2/user?username=ebellm",
						"name": "ebellm",
						"key": "ebellm",
						"emailAddress": "ecbellm@uw.edu",
						"avatarUrls": {
							"48x48": "https://jira.lsstcorp.org/secure/useravatar?ownerId=ebellm&avatarId=13000",
							"24x24": "https://jira.lsstcorp.org/secure/useravatar?size=small&ownerId=ebellm&avatarId=13000",
							"16x16": "https://jira.lsstcorp.org/secure/useravatar?size=xsmall&ownerId=ebellm&avatarId=13000",
							"32x32": "https://jira.lsstcorp.org/secure/useravatar?size=medium&ownerId=ebellm&avatarId=13000"
						},
						"displayName": "Eric Bellm",
						"active": true,
						"timeZone": "America/Los_Angeles"
					},
					{
						"self": "https://jira.lsstcorp.org/rest/api/2/user?username=sullivan",
						"name": "sullivan",
						"key": "sullivan",
						"emailAddress": "sullii@uw.edu",
						"avatarUrls": {
							"48x48": "https://jira.lsstcorp.org/secure/useravatar?ownerId=sullivan&avatarId=16804",
							"24x24": "https://jira.lsstcorp.org/secure/useravatar?size=small&ownerId=sullivan&avatarId=16804",
							"16x16": "https://jira.lsstcorp.org/secure/useravatar?size=xsmall&ownerId=sullivan&avatarId=16804",
							"32x32": "https://jira.lsstcorp.org/secure/useravatar?size=medium&ownerId=sullivan&avatarId=16804"
						},
						"displayName": "Ian Sullivan",
						"active": true,
						"timeZone": "America/Los_Angeles"
					},
					{
						"self": "https://jira.lsstcorp.org/rest/api/2/user?username=swnelson",
						"name": "swnelson",
						"key": "swnelson",
						"emailAddress": "swnelson@uw.edu",
						"avatarUrls": {
							"48x48": "https://jira.lsstcorp.org/secure/useravatar?ownerId=swnelson&avatarId=16100",
							"24x24": "https://jira.lsstcorp.org/secure/useravatar?size=small&ownerId=swnelson&avatarId=16100",
							"16x16": "https://jira.lsstcorp.org/secure/useravatar?size=xsmall&ownerId=swnelson&avatarId=16100",
							"32x32": "https://jira.lsstcorp.org/secure/useravatar?size=medium&ownerId=swnelson&avatarId=16100"
						},
						"displayName": "Spencer Nelson",
						"active": true,
						"timeZone": "UTC"
					}
				],
				"customfield_10223": null,
				"customfield_10224": null,
				"customfield_11303": null,
				"customfield_15903": null,
				"customfield_11304": null,
				"customfield_11305": null,
				"customfield_14812": null,
				"customfield_15901": null,
				"customfield_15109": null,
				"customfield_11306": null,
				"customfield_15902": null,
				"customfield_11307": null,
				"timeestimate": null,
				"status": {
					"self": "https://jira.lsstcorp.org/rest/api/2/status/10001",
					"description": "",
					"iconUrl": "https://jira.lsstcorp.org/images/icons/subtask.gif",
					"name": "To Do",
					"id": "10001",
					"statusCategory": {
						"self": "https://jira.lsstcorp.org/rest/api/2/statuscategory/2",
						"id": 2,
						"key": "new",
						"colorName": "blue-gray",
						"name": "To Do"
					}
				},
				"customfield_15100": null,
				"customfield_15104": null,
				"customfield_15101": null,
				"customfield_15102": null,
				"customfield_11300": null,
				"customfield_14811": null,
				"customfield_15900": null,
				"customfield_15108": null,
				"customfield_11301": null,
				"customfield_10203": null,
				"customfield_10204": "9223372036854775807",
				"customfield_10205": null,
				"customfield_10206": "DM-30508",
				"aggregatetimeestimate": null,
				"creator": {
					"self": "https://jira.lsstcorp.org/rest/api/2/user?username=swnelson",
					"name": "swnelson",
					"key": "swnelson",
					"emailAddress": "swnelson@uw.edu",
					"avatarUrls": {
						"48x48": "https://jira.lsstcorp.org/secure/useravatar?ownerId=swnelson&avatarId=16100",
						"24x24": "https://jira.lsstcorp.org/secure/useravatar?size=small&ownerId=swnelson&avatarId=16100",
						"16x16": "https://jira.lsstcorp.org/secure/useravatar?size=xsmall&ownerId=swnelson&avatarId=16100",
						"32x32": "https://jira.lsstcorp.org/secure/useravatar?size=medium&ownerId=swnelson&avatarId=16100"
					},
					"displayName": "Spencer Nelson",
					"active": true,
					"timeZone": "UTC"
				},
				"customfield_16303": null,
				"aggregateprogress": {
					"progress": 0,
					"total": 0
				},
				"customfield_14800": null,
				"customfield_10201": null,
				"customfield_10202": 1.0,
				"customfield_15320": null,
				"timespent": null,
				"customfield_15202": null,
				"customfield_15203": null,
				"customfield_15201": null,
				"customfield_15206": null,
				"aggregatetimespent": null,
				"customfield_11401": null,
				"customfield_13700": null,
				"customfield_15204": null,
				"customfield_11400": null,
				"customfield_15205": null,
				"customfield_15318": null,
				"customfield_15319": null,
				"workratio": -1,
				"created": "2021-11-09T21:17:27.000+0000",
				"customfield_15312": null,
				"customfield_15310": null,
				"customfield_16400": null,
				"customfield_15311": null,
				"customfield_15316": null,
				"customfield_10300": null,
				"customfield_15314": null,
				"customfield_15315": null,
				"customfield_15308": null,
				"customfield_15301": null,
				"customfield_15302": null,
				"customfield_15305": null,
				"customfield_15306": null,
				"customfield_15303": null,
				"customfield_15304": null,
				"customfield_13114": null,
				"customfield_11601": null,
				"customfield_14319": null,
				"customfield_11600": null,
				"customfield_14317": null,
				"customfield_14318": null
			}
		}
	]
};


const fs = require('fs');
const axios = require('axios');
const ObjectsToCsv = require('objects-to-csv'); // https://github.com/anton-bot/objects-to-csv

// Retrieved using 'getJiraFieldNames' function
const lsstFieldMap = {
	customfield_14311: 'Analysis Performed By',
	customfield_14312: 'Analysis Date',
	customfield_14310: 'Root Cause',
	resolution: 'Resolution',
	customfield_14316: 'Effectiveness of Corrective Action',
	customfield_13106: 'Deviation Type',
	customfield_14313: 'FMEA Reference',
	customfield_13105: 'NSF/DOE Review Required?',
	customfield_14314: 'Recommended Corrective Action',
	customfield_14309: 'End Effect',
	customfield_10502: 'Team',
	lastViewed: 'Last Viewed',
	customfield_12000: 'Explain your urgency',
	customfield_14301: 'Supplier Name',
	customfield_12002: 'Verification Method',
	customfield_14304: 'Description of Trouble (First Symptoms)',
	customfield_14305: 'Failure Detection/Isolation Effectiveness',
	customfield_14302: 'Part Number(s)',
	labels: 'Labels',
	customfield_12005: 'Early',
	customfield_14303: 'Incident Classification',
	customfield_12910: 'Severity (Final)',
	aggregatetimeoriginalestimate: 'Σ Original Estimate',
	issuelinks: 'Linked Issues',
	assignee: 'Assignee',
	components: 'Component/s',
	customfield_15503: 'Priority ID',
	customfield_10600: 'Rank',
	customfield_12901: 'Hazardous Situation',
	customfield_12900: 'activity_id',
	customfield_12902: 'Hazard',
	customfield_12905: 'Probability (Final)',
	customfield_12904: 'Verification',
	customfield_12907: 'Cause',
	customfield_12906: 'Severity',
	customfield_12909: 'Harm',
	customfield_12908: 'Probability',
	subtasks: 'Sub-Tasks',
	customfield_14400: 'Reason for Cancellation',
	reporter: 'Reporter',
	customfield_16702: 'Time lost (hr)',
	customfield_16701: 'Risk Likelihood',
	customfield_16700: 'Risk Impact',
	progress: 'Progress',
	votes: 'Votes',
	issuetype: 'Issue Type',
	project: 'Project',
	customfield_13300: 'Development',
	customfield_15602: 'Urgent?',
	customfield_15600: 'Cause or Failure Mode',
	customfield_15601: 'Hazard Mitigation',
	customfield_12206: 'Verification Level',
	customfield_12205: 'Refining Parameters',
	customfield_10700: 'Units',
	customfield_12208: 'DM Priority',
	customfield_12207: 'Verification Phase',
	customfield_10702: 'DueTime',
	customfield_10703: 'Location',
	customfield_12209: 'T&S Verification Phase',
	resolutiondate: 'Resolved',
	watches: 'Watchers',
	customfield_16002: 'POP Deliverable',
	customfield_16001: 'POP Milestone',
	customfield_16000: 'RO Milestone ID',
	customfield_12202: 'Discussion',
	customfield_12204: 'Success Criteria',
	customfield_14500: 'Task Dependencies',
	customfield_12203: 'Verification Requirement',
	customfield_11900: 'ICD?',
	updated: 'Updated',
	timeoriginalestimate: 'Original Estimate',
	description: 'Description',
	customfield_11101: 'PercentDone',
	customfield_14605: 'Verifies',
	customfield_12304: 'Owner',
	customfield_14724: 'Facilities Required',
	customfield_14603: 'Impacted Verification Issues',
	customfield_14725: 'Meal(s) Requested',
	customfield_14604: 'Verified By',
	customfield_10800: 'issueFunction',
	customfield_13519: 'Impacted Document Links',
	customfield_13518: 'Impacted System',
	summary: 'Summary',
	customfield_14722: 'Activity Plan',
	customfield_14723: 'Activity Report',
	customfield_14602: 'Deviation Requests',
	customfield_14720: 'Car Required',
	customfield_14721: 'Taxi Required',
	customfield_14715: 'Check-In',
	customfield_14716: 'Check-Out',
	customfield_14713: 'TR No.',
	customfield_14714: 'Lodging',
	customfield_14719: 'Office Required',
	duedate: 'Due Date',
	customfield_14717: 'Require Minibus Transportation',
	customfield_14718: 'Meeting Room Required',
	customfield_15000: 'Sub-Component(s)',
	customfield_15001: 'Sub-Component',
	customfield_15004: 'Time Estimate (months)',
	customfield_15005: 'PipeTeam',
	customfield_10230: 'Release Version History',
	customfield_15002: 'Product Owner',
	fixVersions: 'Fix Version/s',
	customfield_15003: 'Manager',
	customfield_14711: 'Authorized Driver',
	customfield_11200: 'Checklist',
	customfield_15008: 'Test Plan',
	customfield_14712: 'Admin Resource Request Status',
	customfield_15006: 'Meetings',
	customfield_14710: 'Trade',
	customfield_15007: 'Relevant Documentation',
	customfield_10225: 'Baseline Start',
	customfield_14704: 'Post Validation Actions',
	customfield_10226: 'Baseline End',
	customfield_14705: 'Vehicle Request',
	customfield_10227: 'Velocity %',
	customfield_14703: 'Related to Verification',
	customfield_10229: 'MS-Project ID',
	customfield_14708: 'Work Location',
	customfield_14709: 'Driver Training Complete',
	customfield_14706: 'Resource Request',
	customfield_14707: 'Task or Event Participants',
	customfield_16200: 'Starting',
	customfield_10220: 'Planned Start',
	customfield_16201: 'FE-test',
	customfield_10221: 'Planned End',
	customfield_12400: 'Container Link',
	customfield_10222: 'Latest Start',
	customfield_10101: 'Watchers',
	customfield_10223: 'Latest End',
	customfield_10224: 'Gantt Options',
	customfield_11303: 'Start date',
	customfield_15903: 'Max Expected (months)',
	customfield_11304: 'End date',
	customfield_11305: 'Baseline start date',
	customfield_14812: 'Activity ID',
	customfield_15901: 'Max Expected Dollars (K$)',
	customfield_15109: 'Program Increment',
	customfield_11306: 'Baseline end date',
	customfield_15902: 'Min Expected (months)',
	customfield_11307: 'Progress',
	timeestimate: 'Remaining Estimate',
	status: 'Status',
	customfield_15100: 'Traveler',
	customfield_15104: 'Is Parent Risk',
	customfield_15101: 'Summit Start Date',
	customfield_15102: 'Summit End Date',
	customfield_11300: 'Bibcode',
	customfield_14811: 'Discipline',
	customfield_15900: 'Min Expected Dollars (K$)',
	customfield_15108: 'Task mode',
	customfield_11301: 'Peer Reviewed',
	customfield_10203: 'Business Value',
	customfield_10204: 'Rank (Obsolete)',
	customfield_10205: 'Sprint',
	customfield_10206: 'Epic Link',
	aggregatetimeestimate: 'Σ Remaining Estimate',
	creator: 'Creator',
	customfield_16303: 'Site',
	aggregateprogress: 'Σ Progress',
	customfield_14800: 'AIV Build Code',
	customfield_10201: 'Epic/Theme',
	customfield_10202: 'Story Points',
	customfield_15320: 'HazardSubComponent',
	timespent: 'Time Spent',
	customfield_15202: 'COBRA_WP',
	customfield_15203: 'Contracted Service',
	customfield_15201: 'Risks Mitigated',
	customfield_15206: 'Blocks Verification Issues',
	aggregatetimespent: 'Σ Time Spent',
	customfield_11401: 'Risk consequence',
	customfield_13700: 'Requires Monitoring?',
	customfield_15204: 'Requirement Priority',
	customfield_11400: 'Risk probability',
	customfield_15205: 'Blocked By',
	customfield_15318: 'Originating Hazard Analysis',
	customfield_15319: 'Hazard Analysis Selector',
	workratio: 'Work Ratio',
	created: 'Created',
	customfield_15312: 'Hazard Risk Level',
	customfield_15310: 'Hazard Probability',
	customfield_16400: 'Related Issues',
	customfield_15311: 'Hazard Severity',
	customfield_15316: 'Reduced Hazard Probability',
	customfield_10300: 'Reviewers',
	customfield_15314: 'Hazard Mitigation Verification Artifact(s)',
	customfield_15315: 'Reduced Hazard Severity',
	customfield_15308: 'Project Phases',
	customfield_15301: 'Requirement Expected Compliance',
	customfield_15302: 'Machine or Sub-Process',
	customfield_15305: 'Task Description',
	customfield_15306: 'Hazard (Hazard Category)',
	customfield_15303: 'Hazard Number',
	customfield_15304: 'Users',
	customfield_13114: 'Anticipated completion date',
	customfield_11601: 'Flowdown Doc',
	customfield_14319: 'Follow Up Completion Date',
	customfield_11600: 'Milestone Level',
	customfield_14317: 'Follow Up Completed By',
	customfield_14318: 'Further Recommendations'
};

async function main() {
	const configuration = {
		name: 'LSST Data Management',
		tracker_host: 'jira.lsstcorp.org',
		jql: 'project = DM',
		timeout: 5000
	};

	console.log("Requesting data from issue tracker");

	const stories = await getMultiPageTrackerResponse(configuration.tracker_host, configuration.jql, configuration.timeout, 0, configuration.name);

	console.log(`Retrieved [${stories.length}] records.`);

	const csv = new ObjectsToCsv(stories);
	try {
		const filename = getValidFileName(`${configuration.name}_stories`, 'csv');
		await csv.toDisk(filename, { allColumns: true });
		console.log("Saved to disk as csv: " + filename);
	} catch (e) {
		console.error(e);
	}
}

/**
 * Does a small call and retrieves the names key which contains the required fields
 * @param {string} host 
 * @param {string} jql 
 * @returns 
 */
async function getJiraFieldNames(host, jql) {
	const response = await getTrackerResponse(host, jql, 0, 1, true);
	const fieldNames = response.names;
	return fieldNames;
}

/**
 * Checks if a file with a given name exists and whehter it is alreayd duplicated with a file(n) number indication for the amount of duplications.
 * @param {string} path 
 * @param {string} extension 
 * @returns {string} - retursn one of three things, [filename.ext | filename(1).ext | filename(n+1).ext]
 */
function getValidFileName(path, extension) {
	try {
		const fullPath = `${path}.${extension}`;

		if (fs.existsSync(fullPath)) {
			const numRegex = /\((\d+)\)$/;
			const matches = path.match(numRegex); // matches the "somefilename(1)" the number in the parenthesis so it can be incremented
			if (matches && matches.length > 1) {
				// found numbered file
				const num = parseInt(matches[1]);
				const newName = path.replace(numRegex, `(${num + 1})`);
				return getValidFileName(newName, extension);
			}

			return getValidFileName(path + '(1)', extension)
		} else {
			return fullPath;
		}
	} catch (e) {
		console.error(e);
	}
}

/**
 * Saves json to a file
 * @param {string} path 
 * @param {object} json 
 * @returns 
 */
async function saveJson(path, json) {
	return fs.promises.writeFile(path, JSON.stringify(json));
}

/**
 * 
 * @param {string} tracker - jira issue tracker host
 * @param {string} jql - jira query to execute
 * @param {number} [startPosition] - start offset for issue retrieval
 * @param {number} [resultCount] - maxcount of items that will be retrieved, this cannot overwrite the server setting so resultCount might be smaller; 1000 seems to be the default for jira
 * @returns {}
 */
async function getTrackerResponse(tracker, jql, startPosition, resultCount, getNames) {
	if (!resultCount) {
		resultCount = 1000;
	}

	if (!startPosition) {
		startPosition = 0;
	}

	let url = `https://${tracker}/rest/api/2/search?jql=${jql}&maxResults=${resultCount}&startAt=${startPosition}`;
	if (getNames) {
		url += '&expand=names';
	}

	return axios.get(url).then(x => {
		console.log(`Request - ${x.statusText} [${x.status}]`);
		console.log('----------------------\n')
		return x.data;
	});
}

/**
 * Resolves promise after time amount of ms have passed
 * @param {number} time 
 * @returns {Promise}
 */
async function sleep(time) {
	return new Promise(resolve => setTimeout(resolve, time));
}

/**
 * 
 * @param {string} tracker - jira issue tracker host
 * @param {string} jql - jira query to execute
 * @param {number} [timeout] - time between requests if multiple pages of data are going to be retrieved 
 * @param {number} [startOffset] - start offset for issue retrieval
 * @param {string} [saveResponseFileName] - if passed raw response will be saved to file
 * @param {number} [maxRequestCount] - maximum amount of requests to execute
 * @param {number} [resultCount] - maxcount of items that will be retrieved, this cannot overwrite the server setting so resultCount might be smaller; 1000 seems to be the default for jira
 * @returns {Issue[]}
 */
async function getMultiPageTrackerResponse(tracker, jql, timeout, startOffset, saveResponseFileName, maxRequestCount, resultCount) {
	if (!maxRequestCount) {
		maxRequestCount = -1;
	}

	let result = [];
	let current = [];
	let cursor = startOffset ? startOffset : 0;
	let page = 0;
	let getNextPage = true;

	do {
		try {
			console.log(`Executing request starting at ${cursor}`);
			const response = await getTrackerResponse(tracker, jql, cursor, resultCount);
			if (saveResponseFileName) {
				const filename = getValidFileName(saveResponseFileName + '_raw_response', 'json');
				saveJson(filename, response);
			}
			current = getStoriesFromResponse(response);
			page++;
			getNextPage = current.length && (maxRequestCount < 0 || page < maxRequestCount);
			cursor = cursor + current.length;
			result = result.concat(current);

			if (getNextPage && timeout) { // skip if last iteration
				console.log(`Waiting for ${timeout} ms.`);
				await sleep(timeout);
			}
		} catch (e) {
			console.error(e);
			current = [];
			break;
		}

	} while (getNextPage);
	console.log(`Executed ${page} requests to retrieve ${result.length} issues.`);

	return result;
}

/**
 * Maps issues from jira response into fixed format
 * @param {*} response - jira api response
 * @returns {Issue[]}
 */
function getStoriesFromResponse(response) {
	return response.issues.map(normalizeStory)
}


/**
 * 
 * @param {Object.<string, *>} issue 
 * @returns {Object.<string, string>}
 */
function lsstcorpDMFieldMapper(issue) {
	const SPRINT_FIELD = 'customfield_10205';
	const FIELD_MAP = {
		points: 'customfield_10202',
		urgent: 'customfield_15602',
		severity: 'customfield_12906',
		probability: 'customfield_12908',
		probability_final: 'customfield_12905',
		harm: 'customfield_12909',
		risk_likelyhood: 'customfield_16701',
		risk_impact: 'customfield_16700',
		resolutiondate: 'resolutiondate',
		requirement_prio: 'customfield_15204'
	}

	let result = {};
	const sprints = parseJiraSprintFormat(issue[SPRINT_FIELD] || []).sort(makeStringKeySorter('startDate', true));
	const lastSprint = sprints.length ? sprints[0] : null;

	result.sprint_count = sprints.length;

	if (lastSprint) {
		const sprPrefixed = Object.keys(lastSprint).reduce((total, current) => {
			total[`last_sprint_${current}`] = lastSprint[current];
			return total;
		}, {});
		
		result = {
			...result,
			...sprPrefixed
		}
	}

	Object.keys(FIELD_MAP).forEach(key => {
		const fieldName = FIELD_MAP[key];
		result[key] = issue[fieldName];
	});

	return result;
}

/**
 * 
 * @param {string} key - key in object to sort on
 * @param {boolean} descending - if true will sort descending instead of ascending
 * @returns - sort function to be used on [].sort
 */
function makeStringKeySorter(key, descending) {
	const first = descending ? -1 : 1;
	const second = descending ? 1 : -1;

	return function (a, b) {
		if (a[key] > b[key]) return first;
		if (a[key] < b[key]) return second;
		return 0;
	}
}

/**
 * 
 * @param {string[]} sprints - weird jira format sprint string see https://jira.atlassian.com/browse/JSWSERVER-9928
 * @returns {Object.<string, string>}
 */
function parseJiraSprintFormat(sprints) {
	return sprints.map(sprintStr => {
		const sprStringRegex = /com\.atlassian\.greenhopper\.service\.sprint\.Sprint\@[a-z0-9]+\[(.*)\]/gm;
		const [fullmatch, sprintblock] = sprStringRegex.exec(sprintStr);
		const sprint = sprintblock.split(',')
			.reduce((total, current) => {
				const [name, value] = current.split('=');
				total[name] = value;
				return total;
			}, {});
		return sprint;
	});
}

/**
 * Parses jira issue into a simpler fixed format
 * @param {*} story - issue from jira response
 * @returns {Issue}
 */
function normalizeStory(story) {
	const { self, key, fields } = story;

	return {
		link: self,
		id: key,
		labels: fields?.labels?.join(','),
		component_names: fields?.components?.map(c => c.name).join(','),
		components_descriptions: fields?.components?.map(c => c.description).join(','),
		type: fields?.issuetype?.name,
		project: fields?.project?.name,
		status: fields?.status?.name,
		status_key: fields?.status?.statusCategory?.key,
		summary: fields?.summary,
		description: fields?.description,
		assignee: fields?.assignee?.key,
		resolution: fields?.resolution,
		created: fields?.created,
		updated: fields?.updated,
		resolutiondate: fields?.resolutiondate,
		...lsstcorpDMFieldMapper(fields)
	}
}

/**
 * @typedef Issue
 * @property {string} link
 * @property {string} id
 * @property {string} labels
 * @property {string} component_names
 * @property {string} components_descriptions
 * @property {string} votes
 * @property {string} type
 * @property {string} project
 * @property {string} status
 * @property {string} status_key
 * @property {string} summary
 * @property {string} description
 * @property {string} assignee
 * @property {string} points
 * @property {string} urgent
 * @property {string} resolution
 * @property {string} created
 */

main()
	.catch(e => {
		console.log(e);
	})