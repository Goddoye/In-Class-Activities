// Create a map object
var myMap = L.map("map", {
  center: [37.09, -95.71],
  zoom: 5
});

// Add a tile layer
L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets",
  accessToken: API_KEY
}).addTo(myMap);

// City markers

// Add code to create a marker for each city below and add it to the map

// newyork;
// chicago;
// houston;
// la;
// omaha;

var cities = [{
  location: [40.7128, -74.0059],
  name: "New York",
  population: "8,550,405"
},
{
  location: [41.878113, -87.629799],
  name: "Chicago",
  population: "8,550,405"
},
{
  location: [29.760427, -95.369804],
  name: "Houston",
  population: "8,550,405"
},
{
  location: [34.052235, -118.243683],
  name: "LA",
  population: "8,550,405"
},
{
  location: [41.256538, -95.934502],
  name: "Omaha",
  population: "8,550,405"
}
]

for (var i = 0; i < cities.length; i++) {
  var city = cities[i];
  L.marker(city.location)
    .bindPopup("<h1>" + city.name + "</h1> <hr> <h3>Population " + city.population + "</h3>")
    .addTo(myMap);
};
