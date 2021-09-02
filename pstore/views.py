from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate  # add this
from django.contrib import messages

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
# Create your views here.

from . forms import OrderForm1


from .models import *


@login_required(login_url='login_request')
def home(request):
    if request.method == 'POST':
        ctype = request.POST.get("nctype")
        color = request.POST.get('colorchange')
        note = request.POST.get('nnote')
        if "fullchange" in request.POST and request.POST.get('nctype') == 'full':
            picId = request.POST.get('npid')
            font = request.POST.get('fontchange')
            con = request.POST.get('ngetcon')
            pic = get_object_or_404(PhotoStoreModel, id=picId)
            datad = {"Font: ": font, "Color: ": color, "Content: ": con}
        elif "nclogoform" in request.POST and request.POST.get("nctype") == 'logo':
            picId = request.POST.get('npid')
            font = "No Change"
            pic = get_object_or_404(PhotoStoreModel, id=picId)
            datad = "Color: " + color
        else:
            return render(request, 'pstore/formerror.html', {"msg": "Form is not valid"})

        if(pic):

            formdata = FormCust1Model(
                order_from=request.user,
                photoid=pic,
                custType=ctype,
                detail=datad,
                note=note,
            )
            formdata.save()
            return render(request, 'pstore/formsuccess.html', {"msg": "Form Success"})

    data = ""
    catinfo = ""
    if(request.GET.get('catid')):
        catId = request.GET.get('catid')
        data = PhotoStoreModel.objects.filter(cat=catId)
        catobj = Category.objects.get(id=catId)
        catinfo = catobj.cat
        print(request.GET.get('catid'))

    else:
        data = PhotoStoreModel.objects.all()
        catinfo = False
    cat = Category.objects.all()

    context = {"cat": cat, "data": data, "catinfo": catinfo}
    return render(request, 'pstore/home.html', context)


# class DocumentDownload(View):
#     def get(self, request, relative_path):
#         document = get_object_or_404(Document, file=relative_path)
#         if not request.user.is_superuser and document.created_by != request.user:
#             return HttpResponseForbidden()
#         absolute_path = '{}/{}'.format(settings.MEDIA_ROOT, relative_path)
#         response = FileResponse(open(absolute_path, 'rb'), as_attachment=True)
#         return response
@login_required(login_url='login_request')
def mediaview(request):
    pass


def register(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('login')

    else:
        f = UserCreationForm()

    return render(request, 'pstore/register.html', {'form': f})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="pstore/login.html", context={"login_form": form})


@login_required(login_url='login_request')
def logoutUser(request):
    logout(request)
    return redirect('login_request')


@login_required(login_url='login_request')
def teamDash(request):
    task = FormCust1Model.objects.all()
    count = task.count()
    ass = FormCust1Model.objects.all().order_by('-date')[:3]
    context = {"task": task, "count": count, "ass": ass}
    return render(request, 'pstore/team-dashboard.html', context)
