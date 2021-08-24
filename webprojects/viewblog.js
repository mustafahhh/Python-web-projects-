var obj = null;
var tox = null;

document.addEventListener("DOMContentLoaded",function() {
var queryString = decodeURIComponent(window.location.search);
queryString = queryString.substring(1);
var queries = queryString.split("&");
var data = queryString.split('=')[1]

tox = PostData('http://127.0.0.1:8000/get/pulldata/','post',data)
tox = JSON.parse(tox)

document.getElementById('date').innerHTML=tox.date;
document.getElementById('title').innerHTML=tox.title;
document.getElementById('content').innerHTML=tox.content;


});