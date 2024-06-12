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
            { data: 'position'},
            { data: 'full_name'},
            { data: 'cedula'},
            { data: 'nombre_persona_atendio'},
            { data: 'fecha_visita'},
            { data: 'fecha_proxima_visita'},
            { data: 'motivo_visita'},
            { data: 'lote1'},
            { data: 'lote2'},
            { data: 'lote3'},
            { data: 'lote4'},
            { data: 'edad_cultivo'},
            { data: 'superficie_up'},
            { data: 'superficie_preparada'},
            { data: 'superficie_sembrada'},
            { data: 'rubro_sembrado'},
            { data: 'semilla_variedad'},
            { data: 'realizar_recomendacion'},
            { data: 'fecha_estimada_cosecha'},
            { data: 'superficie_por_consechar'},
            { data: 'superficie_cosechada'},
            { data: 'superficie_perdida'},
            { data: 'superficie_efectiva'},
            { data: 'estimacion_del_redimiento'},
            { data: 'redimiento'},
            { data: 'redimiento_total'},
            { data: 'dar_continuidad'},
            { data: 'descripcion'},
            { data: 'coordenadas_norte'},
            { data: 'coordenadas_sur'},
            { data: 'tecnico_name'},
            { data: 'Opciones'},
        
        ],
        columnDefs: [

            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/sold/seguimientos/update/' + row.id + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/sold/seguimientos/delete/' + row.id + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    buttons += '<a type="button" class="btn btn-success btn-xs btn-flat" onclick="location.href=\'/sold/generarpdf/' + row.seguimiento_id + '/\'"><i class="fas fa-check"></i> reporte</a>';

                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});