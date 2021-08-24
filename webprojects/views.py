from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Blog as blog
import json
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    x=blog.objects.last().id
    response=[]
    ids=[]
    for i in range(1,x+1):
       response.append(blog.objects.get(pk=i).title)
       ids.append(i)
    responsedata= {
        'titles' : response,
        'ids':ids ,
        }
    return JsonResponse(responsedata)
@csrf_exempt
def datapull(request):
    if request.method=='POST':
        requestbody = request.body.decode('utf-8').replace("'", '"')
        responsedata=blog.objects.get(pk=requestbody)
        responsecontent = {
            'title': responsedata.title,
            'content' : responsedata.content,
            'date' : str(responsedata.date.year) + "/" + str(responsedata.date.month) + "/" + str(responsedata.date.day)

        }
        return JsonResponse(responsecontent)
    else:
        return HttpResponse('error')

@csrf_exempt
def make(request):
    if request.method=='POST':

        requestbody=request.body.decode('utf-8').replace("'",'"')
        print(requestbody)
        data=json.loads(requestbody)
        print(request.body)

        #errors handling
        try:
            if not data["title"] or not data["content"]or data["title"]==None or data["content"] == None or data["title"].isspace() or data["content"].isspace():
                print('x')
                response= {
                        'message':'409'
                    }
                #409 means that theres loss in data
                return JsonResponse(response)
        except:
                response= {
                        'message':'409'
                    }
                #409 means that theres loss in data
                return JsonResponse(response)
        try:
            print(blog.objects.get(title=data['title']) and blog.objects.get(content=data['content']))
            response = {
                'message': '409'
            }
            # 409 means that theres loss in data
            return JsonResponse(response)
        except:
            pass
        #############################################
        theblog = blog(title=data["title"],content=data["content"])
        theblog.save()
        responsedata= {
        'message' : theblog.pk,
        }
        return JsonResponse(responsedata)
    else:
        response= {
                'message':'566'
            }
        #566 means wrong request method 
        return JsonResponse(response)
@csrf_exempt
def date(request):
    return HttpResponse(str(timezone.now().year) + "/" + str(timezone.now().month) + "/" + str(timezone.now().day))
