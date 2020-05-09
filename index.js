var protoLoader = require('@grpc/proto-loader');
var PROTO_PATH = __dirname + '/gigabloat.proto';
var packageDefinition = protoLoader.loadSync(
    PROTO_PATH,
    {
        keepCase: true,
        longs: String,
        enums: String,
        defaults: true,
        oneofs: true
    });

exports.gigabloatDefinition = packageDefinition