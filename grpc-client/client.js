const grpc = require("@grpc/grpc-js");
const protoLoader = require("@grpc/proto-loader");
const path = require("path");

const PROTO_PATH = path.join(__dirname, "calculator.proto");
const packageDefinition = protoLoader.loadSync(PROTO_PATH, {});
const calculatorProto =
  grpc.loadPackageDefinition(packageDefinition).calculator;

function main() {
  const client = new calculatorProto.Calculator(
    "localhost:50051",
    grpc.credentials.createInsecure()
  );
  const request = { a: 4, b: 5 };

  client.Sum(request, (error, response) => {
    if (error) {
      console.error("Erro ao chamar o método Sum:", error);
      return;
    }
    console.log(`O resultado da soma é: ${response.result}`);
  });
}

main();
