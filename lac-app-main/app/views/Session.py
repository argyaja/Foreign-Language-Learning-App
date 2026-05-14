from django.shortcuts import render, redirect

def set_session_view(request):
    # Set nilai dalam session
    request.session['username'] = 'john_doe'
    return redirect('get_session_view')

def get_session_view(request):
    # Ambil nilai dari session
    username = request.session.get('username', 'Guest')
    return render(request, 'some_template.html', {'username': username})

def logout_view(request):
    # Hapus data session
    request.session.flush()
    return redirect('login')