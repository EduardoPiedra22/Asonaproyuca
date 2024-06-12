
$(function () {
    $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {data: "position"},
            {"data": "id"},
            {"data": "username"}, 
            {"data": "cedula"},
            {"data": "cedula_agraria"},
            {"data": "codigo_asonaproyuca"},
            {"data": "full_name"},  
            {"data": "email"},
            {data: "Opciones"},
        ],
        columnDefs: [

            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var url = "/sold/inspeccion/add/";
                    var buttons = '<a href="/user/update/' + row.id + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/user/delete/' + row.id + '/" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    buttons += '<a href="' + url + '" class="btn btn-success btn-xs btn-flat"><i class="fas fa-check"></i> Inspección</a>';
                    buttons += '<button type="button" class="btn btn-success btn-xs btn-flat" onclick="location.href=\'/sold/generar_pdf/' + row.id + '/\'"><i class="fas fa-check"></i> reporte</button>';
                    buttons += '<a href="/sold/seguimientos/add/" class="btn btn-info btn-xs btn-flat"><i class="fas fa-plus"></i> Crear Seguimiento</a>';

                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});
