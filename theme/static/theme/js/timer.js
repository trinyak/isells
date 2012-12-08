	var Timer,
		TotalSeconds;

	function CreateTimer(TimerID, Time) {
		Time.month = Time.month - 1; //This adjusts for new Date() starting months at 0
		endDate = new Date(Time.year,Time.month,Time.day);
		now = new Date();
		Time = endDate - now;
		if(Time <= 0) {
			Time = 0;
			return; //This stops the timer from being inserted if the time is up.
		}

		Timer = document.getElementById(TimerID);
		TotalSeconds = Math.floor(Time / 1000);

		UpdateTimer()
		window.setTimeout('Tick()', 1000);
	}


	function Tick() {
		if (TotalSeconds <= 0) {
			return;
		}

		TotalSeconds -= 1;
		UpdateTimer()
		window.setTimeout("Tick()", 1000);
	}

	function UpdateTimer() {
		var Seconds = TotalSeconds;
        var Days = Math.floor(Seconds / 86400);
        Seconds -= Days * 86400;
        var Hours = Math.floor(Seconds / 3600);
        Seconds -= Hours * (3600);
        var Minutes = Math.floor(Seconds / 60);
        Seconds -= Minutes * (60);

        var TimeStr = '<div class="figure"><div class="square"><span>' + LeadingZero(Days) + '</span></div><label>DAYS</label></div><div class="figure"><div class="square"><span>' + LeadingZero(Hours) + '</span></div><label>HOURS</label></div><div class="figure"><div class="square"><span>' + LeadingZero(Minutes) + '</span></div><label>MINUTES</label></div><div class="figure"><div class="square"><span>' + LeadingZero(Seconds) + '</span></div><label>SECONDS</label></div>'

		Timer.innerHTML = TimeStr;
	}

	function LeadingZero(Time) {
	    return (Time < 10) ? "0" + Time : + Time;
	}
