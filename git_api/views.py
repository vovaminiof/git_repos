# Create your views here.
from github import Github
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	if request.method == 'POST':
		query = request.POST['query']
		users = []
		try:
			g = Github('vovaminiof', '14011994ly')
			repo = g.get_repo(query)
			for user in repo.get_contributors():
				obj = {'id': user.id, 'name' : user.name, 'login' : user.login, 'link' : user.html_url}
				users.append(obj)
		except Exception as ex:
			return HttpResponse('Currently unavailable')
		
		return render(request, 'index.html', {'users':users})

	return render(request,'index.html')