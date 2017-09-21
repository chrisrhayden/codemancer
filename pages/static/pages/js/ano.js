'use strict';

function makeAnoWriter() {
    let $ano_row = $('<tr>', {
        'id': 'ano-form-tr',
        'data-state': 'off'
    });

    let $ano_first_td = $('<td>');

    $ano_row.append($ano_first_td);

    let $ano_td = $('<td>');

    let $ano_box = $('#ano-form');

    $ano_td.append($ano_box);

    $ano_row.append($ano_td);

    $('.second-section').append($ano_row);
}


function setAnoWriterListen() {
    $('.line-number').on('click', function() {
        let line_number = $(this).attr('data-line');
        let if_ano_siblings_eq_zero = $(`#line-${line_number}`)
            .prev('.annotation_row').length === 0;

        if (if_ano_siblings_eq_zero) {
            let $ano_row = $('#ano-form-tr');

            $(`#line-${line_number}`).before($ano_row);
        }
    });
}

function makeAnno(annotation, line_number) {
    // part of makeAnoRow()
    // make table sructer
    // add style and attrs
    // add to table with display none

    let $ano_row = $('<tr>', {
        'class': 'annotation_row',
        'data-row': `${line_number}`,
        'data-display': 'hide'
    }).css({
        'color': 'black',
        'background-color': 'white',
        'display': 'none',
        'line-height': '30px',
        'padding': '0.5em'
    });

    // change background to white
    // TODO find a better code highlight
    $(annotation).children('code').css({
        'color': 'black',
        'background-color': 'white'
    });

    // make two spans
    // the - closes the ano
    // the + opens ano writer
    // append both to a <td>
    let spanish = $('<span>').text('-').on('click', function() {
        $ano_row.css({
            'display': 'none'
        });
    });

    let espanol = $('<span>').text('+').on('click', function() {
        setAnoWriterListen();
    });

    // append both <span>'s to a <td>
    let open_close_td = $('<td>').append(spanish, espanol).css({
        'display': 'flex',
        'flex-flow': 'column',
    });

    $ano_row.append(open_close_td);

    // make a <td>
    // add the annotation
    // add above the line user clicks
    let $ano_td = $('<td>');

    $ano_td.html(annotation);

    $ano_row.append($ano_td);

    $(`#line-${line_number}`).before($ano_row);
}

function setAnoClickListen() {
    $('.line-number').on('click', function() {
        let line_number = $(this).attr('data-line');

        $(`tr[data-row=${line_number}]:first,
            tr[data-row=${line_number}] .annotations:first`).css({
            'display': 'table-row'
        });
    });
}

function makeAnoRow() {
    let all_annos = $('.annotations').toArray();
    let ano_count = {};

    for (let i=0;i < all_annos.length;i++) {
        let annotation = all_annos[i];
        let line_number = $(annotation).attr('data-row');

        let $row_line = $(`#line-${line_number}`);

        if (line_number in ano_count) {
            ano_count[line_number] += 1;
        } else {
            ano_count[line_number] = 1;
        }

        $row_line.css({
            'color': 'green'
        });

        let chil = $row_line.children().first().children('span');

        if (chil.length > 0) {
            chil.text(ano_count[line_number]);

        } else {
            let tool_text = $('<span>', {
                'class': 'tooltext'
            }).text(`${ano_count[line_number]}`);

            tool_text.css({
                'display': 'inline-block',
                'position': 'absolute',
                'z-index': '1',
                'visibility': 'hidden',
                'background-color': 'black',
                'color': 'white',
                'width': '20px',
                'padding': '0 0 0 10px',

            });

            $row_line.hover(function() {
                $(tool_text).css({
                    'visibility': 'visible',
                    'opacity': '1'
                });
            }, function() {
                $(tool_text).css({
                    'visibility': 'hidden',
                    'opacity': '1'
                });
            });

            $row_line.children().first().append(tool_text);
        } // the else

        makeAnno(annotation, line_number);
    } // the for loop
}


$(document).ready(function() {
    makeAnoRow();

    setAnoClickListen();

    makeAnoWriter();

    setAnoWriterListen();
});
