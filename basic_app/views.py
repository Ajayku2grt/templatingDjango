from django.shortcuts import render

# Create your views here.
def index(request):
    data={'text':"Future depend what you do in present.",'text_1':'Build ourself',
          'text_2':'bluid good habits, fuel your dream, be consistent, remove porn',
          'number':66}
    return render(request,'basic_app/index.html',data)


def other(request):
    return render(request,'basic_app/other.html')


def relative(request):
    return render(request,'basic_app/relative_url_templates.html')
