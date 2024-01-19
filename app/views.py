from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Question, Answer, Tag
# Create your views here.

def index(request):

    questions = Question.objects.all().order_by('-updated_at')

    paginator = Paginator(questions, 25)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "questions" : page_obj,
    }

    return render(request, "index.html", context)