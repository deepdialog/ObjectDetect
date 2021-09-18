# Simple Object Detect

## Install

```bash
$ pip install object-detect
```

## Usage

```python
>>> import object_detect
>>> object_detect.predict('pingguo.png')
[{'score': 0.7782772, 'cls': 'apple', 'box': array([ 60.206234,  68.00511 , 231.40326 , 188.97191 ], dtype=float32)}, {'score': 0.73667014, 'cls': 'apple', 'box': array([144.23593, 294.85623, 318.25494, 431.44476], dtype=float32)}, {'score': 0.67745084, 'cls': 'apple', 'box': array([166.161  , 177.62476, 347.23557, 308.32822], dtype=float32)}, {'score': 0.58755594, 'cls': 'apple', 'box': array([ 49.135155, 177.81197 , 209.82591 , 306.37067 ], dtype=float32)}]
```

## Model

tfhub

```
python3 -m tf2onnx.convert --opset 13 --tflite lite-model_yolo-v5-tflite_tflite_model_1.tflite --output model.onnx
```

## Classes

Support 80 classes

```
person
bicycle
car
motorbike
aeroplane
bus
train
truck
boat
traffic light
fire hydrant
stop sign
parking meter
bench
bird
cat
dog
horse
sheep
cow
elephant
bear
zebra
giraffe
backpack
umbrella
handbag
tie
suitcase
frisbee
skis
snowboard
sports ball
kite
baseball bat
baseball glove
skateboard
surfboard
tennis racket
bottle
wine glass
cup
fork
knife
spoon
bowl
banana
apple
sandwich
orange
broccoli
carrot
hot dog
pizza
donut
cake
chair
sofa
pottedplant
bed
diningtable
toilet
tvmonitor
laptop
mouse
remote
keyboard
cell phone
microwave
oven
toaster
sink
refrigerator
book
clock
vase
scissors
teddy bear
hair drier
toothbrush
```

```
人
自行车
车
摩托车
飞机
公共汽车
火车
卡车
船
红绿灯
消防栓
停止标志
停车收费表
长椅
鸟
猫
狗
马
羊
奶牛
大象
熊
斑马
长颈鹿
背包
伞
手提包
领带
手提箱
飞盘
滑雪板
滑雪板
运动球
风筝
棒球棒
棒球手套
滑板
冲浪板
网球拍
瓶子
红酒杯
杯子
叉子
刀
勺子
碗
香蕉
苹果
三明治
橘子
西兰花
萝卜
热狗
比萨
甜甜圈
蛋糕
椅子
沙发
盆栽植物
床
餐桌
洗手间
电视监视器
笔记本电脑
鼠
偏僻的
键盘
手机
微波
烤箱
烤面包机
下沉
冰箱
书
时钟
花瓶
剪刀
玩具熊
吹风机
牙刷
```
