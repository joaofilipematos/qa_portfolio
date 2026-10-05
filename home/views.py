from django.shortcuts import render

def home(request):
    """Render the homepage."""
    context = {
        'page_title': 'Home - QA Portfolio',
        'tagline': 'Test Automation & QA Engineering',
    }
    return render(request, 'home/index.html', context)
