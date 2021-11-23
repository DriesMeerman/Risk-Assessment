# Jira Data retrieval

# Usage
To retrieve data from lsst corp's jira.

Start by installing the dependencies  
`npm install`  

Then run one of the following:  
`npm run start`  
`node getJiraStories.js`  

This will create a csv file containing all the stories from the instance.

## Modifications for different Jira instances

To change where data should be retrieved from the following should be changed.  

On line 963:
```javascript
const configuration = {
		name: 'LSST Data Management',
		tracker_host: 'jira.lsstcorp.org',
		jql: 'project = DM',
		timeout: 5000
	};
```

Change the tracker host and query so correct data will be retrieved.
Change the name so generated files have correct and clear naming, as generated csv and other files are pre-fixed with this name.

There is a helper function that can be called to retrieve field names of other Jira instances.
`getJiraFieldNames` output of this function for lsstcorp's jira is hardcoded into the file with the variable name `lsstFieldMap`.  

For other Jira instances the custom fields can be different.
So change the mapping in the `lsstcorpDMFieldMapper` function, or replace that function with a different mapper at line 1244 in `normalizeStory` method.