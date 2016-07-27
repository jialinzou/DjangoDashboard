$( document ).ready(function() {
    d3.json('/chart/get_ROL_users', pieAndBar);   
    $.getJSON('/chart/get_posts_ROL', postList);
});