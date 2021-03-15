setTimeout(() => {
	document.addEventListener("visibilitychange", () => {
		if ("hidden" == document.visibilityState){
			location.href = "/gameover"
		}
	});

}, 4000);