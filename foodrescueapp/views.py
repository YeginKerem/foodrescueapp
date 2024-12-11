from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, logout
from django.contrib import messages
from foodrescue import models


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
def create_donation_view(request):
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
    donations = models.DonateOperations.get_current_donations()
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




