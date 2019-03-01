from django.shortcuts import render,redirect
import bcrypt
from .models import *
from django.contrib import messages

def index(request):
    return render(request,"login/indexlogin.html")
def signup(request):
    return render(request,"login/register.html")
def registor(request):
    print(request.POST)
    errors = register.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/Signup')
    else:
        if request.method=="POST":
            if register.objects.filter(email=request.POST['email']):
                messages.error(request, "email already exists.")
                return redirect('/Signup')
            else:
                hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
                one=register.objects.create(user_name=request.POST['user_name'],phone_number=request.POST['phone_number'],catergory=request.POST['catergory'],email=request.POST['email'],password=hash1)
                # print(one)
                request.session['id']=one.id
                return redirect('/homepage')

def loginaccount(request):
    if not register.objects.filter(email=request.POST['email']):
        messages.error(request, "email no exist.")
        return redirect('/')
    else:
        user = register.objects.get(email=request.POST['email'])
        if bcrypt.checkpw(request.POST['password'].encode(),user.password.encode()):
            request.session['id']=user.id
            return redirect('/homepage')
        else:
            messages.error(request, "password failed.")
            print("failed password")
            return redirect('/')
    
def logout(request):
    try:
        del request.session['id']
    except:
        print("thgffghjknnbbg")
    return redirect('/')

def homepage(request):
    user = register.objects.get(id=request.session['id'])
    print('-----------')
    print(user.teacher.count())
    context = {
        "one": user,
        # 'two': User.objects.get(id=comment_id)
        "all_posts": Posts.objects.all(),
        "all_comments": Comments.objects.all(),
        "all_students": register.objects.exclude(catergory="teacher"),
        }
    print(user.__dict__)
    return render(request,"login/Dashboard.html", context)

def post(request):
    errors = Posts.objects.post_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/homepage')
    else:
        user=register.objects.get(id=request.session['id'])
        new_post= Posts.objects.create(teacher=user,main_post=request.POST['post'])
        # request.session['post.id']=new_post.id
        return redirect('/homepage')
   

def editaccount(request,id):
    context={
        "user": register.objects.get(id=request.session['id']),
        }
    return render(request,'login/editaccount.html', context)

def editmyaccount(request,id):
    errors = register.objects.account_validator(request.POST)
    if len(errors)>0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect('/edit/'+id)
    else:
        c = register.objects.get(id=id)
        c.user_name = request.POST['user_name']
        c.phone_number = request.POST['phone_number']
        c.email = request.POST['email']
        c.save()
        return redirect('/myaccount/'+id)

def viewmyaccount(request,id):
    context={
        "acc": register.objects.get(id=id),
        "comments": Comments.objects.filter(students= register.objects.get(id=id))
        # "posts": Posts.objects.filter(comments=comments)
    }
    return render(request,'login/myaccount.html', context)
def post_a_comment(request):
    post= Posts.objects.get(id=request.POST['hiddenpostid'])
    user=register.objects.get(id=request.session['id'])
    new_comment= Comments.objects.create(comment=request.POST['comment'],students=user,post=post)

    return redirect('/homepage')
def delete(request,id):
    del_post=Posts.objects.get(id=id)
    del_post.delete()
    return redirect('/homepage')
def rightanswer(request,id):
    comment= Comments.objects.get(id=id)
    comment.result = 'right'
    comment.save()
    right_student = register.objects.get(student=comment)
    print(right_student)
    right_student.score = right_student.score + 1
    right_student.save()
    return redirect('/homepage')
def viewthisacc(request,id, id2):
    new_note= Notes.objects.filter(student= register.objects.get(id=id2))
    print(new_note)
    context={
        "main_acc": register.objects.get(id= id),
        "user": register.objects.get(id=id2),
        "comments": Comments.objects.filter(students=register.objects.get(id=id2)),
        "notes": new_note,
    }
    return render(request,"login/thisaccount.html", context)

def wronganswer(request,id):
    comment= Comments.objects.get(id=id)
    comment.result = 'wrong'
    comment.save()
    return redirect('/homepage')

def notes(request,id, id2):
    teacher= register.objects.get(id=id)
    student= register.objects.get(id=id2)
    note= Notes.objects.create(student= student, teacher=teacher, notes=request.POST['notes'])
    # print(note.notes)

    return redirect('/viewthisacc/' +id +'/' + id2)

# def editpost(request,id):
#     c = Posts.objects.get(id=id)
#     c.main_post = request.POST['main_post']
#     c.save()
#     return redirect('/homepage')