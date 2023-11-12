
    var map = L.map('map').setView([53.3498, -6.2603], 6);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 15,
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    function parseLatLngFromWKT(wkt) {
        const match = wkt.match(/POINT \(([^ ]+) ([^ ]+)\)/);
        if (match) {
            const longitude = parseFloat(match[1]);
            const latitude = parseFloat(match[2]);
            return {latitude, longitude};
        } else {
            return null;
        }
    }


    var allMarkers = []; // Global array to store markers

    function addHotelMarkers(data) {
        allMarkers.forEach(marker => map.removeLayer(marker));
        allMarkers = [];

        data.forEach(item => {
            const latLng = parseLatLngFromWKT(item.location);
            if (latLng) {
                var marker = L.marker([latLng.latitude, latLng.longitude]).addTo(map)
                    .bindPopup(`<b>${item.name}</b><br>${item.address}<br> ${createAttLink(item.name, item.id)}`);

                allMarkers.push(marker);
            } else {
                console.error('Invalid LatLng data for item:', item);
            }
        });
    }

    function addAttMarkers(data) {
        allMarkers.forEach(marker => map.removeLayer(marker));
        allMarkers = [];

        data.forEach(item => {

            var marker = L.marker([item.latitude, item.longitude]).addTo(map)
                .bindPopup(`<b>${item.name}</b><br>${item.addressloc}<br> ${createAttLink(item.name, item.id)}`);

            allMarkers.push(marker);

        });
    }

    function handleSearch() {
        var searchQuery = document.getElementById('parkSearch').value.toLowerCase();

        fetch('/api/v1/att/')
            .then(response => response.json())
            .then(data => {
                var filteredData = data.filter(item => item.name.toLowerCase().includes(searchQuery));

                if (filteredData.length > 0) {
                    const firstMatch = filteredData[0];
                    console.log(firstMatch)

                    map.setView([firstMatch.latitude, firstMatch.longitude], 15);


                    addAttMarkers(filteredData);
                } else {
                    console.log('No matching att found');
                }
            })
            .catch(error => console.error('Error fetching data:', error));
    }

    fetch('/api/v1/hotels/')
        .then(response => response.json())
        .then(data => {
            addHotelMarkers(data);
        }).catch(error => console.error('Error fetching hotel data:', error));

    function closeNav() {
        document.getElementById('sidebar').style.width = "0";
    }

    fetch('/api/v1/att/')
        .then(response => response.json())
        .then(data => {
            addAttMarkers(data);
        }).catch(error => console.error('Error fetching hotel data:', error));

    function closeNav() {
        document.getElementById('sidebar').style.width = "0";
    }

    // Updated createHotelLink function
    function createAttLink(hotelName, hotelId) {
        var encodedHotelName = encodeURIComponent(hotelName);
        var searchUrl = `https://www.google.com/search?q=${encodedHotelName}`;
        return `<a href="${searchUrl}" target="_blank">${hotelName}</a> <br>
          <button onclick="showHotelDetails('${hotelId}')">Ask About This Attraction</button>`;
    }

    function showHotelDetails(hotelId) {
        // fetch hotel details using the hotelId if needed
        var hotelDetailsHTML = `<h3>Attraction Details</h3>
                            <p>Details about the attraction...</p>
                            <h4>Ask a Question</h4>
                            <div id="chatContainer">
                              <div id="chatBox" style="height: 300px; overflow-y: scroll; border: 1px solid #ccc; padding: 10px;"></div>
                              <input type="text" id="userInput" placeholder="Type your question..." style="width: 80%;">
                              <button onclick="sendChat()">Send</button>
                            </div>`;
        document.getElementById('hotelDetails').innerHTML = hotelDetailsHTML;
        document.getElementById('sidebar').style.width = '350px'; // Adjust width for chat

    }

    function sendChat() {
        var input = document.getElementById('userInput').value;
        document.getElementById('userInput').value = '';

        var chatBox = document.getElementById('chatBox');
        chatBox.innerHTML += `<div>User: ${input}</div>`;

        fetch('/api/v1/chat/', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({message: input}),
        })
            .then(response => {
                if (!response.ok) {
                    console.log(response)
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                chatBox.innerHTML += `<div>ChatGPT: ${data.response}</div>`;
                chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the bottom
            })
            .catch(error => console.error('Error:', error));
    }





