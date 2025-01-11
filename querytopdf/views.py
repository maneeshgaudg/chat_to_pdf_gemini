from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from .task import app_chat
# Create your views here.

c = app_chat()

def chat_pdf(request):
   
   if request.method == "GET":
        return render(request, "chat_pdf.html")


   question = request.POST.get("prompt_query", "")
   if question == "":
      return HttpResponse("Please provide promt")
   result =  c.get_answer(question)
   return_dict = {
      "message_code": 200,
      "message": result
   }
   return JsonResponse(return_dict, safe=True)