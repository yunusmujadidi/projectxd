from datadata import *

daftar_penyakit = daftar_penyakit
daftar_deskripsi = daftar_deskripsi
deskripsi_penyakit = {}


for i in range(len(daftar_penyakit)):
    deskripsi_penyakit[daftar_penyakit[i]] = daftar_deskripsi[
        i
    ]  # gabungin daftar_penyakit dan daftar_deskripsi


def harussamapersis(nomor, penyakit, diag):
    try:
        nomor = list(nomor)
    except:
        nomor = [int(x) for x in str(nomor)]
    temp_hasil = []
    for i in range(len(diag)):
        if i in nomor:
            temp_hasil.append(diag[i])
    if temp_hasil.count("y") == len(temp_hasil) == diag.count("y"):
        return penyakit


def forwardchaining(diag):
    if diag.count("y") == 0:
        return
    elif (
        harussamapersis((0, 1, 2, 3, 12), daftar_penyakit[0], diag)
        == daftar_penyakit[0]
    ):
        return "Gastritis"
    elif (
        harussamapersis((0, 1, 3, 4, 5, 13), daftar_penyakit[1], diag)
        == daftar_penyakit[1]
    ):
        return "Dispepsia"
    elif (
        harussamapersis((0, 1, 3, 8, 9, 11, 16), daftar_penyakit[3], diag)
        == daftar_penyakit[3]
    ):
        return "GERD"
    elif (
        harussamapersis((0, 2, 3, 7, 15), daftar_penyakit[6], diag)
        == daftar_penyakit[6]
    ):
        return "Tukak Lambung"
    elif harussamapersis((0, 2), daftar_penyakit[2], diag) == daftar_penyakit[2]:
        return "Kanker Lambung"
    elif (
        harussamapersis((0, 3, 5, 8, 9, 11, 15), daftar_penyakit[4], diag)
        == daftar_penyakit[4]
    ):
        return "Gastroenteritis"
    elif harussamapersis((0, 6), daftar_penyakit[2], diag) == daftar_penyakit[2]:
        return "Kanker Lambung"
    elif harussamapersis(0, daftar_penyakit[6], diag) == daftar_penyakit[6]:
        return "Tukak Lambung"
    elif harussamapersis((1, 2), daftar_penyakit[1], diag) == daftar_penyakit[1]:
        return "Dispepsia"
    elif (
        harussamapersis((1, 2, 6, 9, 11, 13), daftar_penyakit[5], diag)
        == daftar_penyakit[5]
    ):
        return "Gastroparesis"
    elif harussamapersis((1, 3), daftar_penyakit[2], diag) == daftar_penyakit[2]:
        return "Kanker Lambung"
    elif harussamapersis((1, 5, 15), daftar_penyakit[4], diag) == daftar_penyakit[4]:
        return "Gastroenteritis"
    elif harussamapersis((1, 6), daftar_penyakit[1], diag) == daftar_penyakit[1]:
        return "Dispepsia"
    elif harussamapersis((1, 8, 15), daftar_penyakit[4], diag) == daftar_penyakit[4]:
        return "Gastroenteritis"
    elif harussamapersis((1, 10, 15), daftar_penyakit[4], diag) == daftar_penyakit[4]:
        return "Gastroenteritis"
    elif harussamapersis((1, 12), daftar_penyakit[1], diag) == daftar_penyakit[1]:
        return "Dispepsia"
    elif harussamapersis((1, 16), daftar_penyakit[3], diag) == daftar_penyakit[3]:
        return "GERD"
    elif harussamapersis(1, daftar_penyakit[5], diag) == daftar_penyakit[5]:
        return "Gastroparesis"
    elif (
        harussamapersis((2, 3, 6, 7, 11), daftar_penyakit[2], diag)
        == daftar_penyakit[2]
    ):
        return "Kanker Lambung"
    elif harussamapersis((2, 7), daftar_penyakit[2], diag) == daftar_penyakit[2]:
        return "Kanker Lambung"
    elif harussamapersis((2, 10), daftar_penyakit[1], diag) == daftar_penyakit[1]:
        return "Dispepsia"
    elif harussamapersis((2, 13), daftar_penyakit[1], diag) == daftar_penyakit[1]:
        return "Dispepsia"
    elif harussamapersis((2, 14), daftar_penyakit[2], diag) == daftar_penyakit[2]:
        return "Kanker Lambung"
    elif harussamapersis(2, daftar_penyakit[0], diag) == daftar_penyakit[0]:
        return "Gastritis"
    elif harussamapersis((3, 0), daftar_penyakit[2], diag) == daftar_penyakit[2]:
        return "Kanker Lambung"
    elif harussamapersis((3, 7), daftar_penyakit[2], diag) == daftar_penyakit[2]:
        return "Kanker Lambung"
    elif harussamapersis((3, 9), daftar_penyakit[1], diag) == daftar_penyakit[1]:
        return "Dispepsia"
    elif harussamapersis((3, 11), daftar_penyakit[2], diag) == daftar_penyakit[2]:
        return "Kanker Lambung"
    elif harussamapersis((3, 13), daftar_penyakit[1], diag) == daftar_penyakit[1]:
        return "Dispepsia"
    elif harussamapersis((3, 14), daftar_penyakit[2], diag) == daftar_penyakit[2]:
        return "Kanker Lambung"
    elif harussamapersis(3, daftar_penyakit[1], diag) == daftar_penyakit[1]:
        return "Dispepsia"
    elif harussamapersis((5, 9, 15), daftar_penyakit[4], diag) == daftar_penyakit[4]:
        return "Gastroenteritis"
    elif harussamapersis((5, 13, 15), daftar_penyakit[4], diag) == daftar_penyakit[4]:
        return "Gastroenteritis"
    elif harussamapersis((6, 7), daftar_penyakit[2], diag) == daftar_penyakit[2]:
        return "Kanker Lambung"
    elif harussamapersis((6, 9), daftar_penyakit[1], diag) == daftar_penyakit[1]:
        return "Dispepsia"
    elif harussamapersis((6, 11), daftar_penyakit[2], diag) == daftar_penyakit[2]:
        return "Kanker Lambung"
    elif harussamapersis((6, 13), daftar_penyakit[1], diag) == daftar_penyakit[1]:
        return "Dispepsia"
    elif harussamapersis((6, 14), daftar_penyakit[2], diag) == daftar_penyakit[2]:
        return "Kanker Lambung"
    elif harussamapersis(6, daftar_penyakit[1], diag) == daftar_penyakit[1]:
        return "Dispepsia"
    elif harussamapersis((7, 12), daftar_penyakit[2], diag) == daftar_penyakit[2]:
        return "Kanker Lambung"
    elif harussamapersis(7, daftar_penyakit[6], diag) == daftar_penyakit[6]:
        return "Tukak Lambung"
    elif harussamapersis((8, 9, 15), daftar_penyakit[4], diag) == daftar_penyakit[4]:
        return "Gastroenteritis"
    elif harussamapersis((8, 13, 15), daftar_penyakit[4], diag) == daftar_penyakit[4]:
        return "Gastroenteritis"
    elif harussamapersis((9, 10, 15), daftar_penyakit[4], diag) == daftar_penyakit[4]:
        return "Gastroenteritis"
    elif harussamapersis((9, 12), daftar_penyakit[1], diag) == daftar_penyakit[1]:
        return "Dispepsia"
    elif harussamapersis((9, 16), daftar_penyakit[3], diag) == daftar_penyakit[3]:
        return "GERD"
    elif harussamapersis((10, 13, 15), daftar_penyakit[4], diag) == daftar_penyakit[4]:
        return "Gastroenteritis"
    elif harussamapersis((11, 2), daftar_penyakit[2], diag) == daftar_penyakit[2]:
        return "Kanker Lambung"
    elif harussamapersis((11, 12), daftar_penyakit[2], diag) == daftar_penyakit[2]:
        return "Kanker Lambung"
    elif harussamapersis(11, daftar_penyakit[6], diag) == daftar_penyakit[6]:
        return "Tukak Lambung"
    elif harussamapersis((12, 13), daftar_penyakit[1], diag) == daftar_penyakit[1]:
        return "Dispepsia"
    elif harussamapersis((12, 14), daftar_penyakit[2], diag) == daftar_penyakit[2]:
        return "Kanker Lambung"
    elif harussamapersis(12, daftar_penyakit[0], diag) == daftar_penyakit[0]:
        return "Gastritis"
    elif harussamapersis((13, 16), daftar_penyakit[3], diag) == daftar_penyakit[3]:
        return "GERD"
    elif harussamapersis(13, daftar_penyakit[5], diag) == daftar_penyakit[5]:
        return "Gastroparesis"
    elif harussamapersis(14, daftar_penyakit[6], diag) == daftar_penyakit[6]:
        return "Tukak Lambung"
    else:
        return "tidak_tahu"


def penyakitnya(
    penyakit,
):  # Kalau tidak ada penyakit yang gejalanya sama persis dengan gejala yang dimasukkan user, maka akan dicari penyakit yang paling mendekati.
    if penyakit == "tidak_tahu":
        penyakitmu = "Mohon maaf, Dr. Magen belum mampu mendeteksi penyakit kamu 😞"
        deskripsinya = ""
    elif penyakit:
        penyakitmu = penyakit
        deskripsinya = deskripsi_penyakit[penyakit]
    else:
        penyakitmu = "Sepertinya kamu sehat-sehat saja ❤️"
        deskripsinya = ""
    return penyakitmu, deskripsinya
