class EquipmentsInMemory {
    constructor() {
        this.equipments = []
    }

    registerEquipment(newEquipment) {
        this.equipments.push(newEquipment)
    }

    getAll() {
        return this.equipments
    }

    getById(id) {
        return this.equipments.find(e => e.id === id)
    }

    removeById(id) {
        this.equipments = this.equipments.filter(e => e.id !== id)
    }

    setStatus(id, status) {
        this.equipments = this.equipments.map(e => {
            if (e.id === id) {
                e.status = status
            }
            return e
        })
    }
}

module.exports = EquipmentsInMemory