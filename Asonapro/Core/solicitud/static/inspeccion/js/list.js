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
            { data: "full_name"},
            { data: "full_name_tecnico"},
            { data: "nombre_unidad"},
            { data: "direccion_unidad"},
            { data: "como_llegar"},
            { data: "estado"},
            { data: "municipio"},
            { data: "parroquia"},
            { data: "vive_en_unidad"},
            { data: "frecuencia_visita"},
            { data: "tenencia_de_tierra"},
            { data: "vivienda"},
            { data: "Opciones"},
        
        ],
        columnDefs: [
            {
                targets: [-5], // Índice de la columna vive_en_unidad
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var checkboxHtml = data ? '<i class="fas fa-check text-success"></i>' : '<i class="fas fa-times text-danger"></i>';
                    return checkboxHtml;
                }
            },
            {
                targets: [-2], // Índice de la columna vivienda
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var checkboxHtml = data ? '<i class="fas fa-check text-success"></i>' : '<i class="fas fa-times text-danger"></i>';
                    return checkboxHtml;
                }
            },

            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/sold/inspeccion/update/' + row.id + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/sold/inspeccion/delete/' + row.id + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    buttons += '<a type="button" class="btn btn-success btn-xs btn-flat" onclick="location.href=\'/sold/generar_pdf/' + row.id + '/\'"><i class="fas fa-check"></i> reporte</a>';

                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});