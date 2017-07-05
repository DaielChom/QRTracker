(function(){

  $(".submit").submit((ev)=>{
    ev.preventDefault();
    path = document.URL.substr(22,);

    if (path == 'clientes'){
      id = $('input[name="id_client"]').val();
      $.ajax({
        url:'/clientes',
        data: $('form').serialize(),
        type: 'POST',
        success: function(response) {
          if(response.success==1){
          $("#response_message").addClass("fondo_correcto");
          $("#response_message").removeClass("hidden");
          $("#response_message:last").html(response.message);
          window.location="/clientes";
          }

          if(response.success == 0){
            $("#response_message").addClass("fondo_incorrecto");
            $("#response_message").removeClass("hidden");
            $("#response_message:last").html(response.error_msg).fadeOut(1500);
          }
        },
        error: function(error) {console.log(error);}
      });
    }
    else if(path == 'paquetes'){}
    else if(path == 'funcionarios'){}

  });

})();
