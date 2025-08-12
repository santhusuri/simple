from django.shortcuts import render, redirect

# admin_home: shows admin-only features when request.user.is_staff True

def admin_home(request):
    return render(request, 'adminportal/home.html')

# escalate: intentionally insecure endpoint to demo privilege escalation
# For demo purposes only: allow ?make_admin=1&user=username to set the user's is_staff flag

def escalate(request):
    if request.GET.get('make_admin') == '1':
        uname = request.GET.get('user')
        from django.contrib.auth.models import User
        try:
            u = User.objects.get(username=uname)
            u.is_staff = True
            u.save()
            return render(request, 'adminportal/escalated.html', {'user': u})
        except User.DoesNotExist:
            pass
    return render(request, 'adminportal/escalate.html')