$( document ).ready(function() {
    d3.json('/chart/get_WH_users', pieAndBar);   
    $.getJSON('/chart/get_posts_WH', postList);
});