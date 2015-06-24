$(document).ready(function(){
    addRowHandlers();
    
    $(document).click( function(e){

        if ($('#dropdown:visible')) {
            $('#dropdown').hide();
        }

        if(!$(e.target).closest('#modalEditarEmpresa').length) {
            if($('#modalEditarEmpresa').is(":visible")) {
                $('#modalEditarEmpresa').hide()
            }
        }
    });    

});

function addRowHandlers() {
    var table = document.getElementById("tabela");
    var rows = table.getElementsByTagName("tr");

    for (i = 0; i < rows.length; i++) {
        var currentRow = table.rows[i];
        var createClickHandler = 
            function(row) 
            {
                return function(e) { 
                    cells = row.getElementsByTagName("td");
                    ramoAtuacao = cells[0].firstChild;
                    nome = cells[1].firstChild;
                    propostaApoio = cells[2].firstChild;
                    tipoParceria = cells[3].firstChild;
                    background = cells[4].firstChild;
                    iniciativas = cells[5].firstChild;
                    apoios = cells[6].firstChild;
                    /*
                    nao necessarios:
                    eventos = cells[1].firstChild;
                    last_name = cells[2].firstChild;
                    is_active = cells[3].firstChild;
                    is_superuser = cells[4].firstChild;
                    is_staff = cells[5].firstChild;
                    last_login = cells[6].firstChild;
                    groups = cells[7].firstChild;
                    user_permissions = cells[8].firstChild;
                   
                    password = cells[10].firstChild;
                    email = cells[11].firstChild;
                    date_joined = cells[12].firstChild;*/

                    if ($('#dropdown:hidden')) {
                        event.stopPropagation();   
                        setposition(e);     
                        $('#dropdown').toggle();
                    }
                };
            };

        currentRow.onclick = createClickHandler(currentRow);
    }
}

function setposition(e) {
    var bodyOffsets = document.body.getBoundingClientRect();
    tempX = e.pageX - bodyOffsets.left;
    tempY = e.pageY;
  console.log(tempX);

    $("#dropdown").css({ 'top': tempY, 'left': tempX });
}

function showModal(){
    if($('#modalEditarEmpresa:hidden')){
        event.stopPropagation();
        document.getElementById('inputNome').value = nome.textContent;
        document.getElementById('inputRamo').value = ramoAtuacao.textContent;
        document.getElementById('inputBackground').value = background.textContent;
        document.getElementById('inputApoios').value = apoios.textContent;
        document.getElementById('inputProposta').value = nome.textContent;

        $('#modalEditarEmpresa').toggle();
        $('#dropdown').hide();
    }
}