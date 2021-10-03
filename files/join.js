function checkroom() { 
    var roomid = document.getElementById('roomid').value;
    response  = PostData(`http://127.0.0.1:8000/api/checkroom/${roomid}/`)
            console.log(response )
                 if (response  == 1) {
                     window.location = `http://127.0.0.1:8000/front/chatroom/${roomid}/`
     
                 } else { 
                     document.getElementById('errorhandler').style.opacity = 1;
                     document.getElementById('errorhandler').style.pointerEvents= 'all';
     
                 }
                 console.log(response ,'dd')
     
     
     
}

document.addEventListener('DOMContentLoaded', function() {  
    imagename = localStorage.getItem('pfp')
    image = document.getElementById('PFP').src =`http://127.0.0.1:8000/files/${imagename}`;
    var button = document.getElementById('sumbit')
    button.addEventListener('click', checkroom)
})