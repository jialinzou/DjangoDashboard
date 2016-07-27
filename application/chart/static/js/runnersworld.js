$( document ).ready(function() {
    d3.json('/chart/get_RW_users', pieAndBar);
    $.currData = [];  
    setTimeout(get_concurrents(), 1000);
    setInterval(get_concurrents, 5000);   
    $.getJSON('/chart/get_posts_RW', postList);
});