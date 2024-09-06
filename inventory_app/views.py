from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import SalesEntry
from django.views.generic.edit import UpdateView
from .models import SalesEntry, StockRequisition, DailyPurchase
from .forms import SalesEntryForm, DailyPurchaseForm
from django.contrib import messages


# Create your views here.
def HomePage(request):
    return render(request, 'home.html')



def LoginPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        paswd = request.POST.get('pass')
        user = authenticate(username=uname, password=paswd)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username/Password is incorrect!")
    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')

def DailyPurchase(request):
    if request.method == 'POST':
        form = DailyPurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            print("Form saved successfully")  # Debugging output
            return redirect('success')
        else:
            print("Form errors:", form.errors)  # Debugging output
    else:
        form = DailyPurchaseForm()
    return render(request, 'daily_purchase_entry.html', {'form': form})


def DailySales(request):
    if request.method == 'POST':
        form = SalesEntryForm(request.POST)
        print("Form data received:", request.POST)
        if form.is_valid():
            form.save()  # Save form data to the database
            # print("Form saved successfully")
            return redirect('success')  # Redirect to a success page or another view
        else:
            print("Form errors:", form.errors)
    else:
        form = SalesEntryForm()
    return render(request, 'daily_sales_entry.html', {'form': form})



def DailyStock(request):
    if request.method == 'POST':
        print(request.POST)
        date = request.POST.get('date')
        item_types = request.POST.getlist('item_type')
        item_names = request.POST.getlist('item_name')
        units = request.POST.getlist('unit')
        closings = request.POST.getlist('closing')
        requireds = request.POST.getlist('required')
        delivereds = request.POST.getlist('delivered')

        save_success = True
        for item_type, item_name, unit, closing, required, delivered in zip(item_types, item_names, units, closings, requireds, delivereds):
            try:
                StockRequisition.objects.create(
                    date=date,
                    item_type=item_type,
                    item_name=item_name,
                    unit=unit,
                    closing=float(closing),
                    required=float(required),
                    delivered=float(delivered)
                )
                print(f"Saved: {item_name}")  # Debugging output
            except Exception as e:
                messages.error(request, f"Error saving item {item_name}: {e}")
                print(f"Error: {e}")  # Debugging output
                save_success = False
                break

        if save_success:
            messages.success(request, "Stock requisitions have been saved successfully.")
            return redirect('home')
        else:
            return render(request, 'daily_stock_requisition.html')

    return render(request, 'daily_stock_requisition.html')


def update_view(request, pk):
    entry = get_object_or_404(SalesEntry, pk=pk)

    if request.method == 'POST':
        form = SalesEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SalesEntryForm(instance=entry)

    return render(request, 'view_update_sales_entry.html', {'form': form})


def SuccessView(request):
    return render(request, 'success.html')