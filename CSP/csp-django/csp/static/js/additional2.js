console.log('This code executed from external script: additional2.js.');

setTimeout(function(){
   var paragraph = document.getElementById('main-paragraph');
   paragraph.style.background = 'red';
}, 1000);

