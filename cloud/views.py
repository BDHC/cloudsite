from django.shortcuts import render, redirect
from .forms import UploadForm
from django.http import HttpResponse, JsonResponse, FileResponse
from .models import FileUpload
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request,'index.html')

def api_image_list(request):
    files = list(FileUpload.objects.values())
    return JsonResponse(files, safe=False)

def image_list(request):
    context = {'files':FileUpload.objects.all()}
    return render(request,'list.html',context)

# single uplaod views.py
# def upload_image(request):
#     context = {'files':FileUpload.objects.all(),'form':UploadForm(request.POST, request.FILES)}
#     if request.method == 'POST':
#         form = UploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('upload_image')
#     else:
#         form = UploadForm()
#     return render(request, 'upload.html',context)

# multiple upload views.py
@login_required(login_url='login')
def upload_image(request):
    if request.user.is_authenticated:
        context = {'files':FileUpload.objects.all(),'form':UploadForm(request.POST, request.FILES)}
        if request.method == 'POST':
            form = UploadForm(request.POST, request.FILES)
            print('test1')
            if form.is_valid():
                for f in request.FILES.getlist('file'):
                    file_instance = FileUpload(file=f)
                    file_instance.save()
            return redirect('upload_image')
        else:
            form = UploadForm()
    else:
        return redirect('index')
    return render(request, 'upload.html',context)




def file_download(request, pk):
    if request.method == 'GET':
        if not FileUpload.objects.filter(pk=pk).exists():
            return  HttpResponseNotFound("<h1>Error: File not found</h1>")
        tmpfile = FileUpload.objects.get(pk=pk).file
        return FileResponse(tmpfile)
    else: 
        return  HttpResponseNotFound("<h1>Page not found</h1>")

def delete_file(request, pk):
    if request.method == 'POST':
        file = FileUpload.objects.get(pk=pk)
        file.delete()
    return redirect('upload_image')