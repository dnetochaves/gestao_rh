function utilizouHoraExtra(id){
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    $.ajax({
        type: 'POST',
        url: '/horas-extras/utilizou-hora-extra/' + id + '/',
        data: {
            csrfmiddlewaretoken: token
        },
        success: function(result){
            $("#mensagem").text(result.mensagem);
            $("#horas_extras_atualizadas").text(result.horas);
        }
    });
}