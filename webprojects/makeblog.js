
var posting= function(){
var title = document.getElementById('title').value
var content = document.getElementById('content').value

var data= JSON.stringify({'title': title,'content': content});
console.log(data)
tox=PostData('http://127.0.0.1:8000/get/make/','post',data)
if(JSON.parse(tox).message == '409'){
document.getElementById('errorsign').style.opacity= 1;
console.log('error')
} else{

window.location = `viewblog.html?blogid=${JSON.parse(tox).message}`;

}


}

var tox=null
document.addEventListener("DOMContentLoaded",function() {
tox = PostData('http://127.0.0.1:8000/get/date/','get')
document.getElementById('date').innerHTML=tox;
});

