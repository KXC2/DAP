from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import RegisterForm, JournalForm
from .models import Register, Journal


def index(request):
    return render(request, "index.html")

def view_journal(request):
    search_text = request.GET.get('search_text')

    if search_text is None:
        journals = []
    elif search_text == "":
        journals = Journal.objects.all().order_by('TimeDate')
    else:
        journals = Journal.objects.filter(
            Q(CellPhone__icontains=search_text) |
            Q(TransactionId__icontains=search_text)
        ).order_by('TimeDate')

    return render(request, 'view_journal.html', {'journals': journals})

def deposit(request):
    return render(request, "deposit.html")
def DialAndPay(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = RegisterForm()
    return render(request, "DialAndPay.html", {'form' : form})

def StandardDeposit(request):
    return render(request, "StandardDeposit.html")


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def check_number(request):
    if request.method == "POST":

        entered_value = request.POST.get('cellphone')

        record = Register.objects.filter(
            cellphone=entered_value
        ).first()

        if record:
            return JsonResponse({
                "found": True,
                "name" : record.name,
                "surname" : record.surname,
                "banks": list(record.banks.values_list("name", flat=True))

            })
        return JsonResponse({
            "found" : False
        })

def add_journal_entry(request):

    if request.method == "POST":

        form = JournalForm(request.POST)

        if form.is_valid():
            form.save()

            return JsonResponse({
                "success": True
            })

        return JsonResponse({
            "success": False,
            "errors": form.errors
        })

    return JsonResponse({
        "success": False
    })

