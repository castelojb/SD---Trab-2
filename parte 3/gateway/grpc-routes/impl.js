module.exports = {
    Identificate(call, callback) {
        callback(null, call.request)
    },
    ReceiveStatus(call) {
        console.log(call)
    }
}