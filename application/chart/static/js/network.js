$( document ).ready(function() {
    d3.json('/chart/get_users_per_channel', pieAndBar);  
    $.getJSON('/chart/get_top_posts', postList);
});