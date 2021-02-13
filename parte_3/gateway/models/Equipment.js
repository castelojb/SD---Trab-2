class Equipment {
    constructor(name, type) {
        this.name = name
        this.type = type
        this.id = Math.random().toString(16).substring(2)
        this.status = undefined
        this.host = "0.0.0.0"
        this.port = 3000
    }

    setType(type) {
        this.type = type
        return this
    }

    setStatus(status) {
        this.status = status
        return this
    }

    setStatus(status) {
        this.status = status
        return this
    }

    setHost(host) {
        this.host = host
        return this
    }

    setPort(port) {
        this.port = port
        return this
    }
}

module.exports = Equipment