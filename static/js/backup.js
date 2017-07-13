// for(var i =0; i<values.length; i++)
                // {
                //   jk = {'lat':values[i].latitude, 'lng':values[i].longitude};
                //   L.marker(jk).addTo(map).bindPopup(values[i].name);
                // 

    // L.marker(result.latlng).addTo(map); //.bindPopup(result.address.Match_addr).openPopup();

    // function locate() {
//   map.locate({setView: true, maxZoom: 16});
// }

// function load_locations(latitude, longitude) {
//     $.ajax({
//           type: 'GET',
//           url:'/locate/?lat='+latitude+'&lng='+longitude,
//           success: function (responseData, textStatus, jqXHR) {
//               if (responseData.count === 1)
//               {
//                 map.setView(new L.LatLng(latitude, longitude), 14);
//                 values = responseData.results[0].around;
//                 add_layer(values);
//               }
//               else
//               {
//                 alert('Sorry we, do not have value for requested coordinates.')
//               }
//           },
//           error: function (jqXHR, errorThrown) {
//               console.log('Error in loading cities.');
//           } //error ends
//     }); //request ends
// }