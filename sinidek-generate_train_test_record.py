import subprocess
print("---------------------------------------------------\n")

namaprogram = "Sistem Informasi Deteksi Benda Berbahaya(Sini Dek Bentar)\n"
devby = "Developed by Ananda Rauf Maududi"
devdate = "18 Oktober 2021"
print(namaprogram)
print(devby)
print(devdate)

print("---------------------------------------------------\n")

bashCommand = "python sinidek-generate_tfrecord.py --csv_input=data/train.csv  --output_path=data/train.record --image_dir=(images)"
output = subprocess.check_output(['bash','-c', bashCommand])
print(output)

bashCommand = "python sinidek-generate_tfrecord.py --csv_input=data/test.csv  --output_path=data/test.record --image_dir=(images)"
output = subprocess.check_output(['bash','-c', bashCommand])
print(output)
