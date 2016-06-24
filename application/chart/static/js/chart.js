$( document ).ready(function() {
  createLineChart("/chart/get_data_linechart")
  createDiffChart("/chart/get_data_diffchart")
  createBarChart("/chart/get_data_barchart")
});

function createLineChart(json_path)
{
  var margin = {top: 10, right: 70, bottom: 20, left: 100},
      width = 1000 - margin.left - margin.right,
      height = 400 - margin.top - margin.bottom;
  
  var parseDate = d3.time.format("%Y%m%d%H").parse;
  
  var x = d3.time.scale()
      .range([0, width]);
  
  var y = d3.scale.linear()
      .range([height, 0]);
  
  var color = d3.scale.category10();
  
  var xAxis = d3.svg.axis()
      .scale(x)
      .orient("bottom");
  
  var yAxis = d3.svg.axis()
      .scale(y)
      .orient("left");
  
  var line = d3.svg.line()
      .interpolate("basis")
      .x(function(d) { return x(d.date); })
      .y(function(d) { return y(d.views); });
  
  var svg = d3.select(".chart_3").append("svg")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
    .append("g")
      .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
  
  d3.json(json_path, function(error, data) {
  //d3.tsv("/static/data.tsv", function(error, data) {
    
    if (error) throw error;
  
    color.domain(d3.keys(data[0]).filter(function(key) { return key !== "date"; }));
  
    //data.forEach(function(d) {
    //  d.date = parseDate(d.date);
    //});
  
    var views_source = color.domain().map(function(name) {
      return {
        name: name,
        values: data.map(function(d) {
          return {date: d.date, views: +d[name]};
        })
      };
    });
  
    x.domain(d3.extent(data, function(d) { return d.date; }));
  
    y.domain([
      d3.min(views_source, function(c) { return d3.min(c.values, function(v) { return v.views; }); }),
      d3.max(views_source, function(c) { return d3.max(c.values, function(v) { return v.views; }); })
    ]);
  
    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis);
  
    svg.append("g")
        .attr("class", "y axis")
        .call(yAxis)
      .append("text")
        .attr("transform", "rotate(0)")
        .attr("y", 6)
        .attr("dy", ".71em")
        .style("text-anchor", "end");
  
    var city = svg.selectAll(".city")
        .data(views_source)
      .enter().append("g")
        .attr("class", "city");
  
    city.append("path")
        .attr("class", "line")
        .attr("d", function(d) { return line(d.values); })
        .style("stroke", function(d) { return color(d.name); });
  
    city.append("text")
        .datum(function(d) { return {name: d.name, value: d.values[d.values.length - 1]}; })
        .attr("transform", function(d) { return "translate(" + x(d.value.date) + "," + y(d.value.views) + ")"; })
        .attr("x", 3)
        .attr("dy", ".35em")
        .text(function(d) { return d.name; });
  });
}

function createDiffChart(json_path)
{
  var margin = {top: 20, right: 25, bottom: 30, left: 70},
    width = 500 - margin.left - margin.right,
    height = 400 - margin.top - margin.bottom;

  var parseDate = d3.time.format("%Y%m%d").parse;
  
  var x = d3.time.scale()
      .range([0, width]);
  
  var y = d3.scale.linear()
      .range([height, 0]);
  
  var xAxis = d3.svg.axis()
      .scale(x)
      .orient("bottom")
      .tickFormat(d3.time.format("%b"));
  
  var yAxis = d3.svg.axis()
      .scale(y)
      .orient("left");
  
  var line = d3.svg.area()
      .interpolate("basis")
      .x(function(d) { return x(d.date); })
      .y(function(d) { return y(d["Actual"]); });
  
  var area = d3.svg.area()
      .interpolate("basis")
      .x(function(d) { return x(d.date); })
      .y1(function(d) { return y(d["Actual"]); });
  
  var svg = d3.select(".chart_2").append("svg")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
    .append("g")
      .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
  
  d3.json(json_path, function(error, data) {
    if (error) throw error;
  
    data.forEach(function(d) {
      d.date = parseDate(d.date);
      d["Actual"]= +d["Actual"];
      d["Forecast"] = +d["Forecast"];
    });
  
    x.domain(d3.extent(data, function(d) { return d.date; }));
  
    y.domain([
      d3.min(data, function(d) { return Math.min(d["Actual"], d["Forecast"]); }),
      d3.max(data, function(d) { return Math.max(d["Actual"], d["Forecast"]); })
    ]);
    
    svg.datum(data);
  
    svg.append("clipPath")
        .attr("id", "clip-below")
      .append("path")
        .attr("d", area.y0(height));
  
    svg.append("clipPath")
        .attr("id", "clip-above")
      .append("path")
        .attr("d", area.y0(0));
  
    svg.append("path")
        .attr("class", "area above")
        .attr("clip-path", "url(#clip-above)")
        .attr("d", area.y0(function(d) { return y(d["Forecast"]); }));
  
    svg.append("path")
        .attr("class", "area below")
        .attr("clip-path", "url(#clip-below)")
        .attr("d", area);
  
    svg.append("path")
        .attr("class", "line")
        .attr("d", line);
  
    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis);
  
    svg.append("g")
        .attr("class", "y axis")
        .call(yAxis)
      .append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 6)
        .attr("dy", ".71em")
        .style("text-anchor", "end");
  });
}

function createBarChart(json_path)
{
  var margin = {top: 20, right: 20, bottom: 50, left: 70},
    width = 500 - margin.left - margin.right,
    height = 400 - margin.top - margin.bottom;
  
  var x0 = d3.scale.ordinal()
      .rangeRoundBands([0, width], .1);
  
  var x1 = d3.scale.ordinal();
  
  var y = d3.scale.linear()
      .range([height, 0]);
  
  var color = d3.scale.ordinal()
      .range(["#1f77b4", "#ff7f0e", "#2ca02c", "#6b486b", "#a05d56", "#d0743c", "#ff8c00"]);
  
  var xAxis = d3.svg.axis()
      .scale(x0)
      .orient("bottom");
  
  var yAxis = d3.svg.axis()
      .scale(y)
      .orient("left")
      .tickFormat(d3.format(".2s"));
  
  var svg = d3.select(".chart_1").append("svg")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
    .append("g")
      .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
  
  d3.json(json_path, function(error, data) {
    if (error) throw error;
  
    var ageNames = d3.keys(data[0]).filter(function(key) { return key !== "State"; });
  
    data.forEach(function(d) {
      console.log(d);
      d.ages = ageNames.map(function(name) { return {name: name, value: +d[name]}; });
      console.log(d.ages);
    });
  
    x0.domain(data.map(function(d) { return d.State; }));
    x1.domain(ageNames).rangeRoundBands([0, x0.rangeBand()]);
    y.domain([0, d3.max(data, function(d) { return d3.max(d.ages, function(d) { return d.value; }); })]);
  
    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis)
        .selectAll("text")
          .style("text-anchor", "end")
          .attr("dx", "-.8em")
          .attr("dy", ".15em")
          .attr("transform", "rotate(-25)" );
  
    svg.append("g")
        .attr("class", "y axis")
        .call(yAxis)
      .append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 6)
        .attr("dy", ".71em")
        .style("text-anchor", "end");
  
    var state = svg.selectAll(".state")
        .data(data)
      .enter().append("g")
        .attr("class", "state")
        .attr("transform", function(d) { return "translate(" + x0(d.State) + ",0)"; });
  
    state.selectAll("rect")
        .data(function(d) { return d.ages; })
      .enter().append("rect")
        .attr("width", x1.rangeBand())
        .attr("x", function(d) { return x1(d.name); })
        .attr("y", function(d) { return y(d.value); })
        .attr("height", function(d) { return height - y(d.value); })
        .style("fill", function(d) { return color(d.name); });
  
    var legend = svg.selectAll(".legend")
        .data(ageNames.slice().reverse())
      .enter().append("g")
        .attr("class", "legend")
        .attr("transform", function(d, i) { return "translate(0," + i * 20 + ")"; });
  
    legend.append("rect")
        .attr("x", width - 18)
        .attr("width", 18)
        .attr("height", 18)
        .style("fill", color);
  
    legend.append("text")
        .attr("x", width - 24)
        .attr("y", 9)
        .attr("dy", ".35em")
        .style("text-anchor", "end")
        .text(function(d) { return d; });
  
  });
}