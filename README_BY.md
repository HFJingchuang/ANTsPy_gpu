# ANTsPy-master
## GPU-配准编译手册
### 硬件
    - GPU:RTX40系列GPU
    - CPU: i7-12700F以上
### 软件
    - windows 11
    - python 3.9
    - CMake  3.28.3以上
    - Visual Studio 2022-17.9.5
    - CUDA12.1
    - opencv
    - ANTs
### 编译和测试方法
1.检查编译的解释器中是否存在antspyx，如果存在请先卸载antspyx，并删除主目录下build和itbuild两个文件夹。
```
pip list
pip uninsatll antspyx
```

2.安装requirements.txt或者未编译的antspyx-0.4.2-cp39-cp39-win_amd64.whl（主要是antspyx所必需的python包）
```
pip install -r requirements.txt
pip install antspyx-0.4.2-cp39-cp39-win_amd64.whl
```

4.配置好环境后在控制台运行下述命令行进行编译。
```
pip setup.py install
```
5.编译完成后，运行主目录下test文件夹中test2.py和test3.py，两个测试脚本均可以正常运行说明编译成功。
### GPU-ANTs的打包和安装
1.编译成功后首先删除编译过程中产生的主目录下build和itbuild两个文件夹，然后在控制台运行下述命令行实现打包。
打包完成后会自动在主目录下生成dist文件夹，文件夹中保存安装gpu配准所需要的文件（antspyx-0.4.2-cp39-cp39-win_amd64.whl）。
```
python setup.py bdist_wheel
```
2.将打包后的antspyx-0.4.2-cp39-cp39-win_amd64.whl复制到需要的项目主目录下，运行下述命令行进行安装和卸载。
```
pip install antspyx-0.4.2-cp39-cp39-win_amd64.whl
pip uninsatll antspyx
```
