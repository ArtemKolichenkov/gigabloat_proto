PROTOS_DIR := ./
PROTOS_FILE := ./gigabloat.proto

protos:
	@poetry run python3 -m grpc_tools.protoc -I$(PROTOS_DIR) --python_out=./gigabloat_proto --grpc_python_out=./gigabloat_proto $(PROTOS_FILE)
