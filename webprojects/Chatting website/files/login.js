
function sumbit() { 
    var errorhandler = document.getElementById("Error")
    var user = document.getElementById("user").value;
    var file = document.getElementById("pfp");
   
    console.log(file.files[0],user,file)
    var formData = new FormData();  
    formData.append("Image",file.files[0])
    
    formData.append("Image",formData);
    request = PostData(`http://127.0.0.1:8000/api/makeuser/${user}/`,'POST',formData)
    if(request == "555") { 
        errorhandler.innerHTML = "Image or User required to make account or User has spaces";
    }
    else if(request=="556") { 
        errorhandler.innerHTML = "User already in use";

    }
    else if (request=='12') { 
            errorhandler.innerHTML='For some reason method is not post';
    }
    else if (request=='212') {
        errorhandler.innerHTML='file size is big';


    }
    else if(request.startsWith('made') ) {
        window.location= "http://127.0.0.1:8000/front/middle/"
        var requestdata = request.split(',')
        console.log(requestdata)
        localStorage.setItem('Token',requestdata[1])
        localStorage.setItem('pfp',requestdata[2])
    }else  { 
        var requestdata = request.split(',')
        console.log(requestdata,request)
        if(request !== ''  || requestdata[1] !== '') { 


        }

}

    //## 555 error means that theres data we need that is not in our request
    //## 12 means that method is not post
    //## 556 mean that user is already available
    //## 212 means that file's size is big
}


document.addEventListener('DOMContentLoaded',function(){ 
    var button = document.getElementById('sumbit');
    button.addEventListener('click', sumbit)
    if(localStorage.length==2) { 
        window.location='http://127.0.0.1:8000/front/middle/'


    }
})