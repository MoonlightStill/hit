# Create your views here.
from django.shortcuts import render_to_response,get_object_or_404, render
from Library.models import Author,Book
from django.http import HttpResponse, HttpResponseRedirect

#def search(request):
#    pass
#
#
#def delete(request):
#    pass

def index(request):
    booklist = Book.objects.all()
    return render(request, 'index.html',{'book_list':booklist})

def addauthor(request):
    return render(request, 'addauthor.html')
    
def saveauthor(request):
    authorID = request.POST.get('author_ID','')
    name = request.POST.get('author_name','')
    age = request.POST.get('author_age','')
    country = request.POST.get('author_country','')
    newauthor = Author(AuthorID = authorID, Name = name, Age = age, Country \
    = country)
    newauthor.save()
    return HttpResponseRedirect("/")
    
    
def addbook(request):
    
    return render(request, 'addInfo.html')

def savebook(request):
    ISBN = request.POST.get('book_ISBN','')
    title = request.POST.get('book_title','')
    authorID = request.POST.get('book_authorID','')
    publisher = request.POST.get('book_publisher','')
    publishDate = request.POST.get('book_publishDate','')
    price = request.POST.get('book_price','')
    author=Author.objects.filter(AuthorID = authorID)
    
    if(author):
        newbook = Book(ISBN = ISBN,Title = title,AuthorID = author[0],Publisher = \
        publisher,PublishDate = publishDate,Price = price)
        newbook.save() 
        return HttpResponseRedirect("/")
    else:
        return render(request, 'newauthor.html',{'book_isbn':ISBN,'book_title':title, \
        'book_publisher':publisher, 'book_publishDate':publishDate,\
        'book_price':price})
        
def search(request):    
    return render(request, 'search.html')

def showauthor(request):
    name = request.POST.get('author_name','')
    authorID = Author.objects.filter(Name = name)
#    booklist = authorID.book_set.all()
    booklist=[]
    for author in authorID:
        booklist.append(Book.objects.filter(AuthorID=author))
        
    return render(request, 'showauthor.html', {'author_name':name, \
    'book_list':booklist })
    
    
def showbook(request, isbn):
    book = Book.objects.get(ISBN = isbn)
    return render(request, 'showbook.html', {'book':book})
    

def delete(request, isbn):
    deletebook = Book.objects.get(ISBN=isbn)
    deletebook.delete()
    return HttpResponseRedirect("/")

def refresh(request, isbn):
    refreshbook = Book.objects.get(ISBN=isbn)
    return render(request, 'refresh.html',{'book':refreshbook})

def change(request):
    isbn = request.POST.get('book_ISBN','')
    refreshbook = Book.objects.get(ISBN=isbn)
#    title = request.POST.get('book_title','')
    authorID = request.POST.get('book_authorID','')
    publisher = request.POST.get('book_publisher','')
    publishdate = request.POST.get('book_publishDate','')
    price = request.POST.get('book_price','')
    author=Author.objects.get(AuthorID = authorID)

    refreshbook.AuthorID = author
    refreshbook.Publisher = publisher
    refreshbook.PublishDate = publishdate
    refreshbook.Price = price
    refreshbook.save()
    
    return HttpResponseRedirect("/")
    
def saveall(request):
    authorID = request.POST.get('author_ID','')
    name = request.POST.get('author_name','')
    age = request.POST.get('author_age','')
    country = request.POST.get('author_country','')
    newauthor = Author(AuthorID = authorID, Name = name, Age = age, Country \
    = country)
    newauthor.save()
    
    ISBN = request.POST.get('book_ISBN','')
    title = request.POST.get('book_title','')
    publisher = request.POST.get('book_publisher','')
    publishDate = request.POST.get('book_publishDate','')
    price = request.POST.get('book_price','')
#    print price
    newbook = Book(ISBN = ISBN,Title = title,AuthorID = newauthor,Publisher = \
    publisher,PublishDate = publishDate,Price = price)
    newbook.save() 
    return HttpResponseRedirect("/")
    
        
def test(request):
    return render(request, "test.html")
        