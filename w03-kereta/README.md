# Week 03: Simulasi Kereta

Program ini mensimulasikan keberangkatan kereta dan kedatangan seorang penumpang.
Objektif dari simulasi adalah menghitung probabilitas penumpang dapat naik kereta. 
Model matematika dari simulasi ini adalah sebagai berikut.
```
let tp = waktu penumpang datang
    tkb = waktu kereta berangkat
    tks = waktu kereta sampai
    tkt = waktu kereta berjalan (travel)
    nk = fungsi yang mereturn true bila penumpang bisa naik kereta
maka
    tks = tkb + tkt
    nk = tp <= tks
```
Simulasi ini akan dijalankan selama 1000 kali, lalu dihitung nilai objektifnya.
Diasumsikan variasi (+-2 menit) waktu kereta berjalan terdistribusi secara uniform.

## How to run
Program ini dibuat dengan java versi 17.0.4. Download jar program lalu jalankan command dibawah.
```shell
java -jar <nama file jar>.jar
```