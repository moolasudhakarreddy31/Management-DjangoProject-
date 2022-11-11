from django.shortcuts import  render, redirect

from ticket_manager.models import Ticket
from .forms import NewUserForm, TicketForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)




def homepage(request):
    return render(request,'homepage.html')

def index(request):
    if not request.user.is_authenticated:
        return redirect("ticket_manager:login")
    tickets = Ticket.objects.order_by('-created_at')[:5]
    return render(request,'homepage.html', {'tickets': tickets})


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("ticket_manager:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("ticket_manager:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def ticket_by_id(request, ticket_id):
    if not request.user.is_authenticated:
        return redirect("ticket_manager:login")
    ticket = Ticket.objects.get(pk=ticket_id)
    return render(request, 'ticket_by_id.html', {'ticket':ticket})

def creating_ticket(request):
    if not request.user.is_authenticated:
        return redirect("ticket_manager:login")
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ticket created successfully." )
            return redirect("ticket_manager:homepage")
    form = TicketForm()
    return render(request, 'ticket.html', context={'ticket_form': form})


def update_view(request, ticket_id):
    if not request.user.is_authenticated:
        return redirect("ticket_manager:login")
    obj = get_object_or_404(Ticket, id=ticket_id)
    form = TicketForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(f"/ticket/{ticket_id}")
    context = {"form": form}
    return render(request, "update_view.html", context)