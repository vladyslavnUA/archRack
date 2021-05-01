from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.utils import timezone
from django import template
import django.template.library
from .models import *
from .forms import *

register = template.Library()

@login_required
def dashboard(request):
    user = request.user
    # print(Project.objects.all().filter(owner=user) | Project.objects.filter(collaborators=user.id))
    projects = Project.objects.all().filter(owner=user) | Project.objects.filter(collaborators=user.id)
    context = {
        'projects': projects
    }
    return render(request, 'app/index.html', context)

@login_required
def browse(request):
    context = {}
    return render(request, 'app/browse.html', context)

@login_required
def singleproject(request):
    context = {}
    return render(request, 'app/single-channel.html', context)

@login_required
def h(request):
    context = {}
    return render(request, 'app/sheet.html', context)

@login_required
def singlevideo(request):
    context = {}
    return render(request, 'app/single-video.html', context)

@login_required
def newdoc(request):
    form = CreateDocForm()
    user = request.user
    if request.method == "POST":
        form = CreateDocForm(request.POST or None)

        if form.is_valid():
            print(form.cleaned_data.get('collaborators'))
            allcollabs = []
            doc = RackDoc()
            doc.name = form.cleaned_data.get('name')
            doc.content = form.cleaned_data.get('content')
            doc.project = form.cleaned_data.get('project')
            doc.created_at = timezone.now()
            doc.owner = user
            doc.slug = doc.name.replace(' ', '-')
            doc.save()
            collabs = form.cleaned_data.get('collaborators')
            users = CustomUser.objects.all()
            for i in collabs:
                allcollabs.append(i.id)
            doc.collaborators.set(allcollabs)
            doc.save()
            return redirect('docdetail', slug=doc.slug)

    elif request.method == "GET":
        user = request.user
        form = CreateDocForm()
        oform = HalfDocForm()
        context = {
            'form': form,
            'oform': oform
        }
        print(form)
        return render(request, 'app/te.html', context)
    context = {
        'form': form
    }
    return render(request, 'app/rackdoc.html', context)

@register.inclusion_tag('app/partials/sidebar.html')
def sidebar(request):
    user = request.user
    projects = Project.objects.all().filter(owner=user)
    context = {
        'projects': projects,
    }
    return render(request, 'app/partials/sidebar.html', context)

@login_required
def myvids(request):
    context = {}
    return render(request, 'app/my-videos.html', context)

@login_required
def rand(request):
    user = request.user
    docs = RackDoc.objects.all().filter(owner=user)
    context = {
        'docs': docs
    }
    return render(request, 'app/random.html', context)

@login_required
def newproj(request):
    user = request.user
    form = CreateProjectForm()
    context = {
        'form': form
    }
    if request.method == "POST":
        form = CreateProjectForm(request.POST or None)

        if form.is_valid():
            allcollabs = []
            none = ['']
            name = form.cleaned_data.get('name')
            description = form.cleaned_data.get('description')
            owner = user
            collaborators = form.cleaned_data.get('collaborators')
            rackdocs = ''
            created_at = timezone.now()
            slug = name.replace(' ', '-')
            for i in collaborators:
                allcollabs.append(i.id)
            proj = Project.objects.create(name=name, description=description, owner=owner, 
                                        created_at=created_at, updated_at=None, slug=slug)
            proj.collaborators.set(allcollabs)
            # proj.rackdocs.set(none)
            proj.save()
            return redirect('projdetail', slug=slug)
        else:
            print(form.errors)

    # profile pic API:
    # get sample image
    # <img src="https://atilogri.sirv.com/Images/org.jpeg" width="612" height="408" alt="" />
    # https://atilogri.sirv.com/Images/org.jpeg?text={{text}}%21&text.size=50&text.color=EBC76D
    # https://demo.sirv.com/omans.jpg?text=Hello%20world%21&text.size=50&text.color=EBC76D

    elif request.method == "GET":
        user = request.user
        form = CreateProjectForm()
        context['form'] = form
        return render(request, 'app/newproj.html', context)
    return render(request, 'app/newproj.html', context)

@login_required
def projdetail(request, slug):
    user = request.user
    project = get_object_or_404(Project, slug=slug)
    docs = project.rackdocs.all().order_by('-updated_at')
    context = {
        'project': project,
        'docs': docs,
    }
    return render(request, 'app/projdetail.html', context)

@login_required
def docdetail(request, slug):
    user = request.user
    print(user)
    doc = get_object_or_404(RackDoc, slug=slug)
    projects = Project.objects.all().filter(owner=user) | Project.objects.filter(collaborators=user.id)
    context = {
        'doc': doc,
        'projects': projects
    }
    return render(request, 'app/docdetail.html', context)

# @login_required
# def docdetail(request, slug):
#     user = request.user
#     doc = get_object_or_404(RackDoc, slug=slug)
#     context = {
#         'doc': doc
#     }
#     return render(request, 'app/docdetail.html', context)

@login_required
def editdoc(request, slug):
    doc = get_object_or_404(RackDoc, slug=slug)
    allthe = doc.collaborators.all()
    context = {}

    if not request.user == doc.owner and request.user not in allthe:
        # print(request.user)
            # .filter(doc_collaborators=request.user)
        # print(doc.collaborators.all().filter(doc_collaborators=request.user).exists())
        # if not doc.collaborators.filter(proj_collaborators=request.user.id):
        return redirect('docdetail', slug=slug)


    if request.method == "POST":
        form = UpdateDocForm(request.POST, instance=doc)

        if form.is_valid():
            doc.name = form.cleaned_data.get('name')
            doc.content = form.cleaned_data.get('content')
            doc.project = form.cleaned_data.get('project')
            doc.collaborators = form.cleaned_data.get('collaborators')
            doc.updated_at = timezone.now()
            doc.save()
            print(doc, 'saved')
            return redirect('docdetail', slug=slug)
        else:
            print(form.errors)

    elif request.method == "GET":
        user = request.user
        form = UpdateDocForm(instance=doc)
        context['doc'] = doc
        context['oform'] = form
        return render(request, 'app/updatedoc.html', context)
    return render(request, 'app/te.html')

@login_required
def profile(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'app/my-channel.html', context)

@login_required
def helpcenter(request):
    context = {}
    return render(request, 'app/help-center.html', context)

@login_required
def videolist(request):
    context = {}
    return render(request, 'app/video-list.html', context)

@login_required
def setting(request):
    context = {}
    return render(request, 'app/my-channel-settings.html', context)