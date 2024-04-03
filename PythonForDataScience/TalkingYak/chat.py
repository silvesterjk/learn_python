# Import necessary libraries
import torch

# Check available GPUs
device = torch.device("cuda" if use_cuda else "cpu")
print("Device: ",device)

use_cuda = torch.cuda.is_available()
if use_cuda:
    print('__CUDA VERSION:', torch.backends.cudnn.version())
    print('__Number CUDA Devices:', torch.cuda.device_count())
    print('__CUDA Device Name:',torch.cuda.get_device_name(0))
    print('__CUDA Device Total Memory [GB]:',torch.cuda.get_device_properties(0).total_memory/1e9)

__CUDNN VERSION: 8401
__Number CUDA Devices: 1
__CUDA Device Name: NVIDIA RTX A4000
__CUDA Device Total Memory [GB]: 16.89124864


# Your machine learning code here, utilizing Paperspace GPU
# For example, training a simple model on GPU
# model = tf.keras.Sequential([...])  # Define your model
# model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
# model.fit(train_data, train_labels, epochs=5, validation_data=(val_data, val_labels))
