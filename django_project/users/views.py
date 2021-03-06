from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

# the code used with  **from django.contrib.auth.forms import UserCreationForm** without  forms.py
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}!')
#             return redirect('blog-home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'users/register.html', {'form': form})


# message types imported from django.contrib -> messages
# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error

#-----------------------------------------------------------------------
# the code used with forms.py and **UserRegisterForm**
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

