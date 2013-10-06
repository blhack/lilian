//this does nothing yet
function login(user,password,token) {
	$.post("/cgi-bin/login.cgi", {"user":user,"password":password,"token":token})
		.done( function(data) {
			var session_id = data["session_id"];
			$.cookie("session_id", session_id);
			location.reload();
		} );
	}

function logout() {
	$.removeCookie("session_id");
	$.post("/cgi-bin/logout.cgi");
	location.reload();
	}

function whoami() {
	var session_id = $.cookie("session_id");
	$.post("/cgi-bin/whoami.cgi", {"session_id":session_id})
		.done(function(data) {
			var user = data["user"];
			$("#user").text(user);
		})
	}
