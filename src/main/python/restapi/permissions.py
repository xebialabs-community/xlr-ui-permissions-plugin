import org.codehaus.jettison.json.JSONObject
import os
def exportSecurityToJSON():
	security = dict()
	for release in releaseApi._delegate.releases:
		for team in release.teams:
			member = []
			role = []
			member.extend(team.members)
			role.extend(team.roles)
			member = map(lambda it: str(it), member)
			role = map(lambda it: str(it), role)
			memberString = str(member).replace("'","").replace("[","").replace("]","")
			roleString = str(role).replace("'","").replace("[","").replace("]","")
			security[str(release.status) + "::" + release.title + "::" + team.teamName + "::" + memberString + "::" + roleString] = str(team.permissions)
	return security		
response.entity = exportSecurityToJSON()
