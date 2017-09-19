'use strict';

function makeAnno(annotation, line_number) {

    let $ano_row = $('<tr>', {
        'class': 'annotation_row',
        'id': `ano-line-${line_number}`,
        'data-display': 'hide'
    }).css({
        'display': 'none'
    });

    let spanish = $('<span>').text('-');

    let new_td = $('<td>').append('x', spanish);

    $ano_row.append(new_td);

    let $ano_td = $('<td>');

    $ano_td.html(annotation);

    $ano_row.append($ano_td);

    $(`#row-${line_number}`).before($ano_row);

}

function showAnnoCount() {
    let all_annos = $('.annotations').toArray();
    let ano_count = {};

    for (let i=0;i < all_annos.length;i++) {
        let annotation = all_annos[i];
        let line_number = all_annos[i].getAttribute('id').slice(4);

        let $row_line = $(`#line-${line_number}`);

        if (line_number in ano_count) {
            ano_count[line_number] += 1;
        } else {
            ano_count[line_number] = 1;
        }

        $row_line.css({
            'color': 'green'
        });

        let chil = $row_line.children('span');
        if (chil.length > 0) {
            chil.text(ano_count[line_number]);
        } else {

            let tool_text = $('<span>', {
                'class': 'tooltext'
            }).text(`${ano_count[line_number]}`);

            $row_line.append(tool_text);

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
        } // the else

        makeAnno(annotation, line_number);
    } // the for loop

}

function setClickListen() {
    $('.line-number').on('click', function() {

        let line_number = $(this).attr('id').slice(5);

        $(`.annotations, #ano-line-${line_number}`).css({
            'display': 'table-row'
        });
    });
}

$(document).ready(function() {
    showAnnoCount();

    setClickListen();
});
