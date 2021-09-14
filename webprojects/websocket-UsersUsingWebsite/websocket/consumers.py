##IMPORTS
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer

#Variables
channel_layer = get_channel_layer()
online=0




#Websocket functions class
class OnlineUsers(AsyncWebsocketConsumer):


    #Connecting websocket function handler
    async def websocket_connect(self, event):
        await self.channel_layer.group_add('online',self.channel_name)
        #Here we adding user to websocket group


        #here we add new user online
        global online   
        online+=1


        #here we send message to users|content is how much users online
        await self.channel_layer.group_send('online',  {
                        'type':'OnlineUsersCounter',
                        'users': online
                    }
                )

        await self.accept()
        #Hand shake



    #Here is the disconnecting function handler
    async def websocket_disconnect(self, event):
        await self.channel_layer.group_discard('online',self.channel_name)
        #Here we discarded user from the group
        
        #Here we substract online users 
        global online
        online-=1



        #Here we send message for the users in websocket|Message is how much users online
        await self.channel_layer.group_send('online',  {
                        'type':'OnlineUsersCounter',
                        'users': online 
                    }
                )


    #Message type handler 
    async def OnlineUsersCounter(self, event):
        print('\n',event)
        response = event.get('users', None)
        print(response)



        # Send message to users in the websocket
        await self.send( str(response))         
