from django.shortcuts import render,redirect
from django.http import HttpResponse

def home(request):
    return render(request,"home.html")

def puja(request):
    return render(request,"puja.html")


def donation(request):
    return render(request,"donation.html")

def history(request):
    return render(request,"history.html")

def history(request):
    return render(request,"history.html")

def events(request):
    return render(request,"events.html")


from django.shortcuts import render, redirect
from .models import Feedback

def feedback_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Create a new Feedback object
        feedback = Feedback(name=name, email=email, message=message)
        feedback.save()  # Save to the database

        return redirect('/feedback_success')  # Redirect after successful submission

    return render(request, 'home.html')  # Render the feedback form


def feedback_success(request):
    return render(request,"feedback_success.html")

def gallary(request):
    return render(request,"gallary.html")

def payment(request):
    return render(request,"payment.html")

def projects(request):
    return render(request,"projects.html")


# views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Donation
import razorpay
import json

# Initialize Razorpay client
razorpay_client = razorpay.Client(auth=("YOUR_RAZORPAY_KEY_ID", "YOUR_RAZORPAY_SECRET_KEY"))

def donation_page(request):
    return render(request, 'donation.html')

@csrf_exempt
def create_donation(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        amount = int(float(data['amount']) * 100)  # Convert to paise
        
        # Create Razorpay Order
        razorpay_order = razorpay_client.order.create(dict(
            amount=amount,
            currency='INR',
            payment_capture='0'
        ))
        
        # Return the order ID to the frontend
        return JsonResponse({
            'id': razorpay_order['id'],
            'amount': amount
        })

@csrf_exempt
def donation_success(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        # Verify the payment signature
        params_dict = {
            'razorpay_payment_id': data['razorpay_payment_id'],
            'razorpay_order_id': data['razorpay_order_id'],
            'razorpay_signature': data['razorpay_signature']
        }
        
        try:
            razorpay_client.utility.verify_payment_signature(params_dict)
        except:
            return JsonResponse({'status': 'fail', 'message': 'Invalid payment signature'})
        
        # If signature is valid, save the donation
        donation = Donation(
            name=data['name'],
            email=data['email'],
            mobile=data['mobile'],
            address=data['address'],
            amount=float(data['amount']) / 100,  # Convert back to rupees
            razorpay_payment_id=data['razorpay_payment_id']
        )
        donation.save()
        
        return JsonResponse({'status': 'success', 'message': 'Donation recorded successfully'})