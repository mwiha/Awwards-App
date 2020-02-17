from .models import Profile,Project,Voted
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
# from .forms import NewsLetterForm,NewArticleForm
# from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
def home(request):
    projects = Project.objects.all()
    return render(request,'home.html',{"projects":projects})

def register(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']            
            last_name = form.cleaned_data['last_name']
            

            user = User.objects.create_user(username,email,password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            
            profile = Profile(user=user,profile_pic='profile_pics/avatar.png')
            profile.save()
            return redirect(handle_login)

         
    form = RegForm()
    return render(request,'auth/registration.html',
    {"form":form})

def handle_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user:
                login(request,user)
                return redirect(home)
            else:
                # HANDLE INVALID LOGIN
                print('None')

    form = LoginForm()
    return render(request,'auth/login.html',{"form":LoginForm})

def handle_logout(request):
    logout(request)
    return redirect(handle_login)

@login_required(login_url='/login') 
def user_profile(request,username):
    user = User.objects.get(username=username)
    profile = Profile.get_user_profile(user)
    
    if 'bio' in request.POST:
        editForm = EditProfile(request.POST)
        if editForm.is_valid():
            profile.bio = editForm.cleaned_data['bio']
            profile.save()
            return redirect(user_profile)

    editForm = EditProfile()


    form = ProjectForm()
    projects = Project.get_user_projects(profile)
    overall_rating = Project.get_overall_average(projects)
    


    return render(request,'profile.html',{"profile":profile,"form":form,
    "projects":projects,"overall_rating":overall_rating,
    "editForm":editForm,})

@login_required(login_url='/login') 
def handle_profile_pic(request):
    profile = Profile.get_user_profile(request.user)
    if request.method == 'POST':
        pic = request.FILES['profile_pic']
        profile.profile_pic = pic
        profile.save()
    return redirect(user_profile,request.user.username)


@login_required(login_url='/login') 
def handle_project_upload(request):
    profile = Profile.get_user_profile(request.user)




    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        link = request.POST['link']
        pic = request.FILES['project_pic']
        project = Project(name=name,description=description,project_pic=pic,profile=profile,link=link)
        project.save()
        

    return redirect(user_profile,request.user.username)

@login_required(login_url='/login') 
def project_details(request,project_id):
    project = Project.objects.get(pk=project_id)
    has_user_voted = Voted.has_user_voted(project,request.user)

    return render(request,'project-details.html',
    {"project":project,"has_user_voted":has_user_voted})

@login_required(login_url='/login') 
def ratings(request,project_id):
    project = Project.objects.get(pk=project_id)
    voted = Voted(user=request.user,project=project)
    voted.save()
    print(project)
    
    design = int(request.POST['design'])
    usability = int(request.POST['usability'])
    content = int(request.POST['content'])
    average = (design + usability + content)/3


    if project.design == 0 and project.content == 0 and project.usability == 0: 
        project.design = design
        project.usability = usability
        project.content = content
        project.average = average
        project.save()
    else:
        project.design = (project.design + design)/2
        project.content = (project.content + content)/2
        project.usability =(project.usability + usability)/2
        project.average = (project.average  + average)/2
        project.save()
    
    data = {'success':'Rated'}
    
    return JsonResponse(data)

@login_required(login_url='/login') 
def search_projects(request):
    search_term = request.GET['search']
    projects = Project.search_projects(search_term)
    return render(request, 'search.html',{"projects":projects})



from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer

class ProfileList(APIView):
    def get(self,request,format=None):
        all_profiles = Profile.objects.all()
        
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)

class ProjectList(APIView):
    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects,many=True)
        return Response(serializers.data)