# ply2b3dm

## 设计初衷

由于本人实习项目的原因，需要将ply文件转换为b3dm文件，但网上没有现成的方案，所以自己写了一个。

## 设计思路

由于ply文件和b3dm文件属于不同的联盟规范文件，所以需要将ply文件转换为gltf文件，再将gltf文件转换为b3dm文件。

## 使用环境要求

python3.7（不可高也不可低）

包要求：numpy, typer, bpy

注意bpy的安装方法为
```
pip install bpy==2.91a0 && bpy_post_install
```

同时克隆 [gltf-to-3d-tiles](https://github.com/xuzhusheng/gltf-to-3d-tiles) 项目到本地，根据该项目要求配置环境，并将DataProcess.py文件放到与gltf-to-3d-tiles同级目录下。

与此同时，DataProcess.py文件的同级目录中创建名为data的文件夹，用于存放ply文件，文件夹格式应当如下：
```angular2html
--data
  |--八甲收费站
  |	  |---block1.ply
  |	  |---block2.ply
  |
  |--一号坡
       |--block1.ply
       |--block2.ply
```

## 使用方法
在DataProcess.py文件的目录中打开命令行终端（注意环境要求为python3.7），输入
```
python DataProcess.py ./data
```