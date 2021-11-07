document.addEventListener('DOMContentLoaded',function(){ 
    //1-Read data
    TotalAnswers = localStorage.getItem('TotalAnswers')
    TotalRounds = localStorage.getItem('TotalRounds')
    AR = localStorage.getItem('AR')
    //2-Write data
    document.getElementById('TotalAnswers').innerHTML = TotalAnswers
    document.getElementById('TotalRounds').innerHTML = TotalRounds
    document.getElementById('AR').innerHTML = AR 
    //We are done 



})