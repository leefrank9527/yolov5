import openvino_tensorflow

rst = openvino_tensorflow.list_backends()
print(rst)

openvino_tensorflow.set_backend('GPU')
