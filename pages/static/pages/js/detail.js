$(document).ready(function() {
    // for detail only
    'use strict';
    let two_click = 0;
    $('.line-number').on('click', function() {
        let line_num = $(this).text();
        if (two_click === 0) {
            $('#id_line_begin').val(Number(line_num));
            two_click = 1;
        } else {
            $('#id_line_end').val(Number(line_num));
        }
    });
    $('.ano-submit').on('click', function(evt) {
        evt.preventDefault();
        let url = '/api/v1/anos/';
        let $code = $('#id_code');
        let $line_begin = $('#id_line_begin');
        let $line_end = $('#id_line_end');
        let snip = $('.code-snip').attr('data-pk');

        let form_data = {
            'code': $code.val(),
            'line_begin': $line_begin.val(),
            'line_end': $line_end.val(),
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

        fetch(url, myInit).then(function(response) {
            $code.val('');
            $line_begin.val('');
            $line_end.val('');
            return response.json();
        }).then(function(data) {
            let new_ano = $('<p>').text(data.code);
            $('.annotations').append(new_ano);
        });
    });

});
