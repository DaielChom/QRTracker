(function(){

  $("#enviar").on('click',(ev)=>{
    path = document.URL.substr(22, );

    if (path == 'clientes'){
      id = $('input[name="id_client"]').val()
    }
    else if(path == 'paquetes'){}
    else if(path == 'funcionarios'){}
  });

})();
