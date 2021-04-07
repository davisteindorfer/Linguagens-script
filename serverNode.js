const http = require('http');

const requestListener = function (req, res) {
  res.writeHead(200);
  res.end('teste');
}

const servidor = http.createServer(requestListener);
servidor.listen(8080);
