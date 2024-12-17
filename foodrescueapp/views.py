from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, logout
from django.contrib import messages
from foodrescue import models 
from foodrescue.models import User, Donor, Feedback2
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from django.db.models import Q  # Add this import
from django.contrib.auth.decorators import login_required

@csrf_exempt
def admin_contact(request):
    if request.method == 'GET':
        return render(request, 'admin_panel/manage_contact.html')

@csrf_exempt
def admin_contact_api(request):
    if request.method == 'GET':
        feedbacks = Feedback2.objects.all().values(
            "id", "name", "email", "phone_number", "message", "created_at"
        )
        data = list(feedbacks)
        return JsonResponse({"data": data}, safe=False)

    elif request.method == 'POST':
        try:
            body = json.loads(request.body)
            feedback_id = body.get('id')

            # İlgili kaydı sil
            feedback = Feedback2.objects.get(id=feedback_id)
            feedback.delete()

            return JsonResponse({"status": "success", "message": "Kayıt başarıyla silindi."})
        except Feedback2.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Kayıt bulunamadı."}, status=404)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)



@csrf_exempt
def admin_donors(request):
    if request.method == "GET":
        return render(request, "admin_panel/manage_donors.html")

@csrf_exempt
def admin_donor_api(request):
    if request.method == "GET":
        donors = Donor.objects.all().values(
            "donorId", "username", "email", "phonenumber", "createdAt", "is_active"
        )
        data = list(donors)
        return JsonResponse({"data": data}, safe=False)
    
    elif request.method == "POST":
        try:
            body = json.loads(request.body)
            donor_id = body.get("id")
            action = body.get("action")
            donor = Donor.objects.get(donorId=donor_id)
            if action == "activate":
                donor.is_active = True
            elif action == "deactivate":
                donor.is_active = False
            else:
                return JsonResponse({"message": "Geçersiz işlem."}, status=400) 
            
            donor.save()
            return JsonResponse({"message": "Bağışçı durumu başarıyla güncellendi."})   
        except Donor.DoesNotExist:
            return JsonResponse({"message": "Bağışçı bulunamadı."}, status=404)
        except Exception as e:
            return JsonResponse({"message": f"Bir hata oluştu: {str(e)}"}, status=500)
    

@csrf_exempt
def admin_panel(request):
    if request.method == "GET":
        return render(request, "admin_panel/manage_users.html")

@csrf_exempt
def admin_user_api(request):
    if request.method == "GET":
        users = User.objects.all().values(
            "customerId", "username", "email", "phonenumber", "createdAt", "is_active"
        )
        data = list(users)
        return JsonResponse({"data": data}, safe=False)
    
    elif request.method == "POST":
        try:
            body = json.loads(request.body)
            user_id = body.get("id")
            action = body.get("action")
            
  
            user = User.objects.get(customerId=user_id)
            
            if action == "activate":
                user.is_active = True
            elif action == "deactivate":
                user.is_active = False
            else:
                return JsonResponse({"message": "Geçersiz işlem."}, status=400)

            user.save()
            return JsonResponse({"message": "Kullanıcı durumu başarıyla güncellendi."})
        except User.DoesNotExist:
            return JsonResponse({"message": "Kullanıcı bulunamadı."}, status=404)
        except Exception as e:
            return JsonResponse({"message": f"Bir hata oluştu: {str(e)}"}, status=500)



def index(request):
    return render(request, 'app/Sayfa-1.html')
def login_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = models.User.objects.get(username=username)
            if user.check_password(password):  # check_password metodu çağrılıyor
                if not user.is_active:
                    messages.info(request, "Giriş yapmak için adminin onaylamasını bekleyiniz.")
                    return redirect('login')

                login(request, user)  # Django'nun login metodunu kullanıyoruz
                return redirect("index")
            else:
                messages.error(request, "Kullanıcı adı ya da parola yanlış")
        except models.User.DoesNotExist:
            messages.error(request, "Böyle bir kullanıcı bulunmamaktadır.")

    return render(request, "account/login.html")
def register_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        phonenumber = request.POST["phonenumber"]

        if password == repassword:
            # Kullanıcı adı kontrolü
            if models.User.objects.filter(username=username).exists():
                return render(request, "account/register.html", 
                              {
                                  "error": "Username kullanılıyor.",   
                                  "username": username,                                 
                                  "firstname": firstname,
                                  "lastname": lastname,  
                                  "email": email,
                                  "phonenumber": phonenumber,                              
                              })
            # E-posta kontrolü
            elif models.User.objects.filter(email=email).exists():
                return render(request, "account/register.html",
                              {
                                  "error": "Mail hesabı sistemimize kayıtlı.",
                                  "username": username,
                                  "email": email,
                                  "firstname": firstname,
                                  "lastname": lastname, 
                                  "phonenumber": phonenumber,                                  
                              })
            # Telefon numarası kontrolü
            elif models.User.objects.filter(phonenumber=phonenumber).exists():
                return render(request, "account/register.html",
                              {
                                  "error": "Telefon numarası sistemimize kayıtlı.",
                                  "username": username,
                                  "email": email,
                                  "firstname": firstname,
                                  "lastname": lastname, 
                                  "phonenumber": phonenumber,                                  
                              })
            else:
                # Kullanıcıyı create_user ile oluşturuyoruz
                user = models.User.create_user(
                    username=username,
                    email=email,
                    password=password,
                    phonenumber=phonenumber,
                    name=firstname,
                    surname=lastname,
                    is_active=False,
                    is_staff=False,
                    is_superuser=False
                )
                return redirect("login")
        else:
            return render(request, "account/register.html", 
                          {
                              "error": "Girdiğiniz parolalar eşleşmiyor.",
                              "username": username,
                              "email": email,
                              "firstname": firstname,
                              "lastname": lastname, 
                              "phonenumber": phonenumber,                                      
                          })
        
    return render(request, "account/register.html")
def logout_request(request):
    logout(request)
    return redirect("index")

@login_required
def reserve_donation_view(request, donation_id):
    donation = get_object_or_404(models.Donation, id=donation_id)
    
    if donation.is_reserved:
        messages.error(request, "This donation has already been reserved.")
        return redirect('create_donation_view')
    
    donation.is_reserved = True
    donation.reserved_by = request.user
    donation.save()
    
    messages.success(request, "Donation reserved successfully!")
    return redirect('create_donation_view')

@login_required
def cancel_reservation_view(request, donation_id):
    donation = get_object_or_404(models.Donation, id=donation_id)
    
    if donation.reserved_by != request.user:

        return redirect('create_donation_view')
    
    donation.is_reserved = False
    donation.reserved_by = None
    donation.save()
    

    return redirect('create_donation_view')


@login_required
def create_donation_view(request):
    if not request.user.is_authenticated:
        messages.warning(request, "You need to log in to perform this action.")
        return redirect('login')
    if request.method == 'POST':
        item = request.POST.get('item')
        quantity = request.POST.get('quantity')
        expiry_date = request.POST.get('expiry_date')
        
        try:
            models.DonateOperations.create_donate(item_name=item, quantity=quantity, expiry_date=expiry_date)
            return render(request, 'app/donate.html', {
                'success': 'Donation created successfully!',
                'donations': models.DonateOperations.get_current_donations()
            })
        except ValueError as e:
            return render(request, 'app/donate.html', {
                'error': str(e),
                'donations': models.DonateOperations.get_current_donations()
            })
    if request.user.is_staff:
        donations = models.DonateOperations.get_current_donations()
    else:
        donations = models.DonateOperations.get_current_donations().filter(
            Q(is_reserved=False) | 
            Q(reserved_by=request.user) 
        )
    return render(request, 'app/donate.html', {'donations': donations})

def delete_donation_view(request, donation_id):
    donation = get_object_or_404(models.Donation, id=donation_id)
    donation.delete()
    messages.success(request, 'Bağış başarıyla silindi.')
    return redirect('create_donation_view')

def feedback(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        feedbackText = request.POST.get('feedbackText')
        
        models.Feedback.create_feedback(user=user, feedbackText=feedbackText)
    
        
        return render(request, 'app/feedback.html')
    return render(request, 'app/feedback.html')

def feedback_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')

        Feedback2.objects.create(
            name=name,
            email=email,
            phone_number=phone_number,
            message=message
        )

        messages.success(request, 'Geri dönüşünüz için teşekkür ederiz!')
        return redirect('index') 

    else:
        return render(request, 'app/feedback2.html')
