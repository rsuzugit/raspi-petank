$(document).ready(function() {
  const image_elem = document.getElementById("streamer-image");
  const forward_button = document.getElementById("forward-button");
  const fire_button = document.getElementById("fire");
  var socket = io.connect('http://' + document.domain + ':' + location.port);
  
  socket.on('connect', function() {
	 console.log('User has connected');
	 socket.emit('check', {data: 'User connected'});
  });
  
  socket.on('image', function(msg) {
	image_elem.src = "data:image/jpeg;base64,"+msg;
  });

  $('#forward').on('touchstart touchend', function touchState(e) {
	if (e.type == "touchstart") {
	  socket.emit('action', '1');
	} else {
	  socket.emit('action', '8');
	}
  });

  $('#back').on('touchstart touchend', function touchState(e) {
	if (e.type == "touchstart") {
	  socket.emit('action', '2');
	} else {
	  socket.emit('action', '8');
	}
  });
  
  $('#left').on('touchstart touchend', function touchState(e) {
	if (e.type == "touchstart") {
	  socket.emit('action', '3');
	} else {
	  socket.emit('action', '8');
	}
  });
  
  $('#right').on('touchstart touchend', function touchState(e) {
	if (e.type == "touchstart") {
	  socket.emit('action', '4');
	} else {
	  socket.emit('action', '8');
	}
  });
  
  $('#turret-left').on('touchstart touchend', function touchState(e) {
	if (e.type == "touchstart") {
	  socket.emit('action', '5');
	} else {
	  socket.emit('action', '8');
	}
  });
  
  $('#turret-right').on('touchstart touchend', function touchState(e) {
	if (e.type == "touchstart") {
	  socket.emit('action', '6');
	} else {
	  socket.emit('action', '8');
	}
  });
  
  $('#fire').on('touchstart touchend', function touchState(e) {
	if (e.type == "touchstart") {
	  socket.emit('action', '7');
	} else {
	  socket.emit('action', '8');
	}
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
  
  fire_button.onclick = function fire_turret() {
	socket.emit('fire', {data: '7'});
  };
	  
});
