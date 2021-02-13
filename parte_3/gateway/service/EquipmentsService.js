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
        this.repository.setStatus(id, status)
    }
}

module.exports = EquipmentService