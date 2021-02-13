const grpc = require("@grpc/grpc-js")
const serviceApi = require("./grpc-routes/api")
const serviceImpl = require("./grpc-routes/impl")

const server = new grpc.Server
server.addService(serviceApi.service, serviceImpl)

module.exports = server