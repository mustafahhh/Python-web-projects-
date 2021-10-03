function makeroom() {
    roomid = PostData("http://127.0.0.1:8000/api/makeroom/")
    window.location.replace(`http://127.0.0.1:8000/front/chatroom/${roomid}/`); 
}
document.addEventListener('DOMContentLoaded', function(){

    imagename = localStorage.getItem('pfp')
    image = document.getElementById('PFP').src =`http://127.0.0.1:8000/files/${imagename}`;




    button=document.getElementById('makeroom')
    button.addEventListener('onclick',makeroom)

})