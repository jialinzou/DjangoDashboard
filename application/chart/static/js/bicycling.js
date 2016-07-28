$( document ).ready(function() {
    d3.json('/chart/get_BI_users', pieAndBar);  
    $.getJSON('/chart/get_posts_BI', postList);
});