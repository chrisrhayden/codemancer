'use strict';

function makeTags(tag) {
    /*
    let $li = $('li');
    let $a = $('a').attr({href: '#'}).text(tag);
    let made_tag = $li.append($a);
    */
    let str = '<li><a href="#">' + tag + '</a></li>';
    return str;
}


$(document).ready(function() {
    $.ajax({
        url: 'http://127.0.0.1:8000/api/v1/tags?format=json',
        success: function(result) {
            let len = result.length;
            for (let i=0;i<len;i++) {
                let tag = result[i].name;
                let made_tag = makeTags(tag);
                $('.ul-tags').append(made_tag);
            }
        },
        error: function(err) {
            alert(err);
        }
    });
});
