var map = L.map('map').setView([20.5937, 78.9629], 6);

L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png').addTo(map);

var geocodeService = L.esri.Geocoding.geocodeService();

var my_layer = L.geoJson().addTo(map);

function onLocationFound(e) {
  var radius = e.accuracy / 2;

  geocodeService.reverse().latlng(e.latlng).run(function(error, result) {
    map.setView(new L.LatLng(result.latlng.lat, result.latlng.lng), 14);
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
              if (responseData.count > 0)
              {
                map.setView(new L.LatLng(responseData.results[0].latitude, responseData.results[0].longitude), 12);
                values = responseData.results[0].around;
                add_layer(values);
              }
              else
              {
                alert('Sorry we, do not have value for requested coordinates.')
              }
          },
          error: function (jqXHR, errorThrown) {
              console.log('Error in loading cities.');
          } //error ends
    }); //request ends
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
            console.log('Error in loading cities.');
        } //error ends
    }); //request ends
}