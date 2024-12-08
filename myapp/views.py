import calendar
import datetime

from django.core.files.storage import FileSystemStorage
from django.db.models import Sum, Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.

from .models import *

def index(request):
    return render(request,'index.html')

def loginn(request):
    return render(request,'admin/login.html')

def addexpert_trainer(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/'</script>")
    return render(request, 'admin/add expert.html')

def viewexpert_trainer(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/'</script>")
    res =trainer.objects.all()
    return render(request, 'admin/view trainer.html', {'data':res})

def view_expert(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/'</script>")
    res =expert.objects.all()
    return render(request, 'admin/view expert.html', {'data':res})

def add_batch(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/'</script>")
    return render(request,'admin/add batch.html')

def add_event(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/'</script>")
    return render(request,'admin/add event.html')

def view_event(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/'</script>")
    res=event.objects.all()
    return render(request, 'admin/view event.html', {'data': res})

def add_event_post(request):
    eventname=request.POST['textfield']
    description=request.POST['textarea']
    date=request.POST['textfield2']
    i=event.objects.filter(eventname=eventname,description=description,date=date)
    if i.exists():
        return HttpResponse('<script>alert("Already added");window.location="/add_event"</script>')
    else:
        obj = event()
        obj.eventname = eventname
        obj.description = description
        obj.date = date
        obj.save()
        return HttpResponse('<script>alert("Added Sucessfully");window.location="/add_event"</script>')

def delete_event(request,id):
    event.objects.filter(id=id).delete()
    return HttpResponse('<script>alert("Deleted Sucessfully");window.location="/view_event"</script>')

def view_batch(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/'</script>")
    res=batch.objects.all()
    return render(request,'admin/view batch.html',{'data':res})

def view_registered_user(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/'</script>")
    res = user.objects.all()
    return render(request,'admin/view registered user.html',{'data':res})

def allocate_user_to_batch(request,id):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/'</script>")
    res=batch.objects.all()
    return render(request,'admin/allocate user & batch.html',{'data':res,'id':id})

def batch_allocation_to_trainer(request,id):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/'</script>")
    res=batch.objects.all()
    return render(request,'admin/batch allocation to trainer.html',{'data':res,'id':id})

def change_password(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/'</script>")
    return render(request,'admin/change password.html')

def month_wise_report(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/'</script>")
    return render(request,'admin/month wise report.html')

def fee_due(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/'</script>")
    current_day = datetime.datetime.now()
    frst_day = current_day.replace(day=1)
    res = payment.objects.filter(date__lt=frst_day)
    print(res)
    l = []
    for i in res:
        if i.USER.id not in l:
            l.append(i.USER.id)
    ulist = []
    print(l)
    for ik in l:
        print(ik)
        re = user.objects.filter(id=ik)
        for u in re:
            ulist.append({
                "username": u.username,
                "email":u.email,
                "phone":u.phone,
            })
    print(ulist)
    return render(request,'admin/view_fee_due.html')

# def send_alert(request):
#     current_day = datetime.datetime.now()
#     current_month = datetime.datetime.now().month
#     # frst_day = current_day.replace(day=1)
#     # res = payment.objects.filter(date__lt=frst_day)
#     res = payment.objects.filter(date__year=current_day.year, date__month=current_month)
#     print(res)
#     l = []
#     for i in res:
#         if i.USER.id not in l:
#             l.append(i.USER.id)
#     ulist = []
#     print(l)
#     rek = pay_payment_alert.objects.filter(date=datetime.datetime.now().strftime("%Y-%m-%d"))
#     if rek.exists():
#         return HttpResponse('<script>alert("Send Sucessfully");window.location="/admin_home"</script>')
#     for ik in l:
#         print(ik)
#         re = user.objects.filter(id=ik)
#         for u in re:
#             obj=pay_payment_alert()
#             obj.USER_id=u.id
#             obj.notification='Payment Alert'
#             obj.date=datetime.datetime.now().strftime("%Y-%m-%d")
#             obj.save()
#     return HttpResponse('<script>alert("Send Sucessfully");window.location="/admin_home"</script>')






def send_alert(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/'</script>")
    current_day = datetime.datetime.now()
    current_month = current_day.month
    current_year = current_day.year
    # print(current_month,"hhhhhhhhhhhhhhhhh")
    payments_this_month = payment.objects.filter(date__year=current_year, date__month=current_month)
    paid_user_ids = payments_this_month.values_list('USER_id', flat=True)
    print(paid_user_ids)
    all_users = user.objects.all()
    unpaid_users = [u for u in all_users if u.id not in paid_user_ids]

    # Check if payment alerts for today already exist
    c_m=current_day.strftime("%m")
    c_mn=int(current_day.strftime("%m"))
    m_n=calendar.month_name[c_mn]
    alerts_this_month = pay_payment_alert.objects.filter(year=current_year, month=c_m)
    # print(alerts_this_month,"hhhhhhhh")
    if alerts_this_month.exists():
        return HttpResponse(
            '<script>alert("Payment alerts already sent this month");window.location="/admin_home"</script>')

    # Send payment alerts to unpaid users
    for unpaid_user in unpaid_users:
        alert = pay_payment_alert()
        alert.USER = unpaid_user
        alert.notification = 'Pay Your Fee For '+m_n
        alert.date = current_day.strftime("%d")
        alert.month = current_day.strftime("%m")
        alert.year = current_day.strftime("%Y")
        alert.save()

    return render(request, "admin/view_alert_for_user.html", {"unpaid_users": unpaid_users})
















def login_post(request):
    username=request.POST['textfield']
    password=request.POST['textfield2']
    res=login.objects.filter(username=username,password=password)
    if res.exists():
        res=res[0]
        request.session['lid']=res.id
        request.session['head'] = ''
        request.session['log'] = "lo"
        if res.usertype=='admin':
            return redirect('/admin_home')
        if res.usertype == 'trainer':
            return redirect('/trainer_home')
        if res.usertype=='expert':
            return redirect('/expert_home')
        else:
            return HttpResponse('<script>alert("Valid");window.location="/"</script>')
    else:
        return HttpResponse('<script>alert("Invalid");window.location="/"</script>')

def add_batch_post(request):
    batchh=request.POST['textfield']
    b=batch.objects.filter(batchname=batchh)
    if b.exists():
        return HttpResponse('<script>alert("Already existed");window.location="/add_batch#abc"</script>')
    else:
        obj = batch()
        obj.batchname = batchh
        obj.save()
        return HttpResponse('<script>alert("Added Sucessfully");window.location="/add_batch#abc"</script>')

def add_expert_post(request):
    name=request.POST['textfield']
    email = request.POST['textfield2']
    phone = request.POST['textfield3']
    place = request.POST['textfield4']
    post = request.POST['textfield5']
    pin=request.POST['textfield6']
    type=request.POST['select']
    import random
    p=random.randint(0000,9999)
    i=login.objects.filter(username=email)
    if i.exists():
        return HttpResponse('<script>alert("Already existed");window.location="/addexpert_trainer#abc"</script>')
    else:
        if type == 'expert':
            obj = login()
            obj.username = email
            obj.password = p
            obj.usertype = 'expert'
            obj.save()
            objto = expert()
            objto.expertname = name
            objto.email = email
            objto.phone = phone
            objto.place = place
            objto.post = post
            objto.pin = pin
            objto.LOGIN = obj
            objto.save()
            return HttpResponse('<script>alert("Added Sucessfully");window.location="/addexpert_trainer#abc"</script>')
        else:
            obj = login()
            obj.username = email
            obj.password = p
            obj.usertype = 'trainer'
            obj.save()
            objto = trainer()
            objto.trainername = name
            objto.traineremail = email
            objto.phone = phone
            objto.place = place
            objto.post = post
            objto.pin = pin
            objto.LOGIN = obj
            objto.save()
            return HttpResponse('<script>alert("Added Sucessfully");window.location="/addexpert_trainer#abc"</script>')


def change_password_post(request):
    current_password=request.POST['textfield']
    new_password=request.POST['textfield2']
    confirm_password=request.POST['textfield3']
    res = login.objects.filter( password=current_password,usertype='admin')
    if res.exists():
        if new_password==confirm_password:
            login.objects.filter(usertype='admin').update(password=new_password)
            return HttpResponse('<script>alert("Password change sucessfully");window.location="/"</script>')
        else:
            return HttpResponse('<script>alert("Mismatch");window.location="/change_password#abc"</script>')
    else:
        return HttpResponse('<script>alert("Mismatch");window.location="/change_password#abc"</script>')

def monthly_wise_report_post(request):
    month=request.POST['select']
    year = request.POST['select2']
    l=[]
    res = payment.objects.filter(date__month=month, date__year=year).aggregate(total_amount=Sum('amount'))
    total_amount = res.get('total_amount', 0)  # Get the total amount or default to 0 if it doesn't exist
    l.append({
        "data": total_amount
    })
    return render(request, 'admin/month wise report.html',{'data':l})

def view_expert_trainer_post(request):
    type=request.POST['select']

def allocate_user_batch_post(request,id):
    batch_name=request.POST['select']
    u=allocated_user.objects.filter(BATCH_id=batch_name,USER_id=id)
    if u.exists():
        return HttpResponse(
            '<script>alert("Already allocated");window.location="/view_registered_user#abc"</script>')
    else:
        obj = allocated_user()
        obj.USER_id = id
        obj.BATCH_id = batch_name
        obj.save()
        return HttpResponse(
            '<script>alert("Allocated Sucessfully");window.location="/view_registered_user#abc"</script>')


def admin_home(request):
    return render(request,'admin/index.html')

def delete_batch(request,id):
    batch.objects.filter(id=id).delete()
    return HttpResponse('<script>alert("Deleted Sucessfully");window.location="/view_batch#abc"</script>')

def delete_expert(request,id):
    login.objects.filter(id=id).delete()
    return HttpResponse('<script>alert("Deleted Sucessfully");window.location="/view_expert#abc"</script>')

def delete_trainer(request,id):
    trainer.objects.filter(id=id).delete()
    return HttpResponse('<script>alert("Deleted Sucessfully");window.location="/viewexpert_trainer#abc"</script>')

def update_expert(request,id):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/'</script>")
    res=expert.objects.get(id=id)
    return render(request, 'admin/update expert.html', {'data':res,'id':id})

def update_expert_post(request,id):
    name = request.POST['textfield']
    email = request.POST['textfield2']
    phone = request.POST['textfield3']
    place = request.POST['textfield4']
    post = request.POST['textfield5']
    pin = request.POST['textfield6']
    expert.objects.filter(id=id).update(expertname=name, email=email, phone=phone, place=place, post=post, pin=pin)
    return HttpResponse('<script>alert("Updated Sucessfully");window.location="/view_expert#abc"</script>')

def update_trainer(request,id):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/'</script>")
    res = trainer.objects.get(id=id)
    return render(request, 'admin/update trainer.html',{'data':res,'id':id})

def update_trainer_post(request,id):
    name = request.POST['textfield']
    email = request.POST['textfield2']
    phone = request.POST['textfield3']
    place = request.POST['textfield4']
    post = request.POST['textfield5']
    pin = request.POST['textfield6']
    trainer.objects.filter(id=id).update(trainername=name,traineremail=email,phone=phone,place=place,post=post,pin=pin)
    return HttpResponse('<script>alert("Updated Sucessfully");window.location="/viewexpert_trainer#abc"</script>')

def batch_allocation_to_trainer_post(request,id):
    batch_name = request.POST['select']
    t=trainer_allocation.objects.filter(TRAINER_id=id,BATCH_id=batch_name)
    if t.exists():
        return HttpResponse('<script>alert("Already allocated ");window.location="/viewexpert_trainer#abc"</script>')
    else:
        obj = trainer_allocation()
        obj.BATCH_id = batch_name
        obj.TRAINER_id = id
        obj.save()
        return HttpResponse('<script>alert("Allocated Sucessfully");window.location="/viewexpert_trainer#abc"</script>')


#expert


def view_and_update_expert(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/'</script>")
    res=expert.objects.get(LOGIN=request.session['lid'])
    return render(request, 'expert/view_and_update.html',{'data':res})

def add_tips_expert(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/'</script>")
    return render(request, 'expert/add tips.html')

def add_videos_expert(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/'</script>")
    return render(request, 'expert/add video.html')

def view_expert_expert(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/'</script>")
    res = user.objects.all()
    return render(request, 'expert/view user.html', {'data':res})

def view_tips_expert(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/'</script>")
    res = health_tips.objects.filter(EXPERT__LOGIN=request.session['lid'])
    return render(request, 'expert/view tips.html',{'data':res})

def view_videos_expert(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/'</script>")
    res = video.objects.filter(EXPERT__LOGIN=request.session['lid'])
    return render(request, 'expert/view video.html',{'data':res})

def change_password_expert(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/'</script>")
    return render(request, 'expert/change password expert.html')

def expert_home(request):
    return render(request, 'expert/index.html')

def view_and_update_expert_post(request):
    name = request.POST['textfield']
    email = request.POST['textfield2']
    phone = request.POST['textfield3']
    place = request.POST['textfield4']
    post = request.POST['textfield5']
    pin = request.POST['textfield6']
    expert.objects.filter(LOGIN=request.session['lid']).update(expertname=name,email=email,phone=phone,place=place,post=post,pin=pin)
    return HttpResponse('<script>alert("Updated Sucessfully");window.location="/view_and_update_expert"</script>')

def add_videos_post(request):
    videoo=request.FILES['fileField']
    description=request.POST['textarea']
    fs=FileSystemStorage()
    d=datetime.datetime.now().strftime("%Y%m%d")
    fs.save(r"C:\Users\jerin\PycharmProjects\ARCANEXX\myapp\static\video\\"+d+'.mp4',videoo)
    path="/static/video/"+d+'.mp4'
    obj=video()
    obj.video=path
    obj.date=datetime.datetime.now().strftime("%Y-%m-%d")+"  "+datetime.datetime.now().strftime("%H:%M:%S")
    obj.description=description
    obj.EXPERT=expert.objects.get(LOGIN=request.session['lid'])
    obj.save()
    return HttpResponse('<script>alert("Added Sucessfully");window.location="/add_videos_expert"</script>')

def add_tips_post(request):
    tipp=request.POST['textfield']
    description = request.POST['textarea']
    t=health_tips.objects.filter(tip=tipp,description=description,EXPERT=expert.objects.get(LOGIN=request.session['lid']))
    if t.exists():
        return HttpResponse('<script>alert("Already existed");window.location="/add_tips_expert"</script>')
    else:
        obj = health_tips()
        obj.tip = tipp
        obj.description = description
        obj.EXPERT = expert.objects.get(LOGIN=request.session['lid'])
        obj.save()
        return HttpResponse('<script>alert("Added Sucessfully");window.location="/add_tips_expert"</script>')

def change_password_expert_post(request):
    current_password = request.POST['textfield']
    new_password = request.POST['textfield2']
    confirm_password = request.POST['textfield3']
    res = login.objects.filter(password=current_password, id=request.session['lid'])
    if res.exists():
        if new_password == confirm_password:
            login.objects.filter(id=request.session['lid']).update(password=new_password)
            return HttpResponse('<script>alert("Password change sucessfully");window.location="/"</script>')
        else:
            return HttpResponse('<script>alert("Mismatch");window.location="/change_password"</script>')
    else:
        return HttpResponse('<script>alert("Mismatch");window.location="/change_password"</script>')

def delete_video(request,id):
    video.objects.filter(id=id).delete()
    return HttpResponse('<script>alert("Deleted Sucessfully");window.location="/view_videos_expert"</script>')

def delete_health_tips(request,id):
    health_tips.objects.filter(id=id).delete()
    return HttpResponse('<script>alert("Deleted Sucessfully");window.location="/view_tips_expert"</script>')


# trainer


def add_attendance_trainer(request,id):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/'</script>")
    # print("okkkkkk",id)
    return render(request,'trainer/add attendance.html',{"id":id})

def add_attendance_trainer_post(request,id):
    date = request.POST['textfield']
    attendances= request.POST['RadioGroup1']
    BID=request.session['batchid']
    a=attendance.objects.filter(date=date,attendances=attendances,USER=user.objects.get(id=id),TRAINER=trainer.objects.get(LOGIN=request.session['lid']))
    if a.exists():
        return HttpResponse(
            '<script>alert("Already added");window.location="/view_user_trainer/'+str(BID)+'#abc"</script>')
    else:
        obj = attendance()
        obj.date = date
        obj.attendances = attendances
        obj.USER = user.objects.get(id=id)
        obj.TRAINER = trainer.objects.get(LOGIN=request.session['lid'])
        obj.save()
        return HttpResponse(
            '<script>alert("Added Sucessfully");window.location="/view_user_trainer/'+str(BID)+'#abc"</script>')


def update_health_details(request,id):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/'</script>")
    return render(request,"trainer/update_health_details.html",{"id":id})

def update_health_details_post(request,id):
    title = request.POST['textfield']
    des = request.POST['textarea']
    BID = request.session['batchid']
    h=health_details.objects.filter(title=title,description=des,TRAINER = trainer.objects.get(LOGIN=request.session['lid']),USER_id = id)
    if h.exists():
        return HttpResponse('<script>alert("Already existed");window.location="/view_user_trainer/'+str(BID)+'#abc"</script>')
    else:
        obj = health_details()
        obj.title = title
        obj.description = des
        obj.TRAINER = trainer.objects.get(LOGIN=request.session['lid'])
        obj.USER_id = id
        obj.save()
        return HttpResponse('<script>alert("Success");window.location="/view_user_trainer/'+str(BID)+'#abc"</script>')


def change_password_trainer(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/'</script>")
    return render(request, 'trainer/change password trainer.html')

def trainer_home(request):
    return render(request, 'trainer/index.html')

def view_allocated_batch_trainer(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/'</script>")
    res=trainer_allocation.objects.filter(TRAINER__LOGIN_id=request.session['lid'])
    return render(request,'trainer/view allocated batch.html',{'data':res})

def view_update_trainer(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/'</script>")
    res=trainer.objects.get(LOGIN=request.session['lid'])
    return render(request,'trainer/view and update trainer.html',{'data':res})

def view_user_trainer(request,id):
    res=allocated_user.objects.filter(BATCH_id=id)
    request.session['batchid']=id
    return render(request,'trainer/view user.html',{'data':res})

# FEE MANAGEMENT

def add_fee(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/'</script>")
    return render(request,"trainer/add_fee.html")

def add_fee_post(request):
    fees = request.POST['textfield']
    f=fee.objects.filter(fee=fees)
    if f.exists():
        return HttpResponse('<script>alert("Already Added");window.location="/add_fee"</script>')
    else:
        obj = fee()
        obj.fee = fees
        obj.save()
        return HttpResponse('<script>alert("Success");window.location="/add_fee"</script>')


def view_fee(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/'</script>")
    data = fee.objects.all()
    print(data)
    return render(request,"trainer/view_fee.html",{"data":data})

def edit_fee(request,id):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/'</script>")
    data = fee.objects.get(id=id)
    return render(request,"trainer/edit_fee.html",{"data":data,"id":id})

def edit_fee_post(request,id):
    fees = request.POST['textfield']
    fee.objects.filter(id=id).update(fee=fees)
    return HttpResponse('<script>alert("Success");window.location="/view_fee"</script>')

def delete_fee(request,id):
    fee.objects.get(id=id).delete()
    return HttpResponse('<script>alert("Deleted");window.location="/view_fee"</script>')

def change_password_trainer_post(request):
    current_password = request.POST['textfield']
    new_password = request.POST['textfield2']
    confirm_password = request.POST['textfield3']
    res = login.objects.filter(password=current_password, id=request.session['lid'])
    if res.exists():
        if new_password == confirm_password:
            login.objects.filter(id=request.session['lid']).update(password=new_password)
            return HttpResponse('<script>alert("Password change sucessfully");window.location="/change_password_trainer"</script>')
        else:
            return HttpResponse('<script>alert("Mismatch");window.location="/change_password_trainer"</script>')
    else:
        return HttpResponse('<script>alert("Changed Sucessfully");window.location="/change_password_trainer"</script>')

# ==== TRAINER CHAT ===========


def chat(request,id):
    return render(request,"trainer/chat2.html",{"id":id})

def chat_post(request,id):
    chat = request.POST['textfield']
    obj=chat_with_trainer_user()
    obj.date = datetime.datetime.now().date()
    obj.type = 'trainer'
    obj.TRAINER = trainer.objects.get(LOGIN=request.session['lid'])
    obj.USER_id = id
    obj.chat = chat
    obj.save()
    return HttpResponse("ok")






def chatt(request,u):
    # request.session['head']="CHAT"
    request.session['uid'] = u
    print("GGG  ", u)
    return render(request,'trainer/chat.html',{'u':u})


def chatsnd(request):
    d=datetime.datetime.now().strftime("%Y-%m-%d")
    # t=datetime.datetime.now().strftime("%H:%M:%S")
    c = request.session['lid']
    b=request.POST['n']
    print(b)
    m=request.POST['m']
    cc = trainer.objects.get(LOGIN__id=c)
    uu = user.objects.get(id=request.session['uid'])
    print("cccccc",cc)
    print("uuuuuuuuuu",uu)
    obj=chat_with_trainer_user()
    obj.date=d
    obj.type='trainer'
    obj.TRAINER=cc
    obj.USER=uu
    obj.chat=m
    obj.save()
    print(obj)
    v = {}
    if int(obj) > 0:
        v["status"] = "ok"
    else:
        v["status"] = "error"
    r = JsonResponse.encode(v)
    return r
# else:
#     return redirect('/')

def chatrply(request):
    # if request.session['log']=="lo":
    c = request.session['lid']
    rid=request.POST['rid']
    cc=trainer.objects.get(LOGIN__id=c)
    print("JJJJ  ",rid)
    uu=user.objects.get(id=rid)
    print("uuuuuuu",uu)
    res = chat_with_trainer_user.objects.filter(TRAINER=cc,USER=uu)
    print(res)
    v = []
    if len(res) > 0:
        print(len(res))
        for i in res:
            v.append({
                'type':i.type,
                'chat':i.chat,
                'nam':i.USER.username,
                'id':i.USER.id,
                # 'upic':i.USER.photo,
                'dtime':i.date,
                'tname':i.TRAINER.trainername,
            })
        print(v)
        return JsonResponse({"status": "ok", "data": v, "id": cc.id})
    else:
        return JsonResponse({"status": "error"})




# ==== EXPERT CHAT ===========

def expert_chatt(request,u):
    # request.session['head']="CHAT"
    request.session['euid'] = u
    return render(request,'expert/chat.html',{'u':u})


def expert_chatsnd(request):
    d=datetime.datetime.now().strftime("%Y-%m-%d")
    # t=datetime.datetime.now().strftime("%H:%M:%S")
    c = request.session['lid']
    b=request.POST['n']
    print(b)
    m=request.POST['m']
    cc = expert.objects.get(LOGIN__id=c)
    uu = user.objects.get(id=request.session['euid'])
    # uu = user.objects.get(LOGIN=c)
    print("uu:",uu)
    obj=chat_expert_user()
    obj.date=d
    obj.type='expert'
    obj.EXPERT=cc
    obj.USER=uu
    obj.chat=m
    obj.save()
    print(obj)
    v = {}
    if int(obj) > 0:
        v["status"] = "ok"
    else:
        v["status"] = "error"
    r = JsonResponse.encode(v)
    return r
# else:
#     return redirect('/')

def expert_chatrply(request):
    # if request.session['log']=="lo":
    c = request.session['lid']
    cc=expert.objects.get(LOGIN__id=c)
    uu=user.objects.get(id=request.session['euid'])
    # uu=user.objects.get(LOGIN=c)
    # print("uuuuuuuuuu",uu)
    res = chat_expert_user.objects.filter(EXPERT_id=cc,USER=uu)
    print(res)
    v = []
    if len(res) > 0:
        print(len(res))
        for i in res:
            v.append({
                'type':i.type,
                'chat':i.chat,
                'nam':i.USER.username,
                # 'upic':i.USER.photo,
                'dtime':i.date,
                'tname':i.EXPERT.expertname,
            })
        # print(v)
        return JsonResponse({"status": "ok", "data": v, "id": cc.id})
    else:
        return JsonResponse({"status": "error"})

# ==============================================================================================
def blog(request):
    return render(request,'blog.html')

def login_index(request):
    return render(request, 'login index.html')



#User Android


def and_login(request):
    username=request.POST['username']
    password=request.POST['password']
    res=login.objects.filter(username=username,password=password)
    if res.exists():
        res=res[0]
        r=user.objects.get(LOGIN=res.id)
        # print("okkk",r)
        return JsonResponse({"status": "Ok",'lid':res.id,'uid':r.id,'type':res.usertype})
    else:
        return JsonResponse({"status": "Invalid"})

def add_user(request):
    username=request.POST['username']
    email=request.POST['email']
    phone=request.POST['phone']
    place=request.POST['place']
    post=request.POST['post']
    pin=request.POST['pin']
    password=request.POST['password']
    u=login.objects.filter(username=email)
    if u.exists():
        return JsonResponse({"status": "No"})
    else:
        obj = login()
        obj.username = email
        obj.password = password
        obj.usertype = 'user'
        obj.save()
        objto = user()
        objto.username = username
        objto.email = email
        objto.phone = phone
        objto.place = place
        objto.post = post
        objto.pin = pin
        objto.LOGIN = obj
        objto.save()
        return JsonResponse({"status": "ok"})


def change_password_user(request):
    lid = request.POST['lid']
    current_password = request.POST['current_password']
    new_password = request.POST['new_password']
    confirm_password = request.POST['confirm_password']
    res = login.objects.filter(password=current_password, id=lid)
    if res.exists():
        if new_password == confirm_password:
            login.objects.filter(id=lid).update(password=new_password)
            return JsonResponse({"status": "Ok"})
        else:
            return JsonResponse({"status": "Mismatch"})
    else:
        return JsonResponse({"status": "Invalid"})

def and_view_profile(request):
    lid = request.POST['lid']
    res=user.objects.get(LOGIN=lid)
    return JsonResponse({"status": "Ok",'username':res.username,'email':res.email,'phone':res.phone,'place':res.place,'post':res.post,'pin':res.pin})

def and_view_allocate_trainer(request):
    lid=request.POST['lid']
    res=allocated_user.objects.get(USER__LOGIN=lid)
    # print("dataaaaaaaaaaaaa",res)
    re=trainer_allocation.objects.filter(BATCH=res.BATCH.id)
    l=[]
    for i in re:
        l.append({
            'trainername':i.TRAINER.trainername,
            'id':i.TRAINER.id,
            'traineremail':i.TRAINER.traineremail,
            'phone':i.TRAINER.phone,
            'place':i.TRAINER.place,
            'post':i.TRAINER.post,
            'pin':i.TRAINER.pin,

        })
    return JsonResponse({"status": "Ok",'data':l})

def and_view_expert(request):
    lid=request.POST['lid']
    res=expert.objects.all()
    l=[]
    for i in res:
        l.append({
            'id':i.id,
            'expertname':i.expertname,
            'email':i.email,
            'phone':i.phone,
            'place':i.place,
            'post':i.post,
            'pin':i.pin,
        })
    return JsonResponse({"status": "Ok", 'data': l})

def and_health_tips(request):
    eid = request.POST['eid']
    print("eid",eid)
    res=health_tips.objects.filter(EXPERT=eid)
    print("ressssss",res)
    l=[]
    for i in res:
        l.append({
            'id':i.id,
            'tip':i.tip,
            'description':i.description,
        })
    print("dataaaaaaaaaaaa",l)
    return JsonResponse({"status": "Ok", 'data':l})

def and_event(request):
    lid = request.POST['lid']
    res=event.objects.all()
    l=[]
    for i in res:
        l.append({
            'id':i.id,
            'eventname':i.eventname,
            'description':i.description,
            'date':i.date
        })
    return JsonResponse({"status": "Ok", 'data': l})

def and_health_details(request):
    lid=request.POST['lid']
    res = health_details.objects.filter(USER__LOGIN=lid)
    l = []
    for i in res:
        l.append({
            'id':i.id,
            'title': i.title,
            'description': i.description,
        })
    return JsonResponse({"status": "Ok", 'data': l})

def and_attendance(request):
    lid = request.POST['lid']
    res = attendance.objects.filter(USER__LOGIN=lid)
    l = []
    for i in res:
        l.append({
            'id':i.id,
            'date': i.date,
            'attendance': i.attendances,
        })
    return JsonResponse({"status": "Ok", 'data': l})

def and_video(request):
    eid = request.POST['eid']
    res = video.objects.filter(EXPERT_id=eid)
    l = []
    for i in res:
        l.append({
            'id':i.id,
            'video':i.video,
            'description':i.description,
            'date': i.date,
        })
    return JsonResponse({"status": "Ok", 'data': l})

def and_pay_payment_alert(request):
    USER = request.POST['uid']
    res = pay_payment_alert.objects.filter(USER_id=USER)
    l = []
    for i in res:
        l.append({
            'notification':i.notification,
            'date': i.date,
        })
    return JsonResponse({"status": "Ok", 'data': l})

def add_chat(request):
    lid = request.POST['lid']
    toid = request.POST['toid']
    message = request.POST['message']
    d=datetime.datetime.now().strftime("%Y-%m-%d")
    t=datetime.datetime.now().strftime("%H:%m:%d")
    expid = trainer.objects.get(id=toid)
    uid = user.objects.get(LOGIN=lid)
    obj=chat_with_trainer_user()
    obj.date=d
    obj.type='user'
    obj.TRAINER=expid
    obj.USER=uid
    obj.chat=message
    obj.save()
    return JsonResponse({'status':"Inserted"})



def view_chat(request):
    lid = request.POST['lid']
    toid = request.POST['toid']
    lastid = request.POST['lastid']
    # print(lid,toid,lastid)
    # res=chat_with_trainer_user.objects.filter(USER=user.objects.get(LOGIN=lid))
    res=chat_with_trainer_user.objects.filter(Q(USER=user.objects.get(LOGIN=lid)),Q(id__gt=lastid))
    # print(res)
    ar=[]
    for i in res:
        ar.append({
            "id":i.id,
            "date":i.date,
            "userid":i.USER.id,
            "sid":i.type,
            "chat":i.chat,
        })
    # print(ar,"arrrrrrrrrrr")
    return JsonResponse({'status':"ok",'data':ar})


def expert_add_chat(request):
    lid = request.POST['lid']
    print("lid:",lid)

    toid = request.POST['toid']
    print("toid:", toid)
    message = request.POST['message']
    d = datetime.datetime.now().strftime("%Y-%m-%d")
    t = datetime.datetime.now().strftime("%H:%m:%d")
    expid = expert.objects.get(id=toid)
    uid = user.objects.get(LOGIN=lid)
    print("expid:", expid)
    print("uid:", uid)
    obj = chat_expert_user()
    obj.date = d
    obj.type = 'user'
    obj.EXPERT = expert.objects.get(id=toid)
    obj.USER = uid
    obj.chat = message
    obj.save()
    return JsonResponse({'status': "Inserted"})


def expert_view_chat(request):
    lid = request.POST['lid']
    toid = request.POST['toid']
    lastid = request.POST['lastid']
    # print(lid, toid, lastid)
    # res = chat_expert_user.objects.filter(USER=user.objects.get(LOGIN=lid))
    res = chat_expert_user.objects.filter(Q(USER=user.objects.get(LOGIN=lid)), Q(id__gt=lastid))
    # print(res)
    ar = []
    for i in res:
        ar.append({
            "id": i.id,
            "date": i.date,
            "userid": i.USER.id,
            "sid": i.type,
            "chat": i.chat,
        })
    # print(ar, "arrrrrrrrrrr")
    return JsonResponse({"status":"ok","data":ar})


def android_view_payment_alerts(request):
    lid = request.POST['lid']
    res = pay_payment_alert.objects.filter(USER__LOGIN=lid)
    ar = []
    for i in res:
        ar.append(
            {
                "id":i.id,
                "notification":i.notification,
                "date":i.date
            }
        )
    return JsonResponse({"status":"ok","data":ar})


def and_view_fee(request):
    lid=request.POST['lid']
    res = fee.objects.all()
    ar = []

    for i in res:
        # Check if the fee ID exists in the Payment table for the logged-in user
        fee_exists_in_payment = payment.objects.filter(USER__LOGIN=lid, FEE_id=i.id).exists()

        if fee_exists_in_payment:
            ar.append({
                "id": i.id,
                "fee": i.fee,
                "status": "completed"
            })
        else:
            ar.append({
                "id": i.id,
                "fee": i.fee,
                "status": "not completed"
            })

    return JsonResponse({"status": "ok", "data": ar})


def android_online_payment(request):
    lid = request.POST['lid']
    fid = request.POST['fid']
    amount = request.POST['amount']
    mode = request.POST['mode']
    obj = payment()
    obj.USER = user.objects.get(LOGIN=lid)
    obj.FEE_id = fid
    obj.date = datetime.datetime.now().date()
    obj.month = datetime.datetime.now().month
    obj.amount = amount
    obj.payment_status = mode
    obj.save()
    return JsonResponse({"status":"ok"})



def logout(request):
    request.session['log']=""
    request.session.clear()
    return HttpResponse("<script>alert('logout succesfully');window.location='/'</script>")