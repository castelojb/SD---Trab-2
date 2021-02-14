const express = require("express")
const app = express()
const http = require("http")
const server = http.createServer(app)
const bodyParser = require("body-parser")
const equipmentsService = require("./service/inMemoryDependency")
const cors = require("cors")
const equipmentsRouter = require("./http-routes/equipments")

app.use(bodyParser.urlencoded({ extended: true }))
app.use(bodyParser.json())

app.use(cors({
    origin: "*"
}))

app.use("/api/equipments", equipmentsRouter(equipmentsService))

module.exports = server