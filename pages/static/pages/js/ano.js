'use strict';

function showAnoWiter(line_number, ano_plus=false) {
    let if_ano_siblings_eq_zero = $(`#line-${line_number}`)
        .prev('.annotation_row').length === 0;

    if (if_ano_siblings_eq_zero) {
        let $ano_row = $('#ano-form-tr');

        $(`#line-${line_number}`).before($ano_row);
    } else if (ano_plus) {
        let $ano_row = $('#ano-form-tr');

        $(`#line-${line_number}`).before($ano_row);
    }
}


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

    $('.line-number').on('click', function() {
        let line_number = $(this).attr('data-line');
        showAnoWiter(line_number);
    });
}


function showAnoCode(line_number, select='default') {
    let $first = $(`tr[data-row=${line_number}]:first,
        tr[data-row=${line_number}] .annotations:first`);

    if (select === 'default') {
        $first.css({
            'display': 'table-row'
        });
    } else if (select === 'forward') {
        let next = $first.siblings('.annotations:nth-child(1)');
        next.css({
            'display': 'table-row'
        });
    }
}

function setAnoClickListen() {
    /*$('.line-number').on('click', function() {
        let line_number = $(this).attr('data-line');
        if (select === 'default') {
            $(`tr[data-row=${line_number}]:first,
                tr[data-row=${line_number}] .annotations:first`).css({
                'display': 'table-row'
            });
        }
    });*/

    $('.line-number').on('click', function() {
        let line_number = $(this).attr('data-line');
        showAnoCode(line_number);
    });
}


function makeAnnoCode(annotation, line_number) {
    /* part of makeAnoRow()
       make table sructer
       add style and attrs
       add to table with display none */

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
        showAnoWiter(line_number, true);
    });

    // append both <span>'s to a <td>
    let open_close_td = $('<td>').append(spanish, espanol).css({
        'height': '10em',
        'display': 'flex',
        'flex-flow': 'column',
        'align-items': 'center',
        'justify-content': 'space-between'
    });

    espanol.on('click', function() {
        showAnoWiter('');
    });

    $ano_row.append(open_close_td);

    // make a <td>
    // add the annotation
    // add above the line user clicks
    let $ano_td = $('<td>');

    $ano_td.html(annotation);

    let $forward = $('<span>');

    $forward.on('click', function() {
        showAnoCode(line_number, 'forward');
    }).text('>');

    let $backward = $('<span>');

    $backward.on('click', function() {
        showAnoCode(line_number, 'backward');
    }).text('<');

    let $step_td = $('<td>');
    $step_td.css({
        'height': '10em',
        'display': 'flex',
        'flex-flow': 'column',
        'align-items': 'center',
        'justify-content': 'space-between'
    }).append($forward, $backward);

    // add all <td>'s to table row
    $ano_row.append($ano_td, $step_td);

    $(`#line-${line_number}`).before($ano_row);
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

            // add tool_text to the first child of table row
            $row_line.children().first().append(tool_text);

        } // the if else statement end

        makeAnnoCode(annotation, line_number);
    } // the for loop end
}


$(document).ready(function() {
    makeAnoRow();

    setAnoClickListen();

    makeAnoWriter();
});
