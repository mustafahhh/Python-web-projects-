function OnLeave() {


    //Define the elements
    var span = document.querySelectorAll("span")
    var body = document.querySelector("#Body")
    var h1 = document.querySelectorAll("h1")
    var button = document.querySelector("#AnalyticsButton")

    //Edit style

    //1-Change background position for the fake body
    body.style.backgroundPosition = '0 100%'

    //2-Change h1 elements font color
    h1.forEach((el) => { 
        el.style.Transition = 'all .40s'
        el.style.color = '#000614'
    })

    //3-Change AnalyticsButton proprties 
    button.style.Transition = 'all .50s'
    button.style.color = '#000614'
    button.style.background = '#000614'
    button.style.border  = '5px solid #000614'
    button.style.boxShadow  = '0 0 0 #a29bfe'
    /*Note:
        We have changed the color for the button and background and border and boxshadow for the button and also the Transition proprties
    */


    //4-Change span proprties

    span.forEach((el) => { 
            el.style.Transition =  'all .50s'
            el.style.background =  "linear-gradient(to right, #000614 50%, #000614 0%)"
            el.style.backgroundClip = 'text'
            el.style.backgroundSize = '200% 100%'
            el.style.backgroundPosition = '100%'
            el.style.webkitTextFillColor = 'transparent'
            el.style.webkitBackgroundClip = 'text'    
    })

    setTimeout(function() {
            window.location.href = 'http://127.0.0.1:8000/stats/charts/'
    },600)

}




document.addEventListener('DOMContentLoaded',function() { 
    var button = document.getElementById("AnalyticsButton")
    button.addEventListener('click',OnLeave)

    var span = document.querySelectorAll('span')
    span.forEach((value) => { 
        if(value.id == 'Level') { 
            value.innerHTML = localStorage.getItem(value.id) +'/2'

        } else{ 
        
        value.innerHTML = localStorage.getItem(value.id)
        
    
    }




    })





})