$( document ).ready(function() {
    $.currData = [];
    get_concurrents();
    setInterval(get_concurrents, 5000);
    d3.json('/chart/get_users_per_channel', pieAndBar);
    //d3.json('/chart/get_concurrents', concurrents);
    //d3.json('/chart/get_top_pages', table);
    $.getJSON('/chart/get_top_posts', postList);
});

function pieAndBar(fData){
    id = '.chart_3';
    var channels = ["Referral", "Direct", "Social", "Search", "Email"];
    var barColor = 'steelblue';
    function segColor(c){ return {'Direct': '#dc3912',
                                 'Email': '#ff9900',
                                 'Search': '#109618',
                                 //'Other': '#3366cc',
                                 //'Paid_Search': '#990099',
                                 'Referral': '#0099c6',
                                 'Social': '#dd4477'}[c]; }
    
    // compute total for each state.
    fData.forEach(function(d){d.total=d.users.Direct+d.users.Email+
                    d.users.Search+d.users.Referral+
                    d.users.Social;});
    
    // parse date
    var parseDate = d3.time.format("%Y%m%d").parse;
    var format = d3.time.format("%b %d");
    fData.forEach(function(d) {
      d.date = format(parseDate(d.date));
    });
    
    // function to handle histogram.
    function histoGram(fD){
        var hG={},    hGDim = {t: 60, r: 0, b: 30, l: 0};
        hGDim.w = 360 - hGDim.l - hGDim.r, 
        hGDim.h = 300 - hGDim.t - hGDim.b;
            
        //create svg for histogram.
        var hGsvg = d3.select(id).append("svg")
            .attr("width", hGDim.w + hGDim.l + hGDim.r)
            .attr("height", hGDim.h + hGDim.t + hGDim.b).append("g")
            .attr("transform", "translate(" + hGDim.l + "," + hGDim.t + ")");
            
        // create function for x-axis mapping.
        var x = d3.scale.ordinal().rangeRoundBands([0, hGDim.w], 0.1)
                .domain(fD.map(function(d) { return d[0]; }));

        // Add x-axis to the histogram svg.
        hGsvg.append("g").attr("class", "x axis")
            .attr("transform", "translate(0," + hGDim.h + ")")
            .call(d3.svg.axis().scale(x).orient("bottom"));

        // Create function for y-axis map.
        var y = d3.scale.linear().range([hGDim.h, 0])
                .domain([0, d3.max(fD, function(d) { return d[1]; })]);

        // Create bars for histogram to contain rectangles and users labels.
        var bars = hGsvg.selectAll(".bar").data(fD).enter()
                .append("g").attr("class", "bar");
        
        //create the rectangles.
        bars.append("rect")
            .attr("x", function(d) { return x(d[0]); })
            .attr("y", function(d) { return y(d[1]); })
            .attr("width", x.rangeBand())
            .attr("height", function(d) { return hGDim.h - y(d[1]); })
            .attr('fill',barColor)
            .on("mouseover",mouseover)// mouseover is defined below.
            .on("mouseout",mouseout);// mouseout is defined below.
            
        //Create the users labels above the rectangles.
        bars.append("text").text(function(d){ return d3.format(".2s")(d[1])})
            .attr("x", function(d) { return x(d[0])+x.rangeBand()/2; })
            .attr("y", function(d) { return y(d[1])-5; })
            .attr("text-anchor", "middle");
        
        //create the title
        hGsvg.append("text")
            .attr("x", (hGDim.w / 2))                
            .attr("y", 0 - (hGDim.t / 2))
            .attr("text-anchor", "middle")
            .attr("class", "title")    
            .style("font-size", "16px")     
            .text('Users from All Sources');
        
        function mouseover(d){  // utility function to be called on mouseover.
            clearInterval(disploop);
            hG.update(fData.map(function(v){
                return [v.date,v.total];}), barColor, 'Users from All Sources');
            // filter for selected date.
            var st = fData.filter(function(s){ return s.date == d[0];})[0],
                nD = channels.map(function(s){ return {type:s, users:st.users[s]};});
            //console.log(nD);   
            // call update functions of pie-chart and legend.    
            pC.update(nD, d[0]);
            leg.update(nD);
        }
        
        function mouseout(d){    // utility function to be called on mouseout.
            // reset the pie-chart and legend.    
            pC.update(tF, 'Last 7 Days');
            leg.update(tF);
        }
        
        // create function to update the bars. This will be used by pie-chart.
        hG.update = function(nD, color, title){
            // update the domain of the y-axis map to reflect change in frequencies.
            y.domain([0, d3.max(nD, function(d) { return d[1]; })]);
            
            // Attach the new data to the bars.
            var bars = hGsvg.selectAll(".bar").data(nD);
            
            // transition the height and color of rectangles.
            bars.select("rect").transition().duration(500)
                .attr("y", function(d) {return y(d[1]); })
                .attr("height", function(d) { return hGDim.h - y(d[1]); })
                .attr("fill", color);

            // transition the users labels location and change value.
            bars.select("text").transition().duration(500)
                .text(function(d){ return d3.format(".2s")(d[1])})
                .attr("y", function(d) {return y(d[1])-5; });   
            
            // transition the title    
            hGsvg.select(".title").transition().duration(500)
                .text(title);       
        }        
        return hG;
    }
    
    // function to handle pieChart.
    function pieChart(pD){
        var pC ={},    pieDim ={t: 60, r: 0, b: 30, l: 0};
        pieDim.w = 250 - pieDim.l - pieDim.r, 
        pieDim.h = 360 - pieDim.t - pieDim.b; 
        pieDim.r = (Math.min(pieDim.w, pieDim.h) -20) / 2;
                
        // create svg for pie chart.
        var piesvg = d3.select(id).append("svg")
            .attr("width", pieDim.w).attr("height", pieDim.h).append("g")
            .attr("transform", "translate("+pieDim.w/2+","+pieDim.h/2+")");
        
        // create function to draw the arcs of the pie slices.
        var arc = d3.svg.arc().outerRadius(pieDim.r - 10).innerRadius(0);

        // create a function to compute the pie slice angles.
        var pie = d3.layout.pie().sort(null).value(function(d) { return d.users; });

        // Draw the pie slices.
        piesvg.selectAll("path").data(pie(pD)).enter().append("path").attr("d", arc)
            .each(function(d) { this._current = d; })
            .style("fill", function(d) { return segColor(d.data.type); })
            .on("mouseover",mouseover).on("mouseout",mouseout);
        
        //create the title
        piesvg.append("text")
            .attr("x", 0)                
            .attr("y", -90 - (pieDim.t / 2))
            .attr("text-anchor", "middle")
            .attr("class", "title")    
            .style("font-size", "16px")     
            .text('Last 7 Days');
        
        // create function to update pie-chart. This will be used by histogram.
        pC.update = function(nD, title){
            piesvg.selectAll("path").data(pie(nD)).transition().duration(500)
                .attrTween("d", arcTween);
            
            // transition the title    
            piesvg.select(".title").transition().duration(500)
                .text(title);
        }        
        // Utility function to be called on mouseover a pie slice.
        function mouseover(d){
            // call the update function of histogram with new data.
            clearInterval(disploop);
            hG.update(fData.map(function(v){ 
                return [v.date,v.users[d.data.type]];}),
                segColor(d.data.type), 
                'Users from '+d.data.type);
        }
        //Utility function to be called on mouseout a pie slice.
        function mouseout(d){
            // call the update function of histogram with all data.
            hG.update(fData.map(function(v){
                return [v.date,v.total];}), barColor, 'Users from All Sources');
        }
        // Animating the pie-slice requiring a custom function which specifies
        // how the intermediate paths should be drawn.
        function arcTween(a) {
            var i = d3.interpolate(this._current, a);
            this._current = i(0);
            return function(t) { return arc(i(t));    };
        }    
        return pC;
    }
    
    // function to handle legend.
    function legend(lD){
        var leg = {};
            
        // create table for legend.
        var legend = d3.select(id).append("table").attr('class','legend').attr('width', '240');
        
        // create one row per segment.
        var tr = legend.append("tbody").selectAll("tr").data(lD).enter().append("tr");
            
        // create the first column for each segment.
        tr.append("td").append("svg").attr("width", '16').attr("height", '16').append("rect")
            .attr("width", '16').attr("height", '16')
            .attr("fill",function(d){ return segColor(d.type); });
            
        // create the second column for each segment.
        tr.append("td").text(function(d){ return d.type;});

        // create the third column for each segment.
        tr.append("td").attr("class",'legendFreq')
            .text(function(d){ return d3.format(",")(d.users);});

        // create the fourth column for each segment.
        tr.append("td").attr("class",'legendPerc')
            .text(function(d){ return getLegend(d,lD);});

        // Utility function to be used to update the legend.
        leg.update = function(nD){
            // update the data attached to the row elements.
            var l = legend.select("tbody").selectAll("tr").data(nD);

            // update the frequencies.
            l.select(".legendFreq").text(function(d){ return d3.format(",")(d.users);});

            // update the percentage column.
            l.select(".legendPerc").text(function(d){ return getLegend(d,nD);});        
        }
        
        function getLegend(d,aD){ // Utility function to compute percentage.
            return d3.format("%")(d.users/d3.sum(aD.map(function(v){ return v.users; })));
        }

        return leg;
    }

    // calculate total frequency by segment for all date.
    var tF = channels.map(function(d){ 
        return {type:d, users: d3.sum(fData.map(function(t){ return t.users[d];}))}; 
    });    
    // calculate total frequency by date for all segment.
    var sF = fData.map(function(d){return [d.date,d.total];});

    var hG = histoGram(sF), // create the histogram.
        pC = pieChart(tF), // create the pie-chart.
        leg= legend(tF);  // create the legend.
    
    function dispLoop(){
        if(i == 5){
            hG.update(fData.map(function(v){
                return [v.date,v.total];}), barColor, 'Users from All Sources');
            i = 0;
        } else {
            hG.update(fData.map(function(v){ 
                    return [v.date,v.users[channels[i]]];}),
                    segColor(channels[i]), 
                    'Users from '+channels[i]);
            i++;
        }
    }
    var i = 5;
    var disploop = setInterval(dispLoop, 13000);
}

function table(top_pages){
    //console.log(top_pages);       
    // create table for legend.
    var legend = d3.select(".chart_1").append("table").attr('class','legend');
    
    // create header
    columns = ["Unique Users", "Titles", "Engaged Times"]; 
    var th = legend.append("thead").selectAll("th").data(columns).enter().append("th");
    th.append("text").text(function(d){return d});   
    
    // create one row per segment.
    var tr = legend.append("tbody").selectAll("tr").data(top_pages).enter().append("tr");
        
    // create the first column for each segment.
    tr.append("td").text(function(d){ return d3.format(",")(d.Unique_users);});
        
    // create the second column for each segment.
    tr.append("td").text(function(d){ return d.Title;});

    // create the third column for each segment.
    tr.append("td").text(function(d){ return d.Engaged_time;});
}

function postList(top3){
    //console.log(top4);
    $('#post1 .fb-post').attr('data-href', top3[0]['link']);
    $('#post2 .fb-post').attr('data-href', top3[1]['link']);
    $('#post3 .fb-post').attr('data-href', top3[2]['link']);
}

function sortByPeoples(a,b){
    var x = a.peoples;
    var y = b.peoples;
    return ((x < y)? 1 : -1);
}
function get_concurrents(){
    $.currData = [];
    var domains = {
        "WH": "womenshealthmag.com",
        "MH": "menshealth.com",
        "PVN": "prevention.com",
        "RW": "runnersworld.com",
        "BI": "bicycling.com",
        "ROL": "rodalesorganiclife.com",
        "WE": "rodalewellness.com"
    };
    var url = 'http://api.chartbeat.com/live/quickstats/v4?apikey=7f24fb00da5bb5d913b7cab306f71ead&host=';
    $.each(domains, function(key, domain){
        $.get(url+domains[key], function(d){
            $.currData.push({'site':key, 'peoples':d['data']['stats']['people']});
            if ($.currData.length === 7){
                $.currData.sort(sortByPeoples);
                if($('.concurrents')[0]){
                    updatePage($.currData);
                } else{
                    concurrents($.currData);
                }
            }
        });
    });    
}

function concurrents(cData){
    var logo = [
        {'site':'MH', 'link':'http://logonoid.com/images/mens-health-logo.png'},
        {'site':'WH', 'link':'http://wendywalk.org/wp-content/uploads/2014/10/womens-health-logo.gif'},
        {'site':'PVN', 'link':'http://www.prevention.com/sites/prevention.com/themes/prevention/logo.png'},      
        {'site':'RW', 'link':'https://www.circules.com/circulation/natmagsproducts/images/rwnewlogo.gif'},
        {'site':'BI', 'link':'http://www.bicycling.com/sites/bicycling.com/themes/bicycling/logo.png'},
        {'site':'ROL', 'link':'http://www.rodalesorganiclife.com/sites/rodalesorganiclife.com/themes/rol/logo.png'},
        {'site':'WE', 'link':'http://www.rodalewellness.com/sites/rodalewellness.com/themes/wellness/logo.png'}
    ];
    
    //d3.select('chart_3').append('circle').attr('height', 512).attr('width', 512).style('fill', 'url(#image)');
    var concurrents = d3.select(".chart_3").append("table").attr('class','concurrents');
    // create patterns
    var defs = d3.select('.chart_3').append('svg').attr('width', 0).attr('height', 0).append("defs")
    var pattern = defs.selectAll('pattern').data(logo).enter()
        .append("pattern")
        .attr("id", function(d){return 'logo-'+d.site;})
        .attr('patternUnits', 'userSpaceOnUse')
        .attr('width', 100)
        .attr('height', 22)
    pattern.append("image")
        .attr('width', 100)
        .attr('height', 22)
        .attr("xlink:href", function(d){return d.link;});

    // create header
    columns = ["", "Concurrents"]; 
    var th = concurrents.append("thead").selectAll("th").data(columns).enter().append("th");
    th.append("text").text(function(d){return d});   
    
    // create one row per segment.
    var tr = concurrents.append("tbody").selectAll("tr").data(cData).enter().append("tr");
    
    // create the first column for each segment.
    tr.append("td").append("svg").attr("width", '100').attr("height", '22').append("rect")
        .attr("width", '100').attr("height", '22').attr('class', 'brands')
        .attr("fill",function(d){ return 'url(#logo-'+d.site+')'; });  

    // create the first column for each segment.
    //tr.append("td").text(function(d){ return d.site;});
        
    // create the second column for each segment.
    tr.append("td").text(function(d){ return d3.format(",")(d.peoples);}).attr('class', 'peoples').style('text-align', 'right');
}
function updatePage(cData){
    var logo = [
        {'site':'MH', 'link':'http://logonoid.com/images/mens-health-logo.png'},
        {'site':'WH', 'link':'http://wendywalk.org/wp-content/uploads/2014/10/womens-health-logo.gif'},
        {'site':'PVN', 'link':'http://www.prevention.com/sites/prevention.com/themes/prevention/logo.png'},      
        {'site':'RW', 'link':'https://www.circules.com/circulation/natmagsproducts/images/rwnewlogo.gif'},
        {'site':'BI', 'link':'http://www.bicycling.com/sites/bicycling.com/themes/bicycling/logo.png'},
        {'site':'ROL', 'link':'http://www.rodalesorganiclife.com/sites/rodalesorganiclife.com/themes/rol/logo.png'},
        {'site':'WE', 'link':'http://www.rodalewellness.com/sites/rodalewellness.com/themes/wellness/logo.png'}
    ];
    // create patterns
    var defs = d3.select('.chart_3').append('svg').attr('width', 0).attr('height', 0).append("defs")
    var pattern = defs.selectAll('pattern').data(logo).enter()
        .append("pattern")
        .attr("id", function(d){return 'logo-'+d.site;})
        .attr('patternUnits', 'userSpaceOnUse')
        .attr('width', 100)
        .attr('height', 22)
    pattern.append("image")
        .attr('width', 100)
        .attr('height', 22)
        .attr("xlink:href", function(d){return d.link;});

    var peoples = d3.selectAll('.peoples').data(cData);
    peoples.transition().duration(500)
        .text(function(d){ return d3.format(",")(d.peoples);}).style('text-align', 'right');

    var brands = d3.selectAll('.brands').data(cData);
    brands.transition().duration(500)
        .attr("fill",function(d){ return 'url(#logo-'+d.site+')'; });
}
