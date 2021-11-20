import pandas as pd
from sklearn.model_selection import train_test_split
import subprocess
print("---------------------------------------------------\n")

namaprogram = "Sistem Informasi Deteksi Benda Berbahaya(Sini Dek Bentar)\n"
devby = "Developed by Ananda Rauf Maududi"
devdate = "18 Oktober 2021"
print(namaprogram)
print(devby)
print(devdate)

print("---------------------------------------------------\n")

data_all= pd.read_csv('hasilconvert.csv')

X=data_all.drop('class', axis=1)
y=data_all['class']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.80, random_state=1010)

y_train=pd.DataFrame(y_train)
y_test=pd.DataFrame(y_test)

data_train=pd.merge(X_train,y_train,left_index=True,right_index=True)
data_test=pd.merge(X_test,y_test,left_index=True,right_index=True)

data_train.to_csv('data/train.csv')
data_test.to_csv('data/test.csv')

bashCommand = "python sinidek-generate_tfrecord.py --csv_input=data/train.csv  --output_path=data/train.record"
output = subprocess.check_output(['bash','-c', bashCommand])
print(output)

bashCommand = "python sinidek-generate_tfrecord.py --csv_input=data/test.csv  --output_path=data/test.record"
output = subprocess.check_output(['bash','-c', bashCommand])
print(output)
