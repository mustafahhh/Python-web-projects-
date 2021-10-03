from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import rooms,accounts

from .helpers import RESIZE,file_size,BasicToken,roomcheck #Importing helpers functions 



from django.utils.crypto import get_random_string
from django.views.decorators.csrf import csrf_exempt









# Create your views here.
def login(request):
    return render(request,'loginpage.html')


def middlewebpage(request):
    return render(request,'middle.html')



def makeroom(request):
    return render(request,'makeroom.html')


def joinroom(request):
    return render(request,'joinroom.html')


def chatroom(request,ID):
    return render(request,'chatroom.html',{'roomid':ID})


#Api


def roomcheckApi(request,room): 
    if roomcheck(room) == True: 
        return HttpResponse('1') 
    if roomcheck(room) == False:
        return HttpResponse('0')   
#this Api makes chatting rooms 
def makeroomApi(request):
    Name = 'dd'
    namegenerated=False

    #Here the ID generated
    while(namegenerated==False) : 
            Name  = get_random_string(length=6)   


            try :
                rooms.objects.get(roomid=Name)
                namegenerated=False                
            except:
                namegenerated=True
                pass

            

    room = rooms(roomid=Name)
    room.save()
    return HttpResponse(Name)


#this Api makes chatting rooms 
@csrf_exempt
def makeAccountApi(request,User):
    print(request.FILES["Image"])

    ## 555 error means that theres data we need that is not in our request
    ## 12 means that method is not post
    ## 556 mean that user is already available
    ## 212 means that file's size is big
    try:
        if  User.isspace() or ' ' in User:
            print(User.isspace())
            print("555")
            return HttpResponse("555")
    except: 
            print("555")
            return HttpResponse("555")

    if request.method == 'POST':
        Image=request.FILES["Image"]
        IMG=RESIZE(Image)
        token=BasicToken()
        if file_size(Image,2) == 1: 
            print('33')
            return HttpResponse("212")

        #Handling if the same user is used by some one 
        try:
            accounts.objects.get(user=User)
            print("user in use")
            return HttpResponse('556')
        except:
            #if the user is not available then save to database
            room = accounts(user=User,image=IMG,token=token)
            room.save()
        print("made")
        return HttpResponse('made ,' +accounts.objects.get(user=User).token + ',' + str(accounts.objects.get(user=User).image))
    else: 
        return HttpResponse("12")