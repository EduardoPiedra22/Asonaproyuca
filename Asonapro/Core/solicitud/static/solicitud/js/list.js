/*Script que funciona para listar las Solicitudes*/

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
            {"data": "position"},
            {"data": "categoria.nombre"},
            {"data": "id_solicitante.full_name"},
            {"data": "fecha_registro"},
            {"data": "estatus"},
            {"data": "descripcion"},
            {"data": "descripcion_motivo"},
            {"data": "id"},
        ],
        columnDefs: [
            {
                targets: [-4],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                   // return row.estado.name
                    if(row.estatus == 'ESPERA') return '<span class="badge badge-danger">En espera</span> ';
                    if(row.estatus == 'APROBADA') return '<span class="badge badge-success">Aprobada</span> ';


                }
                
            },
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) { 
                    var buttons = '<a href="/sold/change/'+row.id+'/" type="button" class="btn btn-primary btn-xs btn-flat"><i class="fas fa-check"></i></a>';
                    buttons += '<a href="/sold/delete/'+row.id+'/" type="button" class="btn btn-danger btn-xs btn-flat "><i class="fas fa-trash-alt"></i></a>';
                    buttons += '<a href="/sold/update/'+row.id+'/" type="button" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });

});