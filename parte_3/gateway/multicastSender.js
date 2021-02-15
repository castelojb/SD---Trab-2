const dgram = require('dgram')
const server = dgram.createSocket('udp4')

server.bind()
// server.setMulticastTTL(128)
const host = process.env.UDP_HOST || '230.185.192.108'
server.addMembership(host)

const message = Buffer.from("where-are-you")
server.send(message, 0, message.length, process.env.UDP_PORT, host)