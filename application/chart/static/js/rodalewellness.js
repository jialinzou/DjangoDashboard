$( document ).ready(function() {
    d3.json('/chart/get_WE_users', pieAndBar);  
    $.getJSON('/chart/get_posts_WE', postList);
});