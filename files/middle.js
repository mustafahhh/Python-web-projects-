


document.addEventListener('DOMContentLoaded',function(){ 
var button = document.getElementById('clearlocalstorage')
button.addEventListener('click', function(){
    
    
    localStorage.clear()
    window.location='http://127.0.0.1:8000/front/'

})



})