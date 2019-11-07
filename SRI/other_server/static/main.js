var h1 = document.getElementsByTagName("h1")[0];
h1.onclick = function(){
    target = window.event.target;
    target.style.color = 'red';
    function retrieveColor() {
        target.style.color = 'black';
    }
    setTimeout(retrieveColor, 1000);
}