!unzip -q ../train_data.zip -d ../

python3 detect.py --source 0 
python3 detect.py --source  img.jpg 
python3 detect.py --weights yolov5s.pt --source bus.jpg
python3 detect.py --weights train_model.pt --source img.jpg
python3 detect.py --weights train_model.pt --source 0
python3 detect.py --weights yolov5s.pt  --source 0

python3 export.py --weights train_model.pt --include tflite
wget https://github.com/PINTO0309/Tensorflow-bin/releases/download/v2.8.0/tensorflow-2.8.0-cp39-none-linux_aarch64.whl
python3 detect.py --weights train_model-fp16.tflite --source 0
python3 classify.py \
  --model train_model-fp16.tflite \
  --maxResults 5