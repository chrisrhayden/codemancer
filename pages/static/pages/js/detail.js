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
    $('.ano-submit').on('click', function(evt) {
        evt.preventDefault();
        let url = '/api/v1/anos/';
        let code = $('#id_code').val();
        let line_begin = $('#id_line_begin').val();
        let line_end = $('#id_line_end').val();
        let snip = $('.code-snip').attr('data-pk');
        let form_data = {
            'code': code,
            'line_begin': line_begin,
            'line_end': line_end,
            'snippet': snip
        };
        let myHeader = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        };
        let myInit = {
            method: 'POST',
            body: JSON.stringify(form_data),
            headers: myHeader,
        };
        fetch(url, myInit);
    });

});
