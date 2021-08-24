    function function1(value,ID) {
    console.log(value);
      var ul = document.getElementById("list");
      var l = document.createElement("li");
      var li = document.createElement("a");
      li.innerHTML=ID;
      l.appendChild(li)
      ul.appendChild(l);
      li.setAttribute("href", `viewblog.html?blogid=${value}`);
      li.setAttribute('class','eles')
      };

  var tox = null
    document.addEventListener("DOMContentLoaded",function() {
        tox = PostData('http://127.0.0.1:8000/get/','get')
        obj = JSON.parse(tox);
        IDs = obj.ids
        IDs.forEach(value => function1(value,obj.titles[value-1]));
        document.getElementById('blognumber').innerHTML= `currently ${IDs.length} blogs`;
    });