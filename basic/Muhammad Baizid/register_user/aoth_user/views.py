from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
import re
from  datetime import datetime, timedelta
from django.core.signing import Signer 
import random
from django.core.mail import send_mail
from register_user.models import Users
from django.utils.html import format_html




def registration_done(request):
 if request.method =='POST':
    Name = request.POST.get('Name')
    Email = request.POST.get('Email')
    password = request.POST.get('password')
    con_pw = request.POST.get('con_pw')
    Phone = request.POST.get('Phone')
    email_reg= r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if(Name=='' or Email=='' or password=='' or con_pw=='' or Phone==''):
      messages.error(request, "your fild can not be empty")
      return redirect('reg')
    else:
       if(len(Name)<3):
        messages.error(request,'the name length must be minium 3 ')
        return redirect('reg')
       elif not re.match(email_reg, Email):
         messages.error(request,'please provide approprite Email ')
         return redirect('reg')
       elif(password != con_pw):
         messages.error(request,'Password dose not match ')
         return redirect('reg')
       elif(len(Phone)!=11):
          messages.error(request,'please provide approprite Phone number')
          return redirect('reg')
       else:
         time = datetime.now().strftime( "%H:%M:%S")
         hoer,m,s= map(int,time.split(":"))
         print( hoer,m,s)
         total_s= hoer*60**2+m*60+s
         random_number = random.choices('1234567890',k=4)
         random_number = ''.join(random_number)
         v_code = str(total_s) + random_number
         signer = Signer()
         encrypted_value = signer . sign(v_code).split(':')[1]
         subject = 'Verify your accound'
         message = 'Could you please check the verification code'+ encrypted_value
         from_mail = "muhammadbaizid9758@gmail.com"
         format_link = format_html('link')
         name = ""
         recipient_list = ['muhammadbaizid110@gmail.com',Email]
         send_mail(subject, format_link, from_mail, recipient_list ,html_message=format_link)
         link = f"<p>Congratulations Mr {name} ! For registering as a user in our system. To confirm the registration </p><a href='http://127.0.0.1:8000/aoth/Users/email_verification/"+encrypted_value+"' target='_blank'>please click this Activation link</a>"
         Users_obj = Users()
         Users_obj.name = name
         Users_obj.email = Email
         Users_obj.pw = password
         Users_obj.Phone_number = Phone
         Users_obj.v_code = encrypted_value
         Users_obj.v_statas = 0
         Users_obj.save()

         return redirect('reg')
 else:
    return HttpResponse('this is not a post method')
 
def reg(request):
  return render(request,'user.html')

def verification(request,id):
  return HttpResponse("id")



 