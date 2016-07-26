$( document ).ready(function() {
    d3.json('/chart/get_PVN_users', pieAndBar);   
    $.getJSON('/chart/get_posts_PVN', postList);
});