## Шаги

- компилируем протокол на Python
    ```shell
    protoc --proto_path=protos --python_out=./protobufs protos/hello.proto
    ```
- компилируем протокол в Python плюс аннотации типов
    ```shell
    protoc --proto_path=protos --python_out=./protobufs --pyi_out=./protobufs protos/*.proto
    ```
- установили Python пакет `grpcio`
- установили Python пакет `grpcio-tools`
- описали сервис `Greeter`
- компилируем командой
    ```shell
    python -m grpc_tools.protoc --proto_path=protos --python_out=./protobufs --pyi_out=./protobufs --grpc_python_out=./protobufs protos/greeter.proto
    ```
- правим импорт
- реализуем сервисер
- запускаем сервер
- вызываем клиент
