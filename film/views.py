from django.shortcuts import render
from main.models import Films
from .models import Comments
from .forms import CommentsForm
def film_page(request,film_id):
    film = Films.objects.get(id=film_id)
    user = request.user.username
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            com = Comments(username=request.user,name=film,
                           comment=request.POST['comment'])
            com.save()
    form = CommentsForm()
    comments = Comments.objects.all().filter(name=film).order_by('-id')[:10] 
    context = {'film':film,'user':user,'form':form,'comments':comments}
    return render(request,'film/film_page.html',context)

