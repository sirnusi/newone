from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text':'helloworld', 'number':100}
    return render(request, 'basic_app/index.html', context_dict)

def other(reqst):
    return render(reqst, 'basic_app/other.html')

def relative(reques):
    return render(reques, 'basic_app/relative_url_template.html')