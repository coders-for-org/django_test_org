from django.shortcuts import render,redirect
from django.http import HttpResponse
from aboutus.models import Employee, Lyrics
from aboutus.forms import EmployeeForm, LyricsForm

posts = [
  {
    'name': 'ashwin',
    'age' : '20',
    'color' : 'med light skin'
  },
  {
    'name': 'Slomo',
    'age' : '18',
    'color' : 'med light skin'
  }
]

def index(request): 
  context = {
    'posts' : posts
  }
  return render(request , "index.html", context)

def home(request):
  context = {
    'posts' : posts
  }
  return render(request , "blog/home.html", context)

def about(request):
  return render(request , "blog/about.html")

def contact(request):
  return render(request , "blog/contact.html")

def display(request):
  punc_text = (request.GET.get('analyze', 'default'))
  remove_punc = (request.GET.get('removepunc', 'off'))
  print(punc_text)
  print(remove_punc)
  analy = {'remove_punc' : 'Removed Punctuations', 'text_punc' :  punc_text}
  return render(request , "blog/display.html", analy)

def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/emp-show')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'blog/emp.html',{'form':form})  

def emp_show(request):  
    all_emp_data = Employee.objects.all()  
    return render(request,"blog/emp_show.html",{'employees':all_emp_data})  

def emp_edit(request, id): 
  employee = Employee.objects.get(id=id)  
  return render(request,'blog/emp_edit.html', {'employee':employee})

def emp_update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/emp-show")  
    return render(request, 'blog/edit.html', {'employee': employee})  

def emp_destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/emp-show")  

def lyrics(request):  
    if request.method == "POST":  
        form = LyricsForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/lyrics-show')  
            except:  
                pass  
    else:  
        form = LyricsForm()  
    return render(request,'blog/lyrics.html',{'form':form})  

def lyrics_show(request):  
    lyrics_data_all = Lyrics.objects.all()  
    return render(request,"blog/lyrics_show.html",{'lyrics_all':lyrics_data_all})  

def lyrics_edit(request, id): 
  lyrics_edit = Lyrics.objects.get(id=id)  
  return render(request,'blog/lyrics_edit.html', {'lyrics_upd':lyrics_edit})

def lyrics_update(request, id):  
    lyrics_upd = Lyrics.objects.get(id=id)  
    form = LyricsForm(request.POST, instance = lyrics_upd)  
    if form.is_valid():  
        form.save()  
        return redirect("/lyrics-show")  
    return render(request, 'blog/lyrics_edit.html', {'lyrics_upd': lyrics_upd})

def lyrics_destroy(request, id):  
  lyrics_del = Lyrics.objects.get(id=id)  
  lyrics_del.delete()  
  return redirect("/lyrics-show")  
