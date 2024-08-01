from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Q,Avg
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm,RecipeForm
from .models import Recipe,Rating
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required


def home(request):    
    return render(request , 'home.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        
        form=CreateUserForm() 
        
        if request.method=="POST":
            form=CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username=form.cleaned_data.get('username')
                messages.success(request,"Account was created for " + username)
                return redirect('login')
            
        
        data={'form':form}
        return render(request,'register.html',context=data)


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,"Username OR Password is Incorrect")
            
        return render(request,'login.html')

def logoutpage(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def add_recipe(request):
    form=RecipeForm()
    if request.method=="POST":
        form=RecipeForm(request.POST,request.FILES)
        if form.is_valid():
            recipe=form.save(commit=False)
            recipe.author=request.user
            recipe.save()
            messages.success(request,"Recipe posted Successfully! For more info check ")
            return redirect('add_recipe')
        
    return render(request,'add_recipe.html',{'form':form})  
 
 
@login_required(login_url='login')
def update_recipe(request,pk):
    recp=Recipe.objects.get(id=pk)
    form=RecipeForm(instance=recp)
     
    if request.method=="POST":
        form=RecipeForm(request.POST,request.FILES,instance=recp)
        if form.is_valid():
            form.save()
            return redirect('dashboard_view')

    return render(request,'add_recipe.html',{'form':form})

@login_required(login_url='login')
def delete_recipe(request,pk):
    recp=Recipe.objects.get(id=pk)
     
    if request.method=="POST":
        recp.delete()
        return redirect('dashboard_view')

    return render(request,'delete_recipe.html')
       
@login_required(login_url='login')
def all_recps(request):
    recipe_list=Recipe.objects.all() 
    
    query=request.GET.get("title")
    if query:
        recipe_list=Recipe.objects.filter(Q(title__icontains=query)|Q(description__icontains=query)| Q(category__icontains=query)).distinct()
    
    for recipe in recipe_list:
        average_value = recipe.ratings.aggregate(avg=Avg('rating'))['avg']
        if average_value:
            average_value =round(average_value,1)
        
        recipe.avg=average_value or 0
    paginator = Paginator(recipe_list, 5)  
    page_number = request.GET.get("page")
    recp = paginator.get_page(page_number)
    
    return render(request, "all_recp.html", {"recp": recp})
    

@login_required(login_url='login')
def view_recp(request, pk):
    recipe = get_object_or_404(Recipe, id=pk)
    
    if request.method == 'POST':
        rating_value = request.POST.get('rating')
        if rating_value:
            rating_value = int(rating_value)
            rating, created = Rating.objects.update_or_create(
                recipe=recipe,
                user=request.user,
                defaults={'rating': rating_value}
            )
            return redirect('view_recp', pk=pk)  # Redirect to the same view to update the average rating
    count=recipe.ratings.count()
    average_value = recipe.ratings.aggregate(avg=Avg('rating'))['avg']
    if average_value:
        average_value=round(average_value,1)
    else:
        average_value=0
    data = {'recipe': recipe, 'avg': average_value,'count':count}
    
    return render(request, 'view_recp.html', data)

@login_required(login_url='login')
def dashboard_userrecps(request):
    recipe_list=Recipe.objects.filter(author=request.user)
    query=request.GET.get("title")
    if query:
        recipe_list=Recipe.objects.filter(Q(title__icontains=query)|Q(description__icontains=query)| Q(category__icontains=query)).distinct()
    for recipe in recipe_list:
        average_value = recipe.ratings.aggregate(avg=Avg('rating'))['avg']
        if average_value:
            average_value=round(average_value,1)
        recipe.avg=average_value or 0
    paginator = Paginator(recipe_list, 4)  
    page_number = request.GET.get("page")
    recp = paginator.get_page(page_number)
    
    return render(request, "dashboard_view.html", {"recp": recp})

@login_required(login_url='login')
def dashboard_join(request):

    return render(request,'dashboard_join.html')

