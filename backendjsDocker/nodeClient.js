const net = require('net');
const host = 'localhost';
const port = '6890';
const EOF = "x23Stop"

const USER_ID = "not_not_mk"
const NUMBER_OF_SCORES = "1000"

var socket = new net.Socket();

socket.connect(port, host, ()=>{
	socket.write(USER_ID + " " + NUMBER_OF_SCORES)
});

socket.on('data', (data) => {
    console.log(`${data}`);
});
