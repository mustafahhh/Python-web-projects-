##IMPORTS
from contextvars import Token
from os import remove
from typing import Text
from asgiref.sync import AsyncToSync
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer
from django.conf import settings
from .helpers import TokenToUser,TokenChecker,roomcheck,dupechecker,adduser,removeuser,UserToImage
from .models import accounts, rooms
import json
from channels.db import database_sync_to_async
from asgiref.sync import AsyncToSync

#Variables
if not settings.configured:
    settings.configure()
    
channel_layer = get_channel_layer()





#Websocket functions class
class Chat(AsyncWebsocketConsumer):


    #Connecting websocket function handler
    async def websocket_connect(self, event):
        #Variables
        self.room = self.scope['url_route']['kwargs']['ID']
        self.Token = self.scope['url_route']['kwargs']['Token']

        #Data in database true and false
        self.rooma = await database_sync_to_async(roomcheck)(self.room)
        self.Tokena = await database_sync_to_async(TokenChecker)(self.Token)



        self.User = await database_sync_to_async(TokenToUser)(self.Token)

        await self.channel_layer.group_add(self.room,self.channel_name)



        await self.accept()
        #Hand shake                                                                                                                             
        #Data in database handler if its not there the disconnect
        if self.rooma == False or self.Tokena == False :
            self.channel_layer.group_discard(self.room, self.channel_name)
            self.close(code=4000)
            raise NameError("Token or room not valid")  # Raise Error
        self.Dupea = await database_sync_to_async(dupechecker)(self.room,self.Token)#Making sure the user did not join the chat twice
        if self.Dupea==1:
            self.channel_layer.group_discard(self.room, self.channel_name)
            self.close(code=4000)
            raise NameError("Duplicated connection")  # Raise Error
        await self.channel_layer.group_send(self.room,  {
                                'type':'UserJoining',
                                'user': self.User
                            }
                        )       

        await database_sync_to_async(adduser)(self.room,self.Token)

    #Here is the disconnecting function handler
    async def websocket_disconnect(self, event):
        room = self.scope['url_route']['kwargs']['ID']
        Token = self.scope['url_route']['kwargs']['Token']
        print(room,Token)
        self.rooma = await database_sync_to_async(roomcheck)(room)
        self.Tokena = await database_sync_to_async(TokenChecker)(Token)
        #Here we discarded user from the group
        
        if self.rooma == False or self.Tokena == False:
            return
        await self.channel_layer.group_discard(room,self.channel_name)

        User = await database_sync_to_async(TokenToUser)(Token)
        await database_sync_to_async(removeuser)(room,Token)#Making sure the user did not join the chat twice
        #Here we send message for the users in websocket|Message is how much users online
        await self.channel_layer.group_send(room,  {
                        'type':'UserLeaving',
                        'user': User,
                    }
                )


    #User joining room chat handler
    async def UserJoining(self,event):
        user = event.get('user', None)
        # Send message to users in the   
        x = '{"name" :' + user +', "event" : "Joining"}'
        await self.send(x)   
    #UserLeavingHandler
    async def UserLeaving(self,event):
        user = event.get('user', None)
        # Send message to users in the   
        x = '{"name" :' + user +', "event" : "Leaving"}'



        await self.send(x)        




    #Message type handler 
    async def UserMessage(self, event):
        Message = event.get('message', None)
        User = event.get('user', None)
        pfp = await database_sync_to_async(UserToImage)(User)
        response = '{"Message" : "' + Message +'", "User" : "' + User +'", "pfp" :"' +str(pfp)+ '","event" :'  + '"message"'  + ' } '

        # Send message to users in the websocket
        await self.send(str(response))  
        print('--------------------------------------------------------------------------------------')

    async def websocket_receive(self,event):
            
        try:
            print(event)
            data = json.loads(event["text"], strict=False)
            print(data)
            if data["message"].isspace():
                return
            
            room = data["room"]
            token = data["token"]
            message = data["message"]
            print(room,token,message)


            rooma = await database_sync_to_async(roomcheck)(room)
            tokena = await database_sync_to_async(TokenChecker)(token)
            print(token,room,message)
            print(tokena,rooma)
            if rooma == True and tokena == True:         
                User = await database_sync_to_async(TokenToUser)(token)
                Message = message
                print(Message)
                await self.channel_layer.group_send(room,  {
                            'type':'UserMessage',
                            'user': User,
                            'message':Message
                        }
                    )
        except Exception as ex : 
            print(ex)

