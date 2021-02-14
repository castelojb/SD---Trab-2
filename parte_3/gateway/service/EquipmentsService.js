const EquipmentClient = require("../grpc-routes/equipmentClient")
const grpc = require("@grpc/grpc-js")

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

    getEquipmentStatus(id, type) {
        const equipment = this.repository.getById(id)
        const client = new EquipmentClient(`${equipment.ip}:${equipment.port}`,
                                       grpc.credentials.createInsecure())
        return new Promise((resolve, reject) => {
            client.GetStatus({
                type
            }, (error, response) => {
                if (error) return reject(error)
                resolve(response)
            })
        })
    }

    getEquipmentsOfType(type) {
        return this.repository.getAll().filter(e => e.type === type)
    }

    registerEquipment(newEquipment) {
        this.repository.registerEquipment(newEquipment)
    }

    updateStatus(id, type, status) {
        const equipment = this.repository.getById(id)
        this.repository.setStatus(id, type, status)
        const client = new EquipmentClient(`${equipment.ip}:${equipment.port}`,
                                       grpc.credentials.createInsecure())
        client.ReceiveUpdate({
            type,
            payload: status
        }, (error, response) => {
            if (error) return console.error(error)
            console.log(response)
        })
    }
}

module.exports = EquipmentService