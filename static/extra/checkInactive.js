document.addEventListener("visibilitychange", () => {
	if ("hidden" == document.visibilityState){
		location.href = "/accounts/register?score=1233"
	}
});