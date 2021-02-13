const grpc = require("@grpc/grpc-js")
const serviceApi = require("./grpc-routes/api")
const serviceImpl = require("./grpc-routes/impl")
const equipmentsService = require("./service/inMemoryDependency")
const server = new grpc.Server

server.addService(serviceApi(equipmentsService).service, serviceImpl)

module.exports = server