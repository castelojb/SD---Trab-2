const Equipment = require("../models/Equipment")

module.exports = service => {
    Identificate(call, callback) {
        const info = call.request
        const equipment = new Equipment(info.type)
        .setHost(info.host)
        .setPort(info.port)
        service.registerEquipment(newEquipment)
        callback(null, call.request)
    },
    ReceiveStatus(call) {
        console.log(call)
    }
}