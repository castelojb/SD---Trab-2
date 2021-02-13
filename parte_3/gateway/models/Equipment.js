class Equipment {
    constructor(type) {
        this.type = type
        this.id = Math.random().toString(16).substring(2)
        this.status = ""
        this.host = "0.0.0.0"
        this.port = 3000
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