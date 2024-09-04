from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306207505',
        'name': 'Alexander William Lim',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
