SRC_DIR=/home/joao/WorkspacePython/SD---Trab-2/parte_3/
DST_DIR=/home/joao/WorkspacePython/SD---Trab-2/parte_3/


#sudo protoc -I=$SRC_DIR --python_out=$DST_DIR $SRC_DIR/Protobuffer/messages.proto

python -m grpc_tools.protoc -I. --python_out=Protobuffer/ --grpc_python_out=. Protobuffer/messages.proto
