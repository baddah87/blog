from django.http import JsonResponse
from django.shortcuts import render
import requests
# Create your views here.
def org_members(request):
	person = request.user
	github_account= person.socialaccount_set.get(user=person.id)
	token_object= github_account.socialtoken_set.get(account=github_account.id)
	token = token_object.token

	url = "https://api.github.com/orgs/joinCODED/members"

	response= requests.get(url, headers={'Authorization': 'token '+token})
	# return JsonResponse(response.json(), safe=False)
	return render(request, 'git.html', {'members':response.json()})




def list_repo(request):
	person = request.user
	github_account= person.socialaccount_set.get(user=person.id)
	token_object= github_account.socialtoken_set.get(account=github_account.id)
	token = token_object.token

	url = "https://api.github.com/user/repos"

	response= requests.get(url, headers={'Authorization': 'token '+token})
	# return JsonResponse(response.json(), safe=False)
	return render(request, 'repos.html', {'repos':response.json()})
