from django.shortcuts import render

# Create your views here.
from .forms import SignUpForm
from .models import Profile

def update_user_data(user):
    Profile.objects.update_or_create(user=user, defaults={'mob': user.profile.mob},)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()

            #newly added
            user.profile.mob = form.cleaned_data.get('mob')
            update_user_data(user)  

            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')

            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            # redirect user to home page
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})