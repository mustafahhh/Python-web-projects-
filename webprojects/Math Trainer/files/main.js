document.addEventListener('DOMContentLoaded',function(){
    AR = localStorage.getItem('A/R')
if (AR == null){
    localStorage.setItem('TotalAnswers',0)
    localStorage.setItem('TotalRounds',0)
    localStorage.setItem('A/R',0)
    localStorage.setItem('Level',1)   


}
if (AR >= 20 && localStorage.getItem('Level') == 1) { 
    localStorage.setItem('Level',2)
}
else if (AR <= 15 && localStorage.getItem('Level') == 2) { 
        localStorage.setItem('Level',1)
}
})