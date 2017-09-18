'use strict';

function showAnnos() {
    let all_annos = $('.annotations').toArray();
    let line_nums = {};

    for (let i=0;i < all_annos.length;i++) {
        let line = all_annos[i].getAttribute('id');

        let $ano_line = $(`#ano-${line}`);

        if (line in line_nums) {
            line_nums[line] += 1;
        } else {
            line_nums[line] = 1;
        }

        $ano_line.css({
            'color': 'green'
        });


        let chil = $ano_line.children('span');
        if (chil.length > 0) {
            chil.text(line_nums[line]);
        } else {

            let tool_text = $('<span>', {
                'class': 'tooltext'
            }).text(`${line_nums[line]}`);

            $ano_line.append(tool_text);

            tool_text.css({
                'display': 'inline-block',
                'position': 'absolute',
                'z-index': '1',
                'visibility': 'hidden',
                'background-color': 'black',
                'color': 'white',
                'width': '20px',
                'padding': '0 0 0 5px',

            });

            $ano_line.hover(function() {
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
    } // the for loop
}

$(document).ready(function() {
    showAnnos();
});
