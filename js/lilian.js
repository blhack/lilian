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

function submit_link(url,title,category,token) {
	$.post("/cgi-bin/submit_link.cgi", {"url":url,"title":title,"category":category,"token":token})
		.done(function(data) {
			var link_id = data["link_id"];
			window.location("/item?" + link_id);
		})
	}




