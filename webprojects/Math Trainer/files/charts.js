


document.addEventListener('DOMContentLoaded', function() { 
Body = document.getElementById('FakeBody')
a = document.querySelectorAll('a')

setTimeout(function(){
    Body.style.backgroundPosition='-100%'
    a.forEach((el) => {
        el.style.transition = 'all 0.95s'
        el.style.color = '#dff9fb'
        el.style.background = '#4832b6'
        el.style.borderColor = '#4832b6'

        el.style.boxShadow = "1px 1px 10px #192a56"

    })




},700)
console.log('timeout')
setTimeout(function(){
    console.log('timeout')

    a.forEach((el) => {
        el.style.transition = '0.25s,box-shadow 0.35s,padding .55s'


    })




},1400)



})