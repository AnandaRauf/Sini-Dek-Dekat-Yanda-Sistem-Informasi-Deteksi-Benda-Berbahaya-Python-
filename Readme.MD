Sini Dek Dekat Yanda V1
------------------------------------------------------------------------------------------------------------------------------

Deveveloped by Ananda Rauf Maududi
Developed date : 17 November 2021

------------------------------------------------------------------------------------------------------------------------------
![Sini Dek Dekat Yanda](https://raw.githubusercontent.com/AnandaRauf/Sini-Dek-Dekat-Yanda-Sistem-Informasi-Deteksi-Benda-Berbahaya-Python-/project/workflow.png)

Requirement :

- Python min versi 3.7  max new version, download here : https://www.python.org/downloads
- Library Package : Tensorflow : tensorflow==1.15.0 non GPU NVDIA Ge Force Cuda, GPU NVDIA Ge Force : tensorflow-gpu==1.15.0. absl, opencv-python, opencv-contrib-python, and tensorflow-object-detection-api.
- Install library with using pip install name library.
- LblIMG, download and then extract file rar/zip:
- Tensorflow Model Official API, dowload and then extract file rar/zip :

Step by step using program :
- Setting Environment Variable in System : New with name : PYTHONPATH variabel path models/research;models/research/slim;models/research/object_detection
- Extract file protoc-3-4-0.zip to folder model>research
- typing in CMD or Terminal Linux/Ubuntu : protoc object_detection/protos/*.proto --python_out=.
- Train your new image object by using labelImg : Go to folder labelImg and then typing in CMD or Terminal Linux/Ubuntu: python labelIMG.py < for python 3.9(New Version) for version 3.7.0 and 2.7 : py labelIMG.py 
- After train image, then run program sinidek-xml2csv.
- After run program xml2csv, output program is hasilconvert.csv and then run program sinidek-split_train_test and checking data in script sinidek-generate_tfrecord editing line 41-56.
- After run program split train test and checking script,then run program script sinidek-generate_train_test.py or copy paste string 'python' you can search using CTRL+F.
- After run program generate train test, then editing script SSD Mobile v1 pets.confiq, editing amount data labels, in confiq using my data model by amount 8, and editing numsteps < you can deleted for unlinimited loop train for efective result, you can exit using CTRL+C or ALT+F4.
- After editing SSD Mobile v1 pets confiq, then run program sinidek-train.py.
- After run program sinidek-train.py.
- Finallay run program sinidek.py.

Have any bugs in my program or confused my tutorial documentation?

See more documentation with using languange Indonesian:
https://medium.com/@hafizhan.aliady/pre-instalasi-tensorflow-api-object-detection-fa1e78155aa4
https://medium.com/@hafizhan.aliady/lihat-apa-yang-ada-di-box-hijau-begini-cara-membuat-object-detection-menggunakan-tensorflow-api-6d4a6d44e1a
