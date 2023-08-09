from django.shortcuts import render, get_object_or_404, redirect
from authentication.models import User
from .forms import WorkerForm, DeleteWorkerForm
from .models import Worker, Metier
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required, permission_required


# Page d'accueil
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    metier = Worker.objects.filter(
        metier__nom_du_metier__contains=q
    )
    profiles = User.objects.all()
    workers = Worker.objects.all()
    metiers = Metier.objects.all()
    context = {'metiers': metiers,
               'profiles': profiles,
               'workers': workers,
               'metier':metier,
               }
    return render(request, "home.html", context)


# Créer Profil Travailleur
@permission_required("job.add_worker", raise_exception=True)
def worker(request):
    work_form = WorkerForm
    message = ""
    if request.method == "POST":
        work_form = WorkerForm(request.POST, request.FILES)
        if work_form.is_valid():
            work = work_form.save(commit=False)
            work.ouvrier = request.user
            work.save()
            return redirect("job:home")
        else:
            message = "Vous n'ètes pas Ouvrier pour avoir accées à cet page"
    context = {
        'work_form': work_form,
        'message': message
    }
    return render(request, "job/work.html", context)


@permission_required(["job.change_worker", "job.delete_worker"], raise_exception=True)
# Modifier ou supprimer profil Travailleur
def edit_or_delete_worker(request, work_id):
    worker = get_object_or_404(Worker, id=work_id)
    edit_worker = WorkerForm(instance=worker)
    delete_worker = DeleteWorkerForm()
    if request.method == "POST":
        if "edit_worker" in request.POST:
            edit_worker = WorkerForm(request.POST, instance=worker)
            if edit_worker.is_valid():
                edit_worker.save()
                return redirect("job:workers_views")
        if "delete_worker" in request.POST:
            delete_worker = DeleteWorkerForm(request.POST)
            if delete_worker.is_valid():
                worker.delete()
                return redirect("job:workers_views")

    context = {
        "edit_worker": edit_worker,
        "delete_worker": delete_worker
    }

    return render(request, "job/edit_and_delete_work.html", context)


# Vue de Travailleur
@login_required
def views_worker(request, id):
    work = get_object_or_404(Worker, id=id)
    likes_connected = get_object_or_404(Worker, id=id)
    liked = False
    if likes_connected.likes.filter(id=request.user.id).exists():
        liked = True
    # data['number_of_likes'] = likes_connected.number_of_likes()
    # data['post_is_liked'] = liked

    return render(request, "job/work_detail.html", {'work': work, "liked":liked})


# Vue pour les travailleur
@login_required
def views_workers(request):
    workers = Worker.objects.all()
    metiers = Metier.objects.all()
    context = {'workers': workers,
               'metiers':metiers}
    return render(request, "job/views_workers.html", context)


def LikeWorker(request, pk):
    worker = get_object_or_404(Worker, id=request.POST.get('work_id'))
    if worker.likes.filter(id=request.user.id).exists():
        worker.likes.remove(request.user)
        work = "Like"
    else:
        worker.likes.add(request.user)
        work = "unLike"
    return HttpResponseRedirect(reverse('job:worker_detail', args=[str(pk)]))