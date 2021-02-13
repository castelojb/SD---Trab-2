const EquipmentClient = require("../grpc-routes/serviceApi")

class EquipmentService {
    constructor(repository) {
        this.repository = repository
    }

    getEquipments() {
        return this.repository.getAll()
    }

    getEquipment(id) {
        return this.repository.getById(id)
    }

    getEquipmentsOfType(type) {
        return this.repository.getAll().filter(e => e.type === type)
    }

    registerEquipment(newEquipment) {
        this.repository.registerEquipment(newEquipment)
    }

    updateStatus(id, status) {
        const equipment = this.repository.getById(id)
        this.repository.setStatus(id, status)
        const client = new EquipmentClient(`${equipment.host}:${equipment.port}`,
                                       grpc.credentials.createInsecure())
        client.ReceiveUpdate({
            eventType: "atualização",
            payload: status
        }, )
    }
}

module.exports = EquipmentService