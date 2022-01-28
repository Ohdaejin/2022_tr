from django.shortcuts import render

def main(request):

    return render(request, 'group/group_main.html')


def make(request):

    return render(request, 'group/group_make.html')


def mine(request):

    return render(request, 'group/group_mine.html')