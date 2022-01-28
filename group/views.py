from django.shortcuts import render

def main(request):

    return render(request, 'group/group_main.html')