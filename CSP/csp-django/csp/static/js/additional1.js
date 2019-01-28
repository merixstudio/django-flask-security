console.log('This code executed from external script: additional1.js.');

setTimeout(function(){
   var paragraph = document.getElementById('main-paragraph');
   paragraph.style.background = 'blue';
}, 1000);

