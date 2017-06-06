(function() {

	let clock = document.querySelector('digiclock');
	
	const pad = (x) => {
		return x < 10 ? '0'+x : x;
	};
	
	const ticktock = () => {
		const d = new Date();
		
		const h = pad( d.getHours() );
		const m = pad( d.getMinutes() );
		const s = pad( d.getSeconds() );
		
		const current_time = [h,m,s].join(':');
		
		clock.innerHTML = current_time;
		
	};
	
	ticktock();
	setInterval(ticktock, 1000);
	
}());
