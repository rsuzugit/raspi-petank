$(document).ready(function() {
  const image_elem = document.getElementById("streamer-image");
  const forward_button = document.getElementById("forward-button");
  const stop_button = document.getElementById("stop-button");
  var socket = io.connect('http://' + document.domain + ':' + location.port);
  
  socket.on('connect', function() {
	 console.log('User has connected');
	 socket.emit('check', {data: 'User connected'});
  });
  
  socket.on('image', function(msg) {
	image_elem.src = "data:image/jpeg;base64,"+msg;
  });
  
  $('#forward').on('mousedown mouseup', function mouseState(e) {
	if (e.type == "mousedown") {
	  socket.emit('action', '1');
	} else {
	  socket.emit('action', '8');
	}
  });
  
  $('#back').on('mousedown mouseup', function mouseState(e) {
	if (e.type == "mousedown") {
	  socket.emit('action', '2');
	} else {
	  socket.emit('action', '8');
	}
  });
  
  $('#left').on('mousedown mouseup', function mouseState(e) {
	if (e.type == "mousedown") {
	  socket.emit('action', '3');
	} else {
	  socket.emit('action', '8');
	}
  });
  
  $('#right').on('mousedown mouseup', function mouseState(e) {
	if (e.type == "mousedown") {
	  socket.emit('action', '4');
	} else {
	  socket.emit('action', '8');
	}
  });
  
  $('#turret-left').on('mousedown mouseup', function mouseState(e) {
	if (e.type == "mousedown") {
	  socket.emit('action', '5');
	} else {
	  socket.emit('action', '8');
	}
  });
  
  $('#turret-right').on('mousedown mouseup', function mouseState(e) {
	if (e.type == "mousedown") {
	  socket.emit('action', '6');
	} else {
	  socket.emit('action', '8');
	}
  });
  
  $('#fire').on('mousedown mouseup', function mouseState(e) {
	if (e.type == "mousedown") {
	  socket.emit('action', '7');
	} else {
	  socket.emit('action', '8');
	}
  });
  
  stop_button.onclick = function stop_motors() {
	socket.emit('stop', {data: '8'});
  };
	  
});
