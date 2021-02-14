const { Router } = require("express")
const Equipment = require("../models/Equipment")

const equipmentsRouter = new Router()

module.exports = equipmentsService => {
    equipmentsRouter
    .get("/", (req, res) => {
        let type = req.query.type
        if (type) {
            res.json(equipmentsService.getEquipmentsOfType(type))
        } else {
            res.json(equipmentsService.getEquipments())
        }
    })
    .post("/", (req, res) => {
        const newEquipment = Object.assign(new Equipment, req.body)
        equipmentsService.registerEquipment(newEquipment)
        res.status(201).json(equipmentsService.getEquipment(newEquipment.id))
    })
    .get("/:equipmentId/status", (req, res) => {
        const type = req.query.type
        equipmentsService.getEquipmentStatus(req.params.equipmentId, type)
        .then(status => res.status(200).json(status))
        .catch(error => res.status(500).json(error))
    })
    .put("/:equipmentId", (req, res) => {
        const { type, status } = req.body
        const { equipmentId } = req.params
        if (status && type) {
            equipmentsService.updateStatus(equipmentId, type, status)
            res.status(200).json(equipmentsService.getEquipment(equipmentId))
        } else {
            res.status(400).json({
                message: "Parâmetros obrigatórios: 'status' e 'type'."
            })
        }
    })

    return equipmentsRouter
}