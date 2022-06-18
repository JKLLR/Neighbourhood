$(document).ready(function(){
    $('form').submit(function(event){
      event.preventDefault()
    }) // End of submit event
  
  }) 

/*LOGIN/SIGNUP ANIMATION */
$(document).ready(function(){
  $('.signupbox').css('transform', 'translateX(80%)');
  $('.signinbox').css('transform', 'translateX(0%)');
 });