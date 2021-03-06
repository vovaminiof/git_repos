# Create your views here.
from github import Github
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    if request.method == 'POST':
        query = request.POST['query']
        users = []
        try:
            g = Github(timeout=60*2)
            repo = g.get_repo(query)
            for user in repo.get_contributors():
                obj = {'id': user.id, 'name' : user.name, 'login' : user.login, 'link' : user.html_url}
                users.append(obj)
                print obj
        except Exception as ex:
            return render(request, 'index.html', {'users':users, 'error' : 'Rate limit exceeded '})
        
        return render(request, 'index.html', {'users':users})

    return render(request,'index.html')
