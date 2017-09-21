function setLineNumbers() {
    // TODO PLAES fix
    let two_click = 0;
    $('.line-number').on('click', function() {
        // add line number to anno field
        let line_num = $(this).text();
        if (two_click === 0) {
            $('#id_line_begin').val(Number(line_num));
            two_click = 1;
        } else {
            $('#id_line_end').val(Number(line_num));
        }
    });


}


$(document).ready(function() {
    // for detail only
    'use strict';

    setLineNumbers();

    $('.com-ano-submit').on('click', function(evt) {
        // POST anos or comments
        // the if after both funcs is the logic

        evt.preventDefault();

        let snip_pk = $('.code-snip').attr('data-pk');
        let $text = $('#id_text');
        let $ano_code = $('#id_code');

        let comment_text = $text.val();
        let annotation_code = $ano_code.val();

        let myHeader = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        };

        function commentPost() {
            // post comment
            let url = '/api/v1/comms/';

            let form_data = {
                'text': comment_text,
                'snippet': snip_pk
            };
            let myInit = {
                method: 'POST',
                body: JSON.stringify(form_data),
                headers: myHeader,
            };

            fetch(url, myInit).then(function(response) {
                // success
                $text.val('');
                return response.json();
            });

            // to fix when user auth is added
            let $com_div = $('.comments');
            let auth = $('<p>').text('anon said');
            let com_text = $('<p>').text(comment_text);
            let text_array = [auth, com_text];
            $com_div.append(text_array);
        }

        function annotationPost() {
            // post annotation
            let url = '/api/v1/anos/';
            let $line_begin = $('#id_line_begin');
            let $line_end = $('#id_line_end');

            let form_data = {
                'code': annotation_code,
                'line_begin': $line_begin.val(),
                'line_end': $line_end.val(),
                'snippet': snip_pk
            };
            let myInit = {
                method: 'POST',
                body: JSON.stringify(form_data),
                headers: myHeader,
            };

            fetch(url, myInit).then(function(response) {
                $ano_code.val('');
                $line_begin.val('');
                $line_end.val('');
                return response.json();
            }); // add anos to page here
        }

        if (comment_text && ! annotation_code) {
            // only a comment
            commentPost();
        } else if (annotation_code && ! comment_text) {
            // only a annotation
            annotationPost();
        } else if (comment_text && annotation_code) {
            // both comment and annotation
            commentPost();
            annotationPost();
        }
    });
});
