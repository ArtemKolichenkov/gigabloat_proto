PROTOS_DIR := ./
PROTOS_FILE := ./gigabloat.proto

protos:
	@poetry run python3 -m grpc_tools.protoc -I$(PROTOS_DIR) --python_out=./protobloat --grpc_python_out=./protobloat $(PROTOS_FILE)
