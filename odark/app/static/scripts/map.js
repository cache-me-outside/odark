const GMAPS_URL = 'https://maps.googleapis.com/maps/api/js?v=3.exp&sensor=false';
(function() {
	$.getScript(GMAPS_URL, (data, textStatus, jqxhr) => {
		const pos = {lat: -34.000009, lng: -56.197645};
		const mapOptions = {
			zoom: 5,
			center: pos,
			mapTypeId: google.maps.MapTypeId.SATELLITE,
			zoomControl: false,
			scaleControl: false,
			mapTypeControl: false,
			streetViewControl: false,
			fullScreenControl: false,
			rotateControl: false,
			draggable: false
		};

		let el = document.createElement('div');

		$(el).attr('id', 'canvas');
		$(el).css('width', 200);
		$(el).css('height', 200);
		$('.map-container').append(el);

		const map = new google.maps.Map(el, mapOptions);
	});
})();