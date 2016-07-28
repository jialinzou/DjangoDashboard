$( document ).ready(function() {
    d3.json('/chart/get_MH_users', pieAndBar);  
    $.getJSON('/chart/get_posts_MH', postList);
});