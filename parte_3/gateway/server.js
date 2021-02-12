const express = require("express")
const app = express()
const http = require("http")
const server = http.createServer(app)
const bodyParser = require("body-parser")
const equipmentsRouter = require("./routes/equipments")
const EquipmentService = require("./service/EquipmentsService")
const EquipmentsInMemory = require("./repository/EquipmentInMemory")

app.use(bodyParser.urlencoded({ extended: true }))
app.use(bodyParser.json())

const equipmentsRepository = new EquipmentsInMemory
const equipmentsService = new EquipmentService(equipmentsRepository)

app.use("/api/equipments", equipmentsRouter(equipmentsService))

const port = 3000
server.listen(port, () => {
    console.log(`Server running on port ${port}`)
})