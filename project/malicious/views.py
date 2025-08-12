from django.shortcuts import redirect, render

# intentionally vulnerable: no validation of 'url' param

def malicious_home(request):
    return render(request, 'malicious/home.html')


def open_redirect(request):
    target = request.GET.get('url')
    if target:
        return redirect(target)
    return render(request, 'malicious/redirect.html')