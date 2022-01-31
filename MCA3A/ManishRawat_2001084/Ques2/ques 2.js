const http = require("http");
const server = http.createServer((req,res) =>{
res.end("Response from server-->>" + PORT);
});
const PORT = process.env.PORT || 3000;
const HOST = "localhost";
server.listen(PORT, HOST, () =>{
    console.log("Current server at PORT "+PORT );
});