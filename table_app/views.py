from django.shortcuts import render

# Create your views here.
def table(request):
    return render(request, 'table_app/tables-data.html', {})


def main(request):
    return render(request, 'table_app/index.html', {})