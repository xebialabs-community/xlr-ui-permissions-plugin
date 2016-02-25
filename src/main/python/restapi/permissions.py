import org.codehaus.jettison.json.JSONObject
import os
def exportSecurityToJSON():
	security = dict()
	for release in releaseApi._delegate.releases:
		for team in release.teams:
			member = []
			member.extend(team.members)
			member.extend(team.roles)
			member = map(lambda it: str(it), member)
			print str(release.status) + " : " + release.title + " : " + team.teamName + " : " + str(member) + " : " + str(team.permissions)
			security[str(release.status) + "::" + release.title + "::" + team.teamName + "::" + str(member)] = str(team.permissions)
	return security		
response.entity = exportSecurityToJSON()
