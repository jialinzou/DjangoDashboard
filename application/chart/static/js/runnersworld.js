$( document ).ready(function() {
    d3.json('/chart/get_RW_users', pieAndBar);   
    $.getJSON('/chart/get_posts_RW', postList);
});