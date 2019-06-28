from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Book, Review
# Create your views here.

# show all
def index(request):
    context = {
        # in real life, this is a query for User.object.get(id=reqsession..
        "user": User.objects.first(),
        "all_books": Book.objects.all(),
        "recent_reviews": Review.objects.order_by("-created_at")[:3],
        "other_books": Review.objects.order_by("-created_at")[3:]
    }

    return render(request, "main/index.html", context)

# show one (shows a book detail page)
def show(request, book_id):

    # do i need data in my template?
    context = {
        "book": Book.objects.get(id = book_id)
    }
    return render(request, "main/show.html", context)

# create (creates book, redirects)
def create(request):
    # # we dont want unauthorized users here!
    # if not "user_id" in request.session:
    #     return redirect('/')
    # if request.method == "POST":
    Book.objects.create(title=request.POST["title"])
    return redirect("/")

# edit one (show an edit form)
def edit(request, book_id):

    # do i need data in my template?
    context = {
        "book": Book.objects.get(id = book_id)
    }
    return render(request, "main/edit.html", context)

# update one (update the book with id to values sent in form, redirect)
def update(request, book_id):

    # do i need data in my template?
    print(request.POST["title"]) # 'Lord of the Rings'
    book_to_update = Book.objects.get(id=book_id)

    print(book_to_update.title)  # 'The Hobbit'

    book_to_update.title = request.POST["title"]
    book_to_update.save()

    print(book_to_update.title)  # 'Lord of the Rings'
    return redirect("/")

# delete one (query for book with book_id, delete it, redriect)
def delete(request, book_id):
    book_to_delete = Book.objects.get(id=book_id)
    book_to_delete.delete()
    return redirect("/")

def home(request):
    msgz = messages.get_messages(request)


    return render(request, "main/validations.html")

def register(request):
    messages.error(request, "First Name is dumb", extra_tags="first_name")
    messages.error(request, "Email's L O L", extra_tags="email")
    messages.error(request, "Pick a better password", extra_tags="password")
    messages.error(request, "Last name is required", extra_tags="last_name")
    return redirect("/home")

def login(request):
    messages.error(request, "Invalid Email/Password")
    return redirect("/home")