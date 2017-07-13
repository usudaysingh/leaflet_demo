var map = L.map('map').setView([20.5937, 78.9629], 6);

L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png').addTo(map);

var geocodeService = L.esri.Geocoding.geocodeService();

var my_layer = L.geoJson().addTo(map);

function onLocationFound(e) {
  var radius = e.accuracy / 2;

  geocodeService.reverse().latlng(e.latlng).run(function(error, result) {
    map.setView(new L.LatLng(result.latlng.lat, result.latlng.lng), 14);
    load_places_with_lat_lng(result.latlng.lat, result.latlng.lng);
  });
}

map.on('locationfound', onLocationFound);

map.locate({setView: true, maxZoom: 16});

function onEachFeature(feature, layer) {
  layer.bindPopup(feature.properties.name).openPopup();;
}

function add_layer(values)
{

  map.removeLayer(my_layer);

  geo_features = [];

  features = {
    "type": "FeatureCollection",
    "features": geo_features
  }

  for (var i=0; i<values.length; i++)
  {
    // var new_point = new L.LatLng(values[i].latitude, values[i].longitude);
    // if (new_point.distanceTo(current_point) <= 1000 || current_point.distanceTo(new_point) <= 1000 )
    // {
      feature = {
        "type": "Feature",
        "properties": {
            "name": values[i].name
        },
        "geometry": {
            "type": "Point",
            "coordinates": [values[i].longitude, values[i].latitude]
        }
      }

      geo_features.push(feature);
    // }
  }

  my_layer = L.geoJSON(features, {
    onEachFeature: onEachFeature
  })

  my_layer.addTo(map);
  
} //add layer

function load_markers(id)
{
  $.ajax({
          type: 'GET',
          url:'/locate/?id='+id,
          success: function (responseData, textStatus, jqXHR) {
            if (responseData.count === 0)
            {
              alert('Sorry we, do not have value for requested coordinates.');
              map.removeLayer(my_layer);
            }
            else
            {
              current_point = new L.LatLng(responseData.results[0].latitude, responseData.results[0].longitude);
              map.setView(current_point, 12);
              $('#latitude').val(responseData.results[0].latitude);
              $('#longitude').val(responseData.results[0].longitude);
              // get_all_values(responseData.results);
              add_layer(responseData.results);
            }
          },
          error: function (jqXHR, errorThrown) {
              console.log('Error');
          } //error ends
    }); //request ends
}

function load_places_with_lat_lng(lat, lng)
{
    $.ajax({
          type: 'GET',
          url:'/locate/?lat='+lat+'&lng='+lng,
          success: function (responseData, textStatus, jqXHR) {
            console.log(responseData);
            if (responseData.count === 0)
            {
              alert('Sorry we, do not have value for requested coordinates.');
              map.removeLayer(my_layer);
            }
            else
            {
              current_point = new L.LatLng(responseData.results[0].latitude, responseData.results[0].longitude);
              $('#latitude').val(responseData.results[0].latitude);
              $('#longitude').val(responseData.results[0].longitude);
              map.setView(current_point, 12);
              add_layer(responseData.results);
              // get_all_values(current_point);
            }
          },
          error: function (jqXHR, errorThrown) {
              console.log('Error');
          } //error ends
    }); //request ends
}

function locate_on_map()
{
  var latitude = $('#latitude').val();
  var longitude = $('#longitude').val();

  load_places_with_lat_lng(latitude, longitude);
}

function load_places()
{
  $.ajax({
        type: 'GET',
        url:'/locate/places',
        success: function (responseData, textStatus, jqXHR) {
            responseData.results.unshift({'id':'0','text':'Select Place'});
            $("#places").select2({
              data: responseData.results
            });
        },
        error: function (jqXHR, errorThrown) {
            console.log('Error');
        } //error ends
    }); //request ends
}