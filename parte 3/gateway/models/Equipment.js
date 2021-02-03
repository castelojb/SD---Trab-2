class Equipment {
    constructor(type) {
        this.type = type
        this.id = Math.random().toString(16).substring(2)
        this.status = ""
    }
}

module.exports = Equipment