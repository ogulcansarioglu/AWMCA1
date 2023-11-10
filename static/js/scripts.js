// Initialize the map on the "map" div with a given center and zoom
var map = L.map('map').setView(10, 13);

// Set up the OSM layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 19,
  attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Function to add park markers
function addBorderMarkers(parks) {
  parks.forEach(function(park) {
    var marker = L.marker([park.lat, park.lng]).addTo(map);
    marker.bindPopup(`<b>${park.name}</b>`).on('click', function() {
      document.getElementById('parkDetails').innerHTML = `
        <h1>${park.name}</h1>
        <p><strong>Location:</strong> ${park.location}</p>
        <p><strong>Description:</strong> ${park.description}</p>
        <!-- Add any additional details you want here -->
      `;
      // Open the sidebar
      document.getElementById('sidebar').style.width = '250px';
    });
  });
}

document.addEventListener('DOMContentLoaded', function() {
    // Initialize the map on the "map" div with a given center and zoom
    var map = L.map('map').setView([51.505, -0.09], 13);

    // Set up the OSM layer
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    // Add a marker
    var marker = L.marker([51.5, -0.09]).addTo(map);
    marker.bindPopup("<b>Hello world!</b><br>I am a popup.").openPopup();

    // Add another marker
    var marker2 = L.marker([51.51, -0.1]).addTo(map);
    marker2.bindPopup("<b>Another point!</b><br>Here's some more info.").openPopup();
});

fetch('/api/v1/hotels/')
      .then(response => response.json())
      .then(data => {
        addBorderMarkers(data);
        console.log("Fetched data:", data);
      }).catch(error => {
        console.error('Error fetching world border data:', error);
      });

function closeNav() {
  document.getElementById('sidebar').style.width = "0";
}
