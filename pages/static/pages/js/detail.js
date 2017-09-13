$(document).ready(function() {
    // for detail only
    'use strict';
    let two_click = 0;
    $('pre').on('click', function() {
        let $chiliins = $(this).children();
        let $code_span = $($chiliins[0]);
        let $code_code = $($chiliins[1]);
        let $line_num = $code_code.attr('data-line');
        if (two_click === 0) {
            $('#id_line_begin').val(Number($line_num));
            two_click = 1;
        } else {
            $('#id_line_end').val(Number($line_num));
        }

        $code_span.css({
            'color': 'green'
        });
    });

});
