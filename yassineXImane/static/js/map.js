function initMap() {
    // Replace 'YOUR_API_KEY' with your actual API key
    const map = new google.maps.Map(document.getElementById("map-container"), {
      zoom: 8,
      center: { lat: -33.8688, lng: 151.2093 },  // You can set your default location here
    });
  }