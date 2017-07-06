(function(){

  $(".submit").submit((ev)=>{
    ev.preventDefault();
    path = document.URL.substr(22,);

    $.ajax({
      url: '/'+path,
      data: $('form').serialize(),
      type: 'POST',
      success: function(response) {
        if(response.success==1){
        $("#response_message").addClass("fondo_correcto");
        $("#response_message").removeClass("hidden");
        $("#response_message:last").html(response.message);
        window.setTimeout(function(){window.location='/'+path;}, 1000);

        }
        if(response.success == 0){
          $("#response_message").addClass("fondo_incorrecto");
          $("#response_message").removeClass("hidden");
          $("#response_message:last").html(response.error_msg).fadeOut(1500);
          }
        },
      error: function(error) {console.log(error);}
      });


  });

})();
