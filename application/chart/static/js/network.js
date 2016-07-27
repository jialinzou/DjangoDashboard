$( document ).ready(function() {
    d3.json('/chart/get_users_per_channel', pieAndBar);
    $.currData = [];  
    setTimeout(get_concurrents(), 1000);
    setInterval(get_concurrents, 5000);   
    $.getJSON('/chart/get_top_posts', postList);
});