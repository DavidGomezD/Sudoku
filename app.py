import random
#Mi libreria 
from codigo import sudoku
#Necesario para el uso de Flask
from flask import Flask, render_template, request
app = Flask(__name__)

fila_1 = sudoku.fun_fila_1()
fila_2 = sudoku.fun_fila_2()
fila_3 = sudoku.fun_fila_3()
fila_4 = sudoku.fun_fila_4()
fila_5 = sudoku.fun_fila_5()
fila_6 = sudoku.fun_fila_6()
fila_7 = sudoku.fun_fila_7()
fila_8 = sudoku.fun_fila_8()
fila_9 = sudoku.fun_fila_9()

n1_f1 = fila_1[0]
n2_f1 = fila_1[1]
n3_f1 = fila_1[2]
n4_f1 = fila_1[3]
n5_f1 = fila_1[4]
n6_f1 = fila_1[5]
n7_f1 = fila_1[6]
n8_f1 = fila_1[7]
n9_f1 = fila_1[8]

n1_f2 = fila_2[0]
n2_f2 = fila_2[1]
n3_f2 = fila_2[2]
n4_f2 = fila_2[3]
n5_f2 = fila_2[4]
n6_f2 = fila_2[5]
n7_f2 = fila_2[6]
n8_f2 = fila_2[7]
n9_f2 = fila_2[8]

n1_f3 = fila_3[0]
n2_f3 = fila_3[1]
n3_f3 = fila_3[2]
n4_f3 = fila_3[3]
n5_f3 = fila_3[4]
n6_f3 = fila_3[5]
n7_f3 = fila_3[6]
n8_f3 = fila_3[7]
n9_f3 = fila_3[8]

n1_f4 = fila_4[0]
n2_f4 = fila_4[1]
n3_f4 = fila_4[2]
n4_f4 = fila_4[3]
n5_f4 = fila_4[4]
n6_f4 = fila_4[5]
n7_f4 = fila_4[6]
n8_f4 = fila_4[7]
n9_f4 = fila_4[8]

n1_f5 = fila_5[0]
n2_f5 = fila_5[1]
n3_f5 = fila_5[2]
n4_f5 = fila_5[3]
n5_f5 = fila_5[4]
n6_f5 = fila_5[5]
n7_f5 = fila_5[6]
n8_f5 = fila_5[7]
n9_f5 = fila_5[8]

n1_f6 = fila_6[0]
n2_f6 = fila_6[1]
n3_f6 = fila_6[2]
n4_f6 = fila_6[3]
n5_f6 = fila_6[4]
n6_f6 = fila_6[5]
n7_f6 = fila_6[6]
n8_f6 = fila_6[7]
n9_f6 = fila_6[8]

n1_f7 = fila_7[0]
n2_f7 = fila_7[1]
n3_f7 = fila_7[2]
n4_f7 = fila_7[3]
n5_f7 = fila_7[4]
n6_f7 = fila_7[5]
n7_f7 = fila_7[6]
n8_f7 = fila_7[7]
n9_f7 = fila_7[8]

n1_f8 = fila_8[0]
n2_f8 = fila_8[1]
n3_f8 = fila_8[2]
n4_f8 = fila_8[3]
n5_f8 = fila_8[4]
n6_f8 = fila_8[5]
n7_f8 = fila_8[6]
n8_f8 = fila_8[7]
n9_f8 = fila_8[8]

n1_f9 = fila_9[0]
n2_f9 = fila_9[1]
n3_f9 = fila_9[2]
n4_f9 = fila_9[3]
n5_f9 = fila_9[4]
n6_f9 = fila_9[5]
n7_f9 = fila_9[6]
n8_f9 = fila_9[7]
n9_f9 = fila_9[8]

#Esta es una ruta 
@app.route("/")
def index():

    #Dificultad (dificil 1.. 5 facil)
    dificultad = 20

    aleatorio_0 = random.randint(0, dificultad)
    aleatorio_1 = random.randint(0, dificultad)
    aleatorio_2 = random.randint(0, dificultad)
    aleatorio_3 = random.randint(0, dificultad)
    aleatorio_4 = random.randint(0, dificultad)
    aleatorio_5 = random.randint(0, dificultad)
    aleatorio_6 = random.randint(0, dificultad)
    aleatorio_7 = random.randint(0, dificultad)
    aleatorio_8 = random.randint(0, dificultad)
    aleatorio_9 = random.randint(0, dificultad)
    aleatorio_10 = random.randint(0, dificultad)
    aleatorio_11 = random.randint(0, dificultad)
    aleatorio_12 = random.randint(0, dificultad)
    aleatorio_13 = random.randint(0, dificultad)
    aleatorio_14 = random.randint(0, dificultad)
    aleatorio_15 = random.randint(0, dificultad)
    aleatorio_16 = random.randint(0, dificultad)
    aleatorio_17 = random.randint(0, dificultad)
    aleatorio_18 = random.randint(0, dificultad)
    aleatorio_19 = random.randint(0, dificultad)
    aleatorio_20 = random.randint(0, dificultad)
    aleatorio_21 = random.randint(0, dificultad)
    aleatorio_22 = random.randint(0, dificultad)
    aleatorio_23 = random.randint(0, dificultad)
    aleatorio_24 = random.randint(0, dificultad)
    aleatorio_25 = random.randint(0, dificultad)
    aleatorio_26 = random.randint(0, dificultad)
    aleatorio_27 = random.randint(0, dificultad)
    aleatorio_28 = random.randint(0, dificultad)
    aleatorio_29 = random.randint(0, dificultad)
    aleatorio_30 = random.randint(0, dificultad)
    aleatorio_31 = random.randint(0, dificultad)
    aleatorio_32 = random.randint(0, dificultad)
    aleatorio_33 = random.randint(0, dificultad)
    aleatorio_34 = random.randint(0, dificultad)
    aleatorio_35 = random.randint(0, dificultad)
    aleatorio_36 = random.randint(0, dificultad)
    aleatorio_37 = random.randint(0, dificultad)
    aleatorio_38 = random.randint(0, dificultad)
    aleatorio_39 = random.randint(0, dificultad)
    aleatorio_40 = random.randint(0, dificultad)
    aleatorio_41 = random.randint(0, dificultad)
    aleatorio_42 = random.randint(0, dificultad)
    aleatorio_43 = random.randint(0, dificultad)
    aleatorio_44 = random.randint(0, dificultad)
    aleatorio_45 = random.randint(0, dificultad)
    aleatorio_46 = random.randint(0, dificultad)
    aleatorio_47 = random.randint(0, dificultad)
    aleatorio_48 = random.randint(0, dificultad)
    aleatorio_49 = random.randint(0, dificultad)
    aleatorio_50 = random.randint(0, dificultad)
    aleatorio_51 = random.randint(0, dificultad)
    aleatorio_52 = random.randint(0, dificultad)
    aleatorio_53 = random.randint(0, dificultad)
    aleatorio_54 = random.randint(0, dificultad)
    aleatorio_55 = random.randint(0, dificultad)
    aleatorio_56 = random.randint(0, dificultad)
    aleatorio_57 = random.randint(0, dificultad)
    aleatorio_58 = random.randint(0, dificultad)
    aleatorio_59 = random.randint(0, dificultad)
    aleatorio_60 = random.randint(0, dificultad)
    aleatorio_61 = random.randint(0, dificultad)
    aleatorio_62 = random.randint(0, dificultad)
    aleatorio_63 = random.randint(0, dificultad)
    aleatorio_64 = random.randint(0, dificultad)
    aleatorio_65 = random.randint(0, dificultad)
    aleatorio_66 = random.randint(0, dificultad)
    aleatorio_67 = random.randint(0, dificultad)
    aleatorio_68 = random.randint(0, dificultad)
    aleatorio_69 = random.randint(0, dificultad)
    aleatorio_70 = random.randint(0, dificultad)
    aleatorio_71 = random.randint(0, dificultad)
    aleatorio_72 = random.randint(0, dificultad)
    aleatorio_73 = random.randint(0, dificultad)
    aleatorio_74 = random.randint(0, dificultad)
    aleatorio_75 = random.randint(0, dificultad)
    aleatorio_76 = random.randint(0, dificultad)
    aleatorio_77 = random.randint(0, dificultad)
    aleatorio_78 = random.randint(0, dificultad)
    aleatorio_79 = random.randint(0, dificultad)
    aleatorio_80 = random.randint(0, dificultad)
    
    #Plantilla en HTML
    return render_template("index.html", 
        fila_1=fila_1, 
        fila_2=fila_2, 
        fila_3=fila_3, 
        fila_4=fila_4, 
        fila_5=fila_5, 
        fila_6=fila_6, 
        fila_7=fila_7, 
        fila_8=fila_8, 
        fila_9=fila_9,
        n1_f1=n1_f1,
        n2_f1=n2_f1,
        n3_f1=n3_f1,
        n4_f1=n4_f1,
        n5_f1=n5_f1,
        n6_f1=n6_f1,
        n7_f1=n7_f1,
        n8_f1=n8_f1,
        n9_f1=n9_f1,
        n1_f2=n1_f2,
        n2_f2=n2_f2,
        n3_f2=n3_f2,
        n4_f2=n4_f2,
        n5_f2=n5_f2,
        n6_f2=n6_f2,
        n7_f2=n7_f2,
        n8_f2=n8_f2,
        n9_f2=n9_f2,
        n1_f3=n1_f3,
        n2_f3=n2_f3,
        n3_f3=n3_f3,
        n4_f3=n4_f3,
        n5_f3=n5_f3,
        n6_f3=n6_f3,
        n7_f3=n7_f3,
        n8_f3=n8_f3,
        n9_f3=n9_f3,
        n1_f4=n1_f4,
        n2_f4=n2_f4,
        n3_f4=n3_f4,
        n4_f4=n4_f4,
        n5_f4=n5_f4,
        n6_f4=n6_f4,
        n7_f4=n7_f4,
        n8_f4=n8_f4,
        n9_f4=n9_f4,
        n1_f5=n1_f5,
        n2_f5=n2_f5,
        n3_f5=n3_f5,
        n4_f5=n4_f5,
        n5_f5=n5_f5,
        n6_f5=n6_f5,
        n7_f5=n7_f5,
        n8_f5=n8_f5,
        n9_f5=n9_f5,
        n1_f6=n1_f6,
        n2_f6=n2_f6,
        n3_f6=n3_f6,
        n4_f6=n4_f6,
        n5_f6=n5_f6,
        n6_f6=n6_f6,
        n7_f6=n7_f6,
        n8_f6=n8_f6,
        n9_f6=n9_f6,
        n1_f7=n1_f7,
        n2_f7=n2_f7,
        n3_f7=n3_f7,
        n4_f7=n4_f7,
        n5_f7=n5_f7,
        n6_f7=n6_f7,
        n7_f7=n7_f7,
        n8_f7=n8_f7,
        n9_f7=n9_f7,
        n1_f8=n1_f8,
        n2_f8=n2_f8,
        n3_f8=n3_f8,
        n4_f8=n4_f8,
        n5_f8=n5_f8,
        n6_f8=n6_f8,
        n7_f8=n7_f8,
        n8_f8=n8_f8,
        n9_f8=n9_f8,
        n1_f9=n1_f9,
        n2_f9=n2_f9,
        n3_f9=n3_f9,
        n4_f9=n4_f9,
        n5_f9=n5_f9,
        n6_f9=n6_f9,
        n7_f9=n7_f9,
        n8_f9=n8_f9,
        n9_f9=n9_f9,
        aleatorio_0=aleatorio_0,
        aleatorio_1=aleatorio_1,
        aleatorio_2=aleatorio_2,
        aleatorio_3=aleatorio_3,
        aleatorio_4=aleatorio_4,
        aleatorio_5=aleatorio_5,
        aleatorio_6=aleatorio_6,
        aleatorio_7=aleatorio_7,
        aleatorio_8=aleatorio_8,
        aleatorio_9=aleatorio_9,
        aleatorio_10=aleatorio_10,
        aleatorio_11=aleatorio_11,
        aleatorio_12=aleatorio_12,
        aleatorio_13=aleatorio_13,
        aleatorio_14=aleatorio_14,
        aleatorio_15=aleatorio_15,
        aleatorio_16=aleatorio_16,
        aleatorio_17=aleatorio_17,
        aleatorio_18=aleatorio_18,
        aleatorio_19=aleatorio_19,
        aleatorio_20=aleatorio_20,
        aleatorio_21=aleatorio_21,
        aleatorio_22=aleatorio_22,
        aleatorio_23=aleatorio_23,
        aleatorio_24=aleatorio_24,
        aleatorio_25=aleatorio_25,
        aleatorio_26=aleatorio_26,
        aleatorio_27=aleatorio_27,
        aleatorio_28=aleatorio_28,
        aleatorio_29=aleatorio_29,
        aleatorio_30=aleatorio_30,
        aleatorio_31=aleatorio_31,
        aleatorio_32=aleatorio_32,
        aleatorio_33=aleatorio_33,
        aleatorio_34=aleatorio_34,
        aleatorio_35=aleatorio_35,
        aleatorio_36=aleatorio_36,
        aleatorio_37=aleatorio_37,
        aleatorio_38=aleatorio_38,
        aleatorio_39=aleatorio_39,
        aleatorio_40=aleatorio_40,
        aleatorio_41=aleatorio_41,
        aleatorio_42=aleatorio_42,
        aleatorio_43=aleatorio_43,
        aleatorio_44=aleatorio_44,
        aleatorio_45=aleatorio_45,
        aleatorio_46=aleatorio_46,
        aleatorio_47=aleatorio_47,
        aleatorio_48=aleatorio_48,
        aleatorio_49=aleatorio_49,
        aleatorio_50=aleatorio_50,
        aleatorio_51=aleatorio_51,
        aleatorio_52=aleatorio_52,
        aleatorio_53=aleatorio_53,
        aleatorio_54=aleatorio_54,
        aleatorio_55=aleatorio_55,
        aleatorio_56=aleatorio_56,
        aleatorio_57=aleatorio_57,
        aleatorio_58=aleatorio_58,
        aleatorio_59=aleatorio_59,
        aleatorio_60=aleatorio_60,
        aleatorio_61=aleatorio_61,
        aleatorio_62=aleatorio_62,
        aleatorio_63=aleatorio_63,
        aleatorio_64=aleatorio_64,
        aleatorio_65=aleatorio_65,
        aleatorio_66=aleatorio_66,
        aleatorio_67=aleatorio_67,
        aleatorio_68=aleatorio_68,
        aleatorio_69=aleatorio_69,
        aleatorio_70=aleatorio_70,
        aleatorio_71=aleatorio_71,
        aleatorio_72=aleatorio_72,
        aleatorio_73=aleatorio_73,
        aleatorio_74=aleatorio_74,
        aleatorio_75=aleatorio_75,
        aleatorio_76=aleatorio_76,
        aleatorio_77=aleatorio_77,
        aleatorio_78=aleatorio_78,
        aleatorio_79=aleatorio_79,
        aleatorio_80=aleatorio_80)

@app.route("/resultado",  methods=["POST"])
def resultado():
 
    res_n1_f1 = ""
    res_n2_f1 = ""
    res_n3_f1 = ""
    res_n4_f1 = ""
    res_n5_f1 = ""
    res_n6_f1 = ""
    res_n7_f1 = ""
    res_n8_f1 = ""
    res_n9_f1 = ""
    res_n1_f2 = ""
    res_n2_f2 = ""
    res_n3_f2 = ""
    res_n4_f2 = ""
    res_n5_f2 = ""
    res_n6_f2 = ""
    res_n7_f2 = ""
    res_n8_f2 = ""
    res_n9_f2 = ""
    res_n1_f3 = ""
    res_n2_f3 = ""
    res_n3_f3 = ""
    res_n4_f3 = ""
    res_n5_f3 = ""
    res_n6_f3 = ""
    res_n7_f3 = ""
    res_n8_f3 = ""
    res_n9_f3 = ""
    res_n1_f4 = ""
    res_n2_f4 = ""
    res_n3_f4 = ""
    res_n4_f4 = ""
    res_n5_f4 = ""
    res_n6_f4 = ""
    res_n7_f4 = ""
    res_n8_f4 = ""
    res_n9_f4 = ""
    res_n1_f5 = ""
    res_n2_f5 = ""
    res_n3_f5 = ""
    res_n4_f5 = ""
    res_n5_f5 = ""
    res_n6_f5 = ""
    res_n7_f5 = ""
    res_n8_f5 = ""
    res_n9_f5 = ""
    res_n1_f6 = ""
    res_n2_f6 = ""
    res_n3_f6 = ""
    res_n4_f6 = ""
    res_n5_f6 = ""
    res_n6_f6 = ""
    res_n7_f6 = ""
    res_n8_f6 = ""
    res_n9_f6 = ""
    res_n1_f7 = ""
    res_n2_f7 = ""
    res_n3_f7 = ""
    res_n4_f7 = ""
    res_n5_f7 = ""
    res_n6_f7 = ""
    res_n7_f7 = ""
    res_n8_f7 = ""
    res_n9_f7 = ""
    res_n1_f8 = ""
    res_n2_f8 = ""
    res_n3_f8 = ""
    res_n4_f8 = ""
    res_n5_f8 = ""
    res_n6_f8 = ""
    res_n7_f8 = ""
    res_n8_f8 = ""
    res_n9_f8 = ""
    res_n1_f9 = ""
    res_n2_f9 = ""
    res_n3_f9 = ""
    res_n4_f9 = ""
    res_n5_f9 = ""
    res_n6_f9 = ""
    res_n7_f9 = ""
    res_n8_f9 = ""
    res_n9_f9 = ""

    r_n1_f1 = request.form.get("n1_f1")
    r_n2_f1 = request.form.get("n2_f1")
    r_n3_f1 = request.form.get("n3_f1")
    r_n4_f1 = request.form.get("n4_f1")
    r_n5_f1 = request.form.get("n5_f1")
    r_n6_f1 = request.form.get("n6_f1")
    r_n7_f1 = request.form.get("n7_f1")
    r_n8_f1 = request.form.get("n8_f1")
    r_n9_f1 = request.form.get("n9_f1")
    r_n1_f2 = request.form.get("n1_f2")
    r_n2_f2 = request.form.get("n2_f2")
    r_n3_f2 = request.form.get("n3_f2")
    r_n4_f2 = request.form.get("n4_f2")
    r_n5_f2 = request.form.get("n5_f2")
    r_n6_f2 = request.form.get("n6_f2")
    r_n7_f2 = request.form.get("n7_f2")
    r_n8_f2 = request.form.get("n8_f2")
    r_n9_f2 = request.form.get("n9_f2")
    r_n1_f3 = request.form.get("n1_f3")
    r_n2_f3 = request.form.get("n2_f3")
    r_n3_f3 = request.form.get("n3_f3")
    r_n4_f3 = request.form.get("n4_f3")
    r_n5_f3 = request.form.get("n5_f3")
    r_n6_f3 = request.form.get("n6_f3")
    r_n7_f3 = request.form.get("n7_f3")
    r_n8_f3 = request.form.get("n8_f3")
    r_n9_f3 = request.form.get("n9_f3")
    r_n1_f4 = request.form.get("n1_f4")
    r_n2_f4 = request.form.get("n2_f4")
    r_n3_f4 = request.form.get("n3_f4")
    r_n4_f4 = request.form.get("n4_f4")
    r_n5_f4 = request.form.get("n5_f4")
    r_n6_f4 = request.form.get("n6_f4")
    r_n7_f4 = request.form.get("n7_f4")
    r_n8_f4 = request.form.get("n8_f4")
    r_n9_f4 = request.form.get("n9_f4")
    r_n1_f5 = request.form.get("n1_f5")
    r_n2_f5 = request.form.get("n2_f5")
    r_n3_f5 = request.form.get("n3_f5")
    r_n4_f5 = request.form.get("n4_f5")
    r_n5_f5 = request.form.get("n5_f5")
    r_n6_f5 = request.form.get("n6_f5")
    r_n7_f5 = request.form.get("n7_f5")
    r_n8_f5 = request.form.get("n8_f5")
    r_n9_f5 = request.form.get("n9_f5")
    r_n1_f6 = request.form.get("n1_f6")
    r_n2_f6 = request.form.get("n2_f6")
    r_n3_f6 = request.form.get("n3_f6")
    r_n4_f6 = request.form.get("n4_f6")
    r_n5_f6 = request.form.get("n5_f6")
    r_n6_f6 = request.form.get("n6_f6")
    r_n7_f6 = request.form.get("n7_f6")
    r_n8_f6 = request.form.get("n8_f6")
    r_n9_f6 = request.form.get("n9_f6")
    r_n1_f7 = request.form.get("n1_f7")
    r_n2_f7 = request.form.get("n2_f7")
    r_n3_f7 = request.form.get("n3_f7")
    r_n4_f7 = request.form.get("n4_f7")
    r_n5_f7 = request.form.get("n5_f7")
    r_n6_f7 = request.form.get("n6_f7")
    r_n7_f7 = request.form.get("n7_f7")
    r_n8_f7 = request.form.get("n8_f7")
    r_n9_f7 = request.form.get("n9_f7")
    r_n1_f8 = request.form.get("n1_f8")
    r_n2_f8 = request.form.get("n2_f8")
    r_n3_f8 = request.form.get("n3_f8")
    r_n4_f8 = request.form.get("n4_f8")
    r_n5_f8 = request.form.get("n5_f8")
    r_n6_f8 = request.form.get("n6_f8")
    r_n7_f8 = request.form.get("n7_f8")
    r_n8_f8 = request.form.get("n8_f8")
    r_n9_f8 = request.form.get("n9_f8")
    r_n1_f9 = request.form.get("n1_f9")
    r_n2_f9 = request.form.get("n2_f9")
    r_n3_f9 = request.form.get("n3_f9")
    r_n4_f9 = request.form.get("n4_f9")
    r_n5_f9 = request.form.get("n5_f9")
    r_n6_f9 = request.form.get("n6_f9")
    r_n7_f9 = request.form.get("n7_f9")
    r_n8_f9 = request.form.get("n8_f9")
    r_n9_f9 = request.form.get("n9_f9")

    if int(r_n1_f1) == int(n1_f1):
        res_n1_f1 = n1_f1
    else:
        res_n1_f1 = "X"

    if int(r_n2_f1) == int(n2_f1):
        res_n2_f1 = n2_f1
    else:
        res_n2_f1 = "X"

    if int(r_n3_f1) == int(n3_f1):
        res_n3_f1 = n3_f1
    else:
        res_n3_f1 = "X"

    if int(r_n4_f1) == int(n4_f1):
        res_n4_f1 = n4_f1
    else:
        res_n4_f1 = "X"

    if int(r_n5_f1) == int(n5_f1):
        res_n5_f1 = n5_f1
    else:
        res_n5_f1 = "X"

    if int(r_n6_f1) == int(n6_f1):
        res_n6_f1 = n6_f1
    else:
        res_n6_f1 = "X"

    if int(r_n7_f1) == int(n7_f1):
        res_n7_f1 = n7_f1
    else:
        res_n7_f1 = "X"

    if int(r_n8_f1) == int(n8_f1):
        res_n8_f1 = n8_f1
    else:
        res_n8_f1 = "X"

    if int(r_n9_f1) == int(n9_f1):
        res_n9_f1 = n9_f1
    else:
        res_n9_f1 = "X"

    if int(r_n1_f2) == int(n1_f2):
        res_n1_f2 = n1_f2
    else:
        res_n1_f2 = "X"

    if int(r_n2_f2) == int(n2_f2):
        res_n2_f2 = n2_f2
    else:
        res_n2_f2 = "X"

    if int(r_n3_f2) == int(n3_f2):
        res_n3_f2 = n3_f2
    else:
        res_n3_f2 = "X"

    if int(r_n4_f2) == int(n4_f2):
        res_n4_f2 = n4_f2
    else:
        res_n4_f2 = "X"

    if int(r_n5_f2) == int(n5_f2):
        res_n5_f2 = n5_f2
    else:
        res_n5_f2 = "X"

    if int(r_n6_f2) == int(n6_f2):
        res_n6_f2 = n6_f2
    else:
        res_n6_f2 = "X"

    if int(r_n7_f2) == int(n7_f2):
        res_n7_f2 = n7_f2
    else:
        res_n7_f2 = "X"

    if int(r_n8_f2) == int(n8_f2):
        res_n8_f2 = n8_f2
    else:
        res_n8_f2 = "X"

    if int(r_n9_f2) == int(n9_f2):
        res_n9_f2 = n9_f2
    else:
        res_n9_f2 = "X"

    if int(r_n1_f3) == int(n1_f3):
        res_n1_f3 = n1_f3
    else:
        res_n1_f3 = "X"

    if int(r_n2_f3) == int(n2_f3):
        res_n2_f3 = n2_f3
    else:
        res_n2_f3 = "X"

    if int(r_n3_f3) == int(n3_f3):
        res_n3_f3 = n3_f3
    else:
        res_n3_f3 = "X"

    if int(r_n4_f3) == int(n4_f3):
        res_n4_f3 = n4_f3
    else:
        res_n4_f3 = "X"

    if int(r_n5_f3) == int(n5_f3):
        res_n5_f3 = n5_f3
    else:
        res_n5_f3 = "X"

    if int(r_n6_f3) == int(n6_f3):
        res_n6_f3 = n6_f3
    else:
        res_n6_f3 = "X"

    if int(r_n7_f3) == int(n7_f3):
        res_n7_f3 = n7_f3
    else:
        res_n7_f3 = "X"

    if int(r_n8_f3) == int(n8_f3):
        res_n8_f3 = n8_f3
    else:
        res_n8_f3 = "X"

    if int(r_n9_f3) == int(n9_f3):
        res_n9_f3 = n9_f3
    else:
        res_n9_f3 = "X"

    if int(r_n1_f4) == int(n1_f4):
        res_n1_f4 = n1_f4
    else:
        res_n1_f4 = "X"

    if int(r_n2_f4) == int(n2_f4):
        res_n2_f4 = n2_f4
    else:
        res_n2_f4 = "X"

    if int(r_n3_f4) == int(n3_f4):
        res_n3_f4 = n3_f4
    else:
        res_n3_f4 = "X"

    if int(r_n4_f4) == int(n4_f4):
        res_n4_f4 = n4_f4
    else:
        res_n4_f4 = "X"

    if int(r_n5_f4) == int(n5_f4):
        res_n5_f4 = n5_f4
    else:
        res_n5_f4 = "X"

    if int(r_n6_f4) == int(n6_f4):
        res_n6_f4 = n6_f4
    else:
        res_n6_f4 = "X"

    if int(r_n7_f4) == int(n7_f4):
        res_n7_f4 = n7_f4
    else:
        res_n7_f4 = "X"

    if int(r_n8_f4) == int(n8_f4):
        res_n8_f4 = n8_f4
    else:
        res_n8_f4 = "X"

    if int(r_n9_f4) == int(n9_f4):
        res_n9_f4 = n9_f4
    else:
        res_n9_f4 = "X"

    if int(r_n1_f5) == int(n1_f5):
        res_n1_f5 = n1_f5
    else:
        res_n1_f5 = "X"

    if int(r_n2_f5) == int(n2_f5):
        res_n2_f5 = n2_f5
    else:
        res_n2_f5 = "X"

    if int(r_n3_f5) == int(n3_f5):
        res_n3_f5 = n3_f5
    else:
        res_n3_f5 = "X"

    if int(r_n4_f5) == int(n4_f5):
        res_n4_f5 = n4_f5
    else:
        res_n4_f5 = "X"

    if int(r_n5_f5) == int(n5_f5):
        res_n5_f5 = n5_f5
    else:
        res_n5_f5 = "X"

    if int(r_n6_f5) == int(n6_f5):
        res_n6_f5 = n6_f5
    else:
        res_n6_f5 = "X"

    if int(r_n7_f5) == int(n7_f5):
        res_n7_f5 = n7_f5
    else:
        res_n7_f5 = "X"

    if int(r_n8_f5) == int(n8_f5):
        res_n8_f5 = n8_f5
    else:
        res_n8_f5 = "X"

    if int(r_n9_f5) == int(n9_f5):
        res_n9_f5 = n9_f5
    else:
        res_n9_f5 = "X"

    if int(r_n1_f6) == int(n1_f6):
        res_n1_f6 = n1_f6
    else:
        res_n1_f6 = "X"

    if int(r_n2_f6) == int(n2_f6):
        res_n2_f6 = n2_f6
    else:
        res_n2_f6 = "X"

    if int(r_n3_f6) == int(n3_f6):
        res_n3_f6 = n3_f6
    else:
        res_n3_f6 = "X"

    if int(r_n4_f6) == int(n4_f6):
        res_n4_f6 = n4_f6
    else:
        res_n4_f6 = "X"

    if int(r_n5_f6) == int(n5_f6):
        res_n5_f6 = n5_f6
    else:
        res_n5_f6 = "X"

    if int(r_n6_f6) == int(n6_f6):
        res_n6_f6 = n6_f6
    else:
        res_n6_f6 = "X"

    if int(r_n7_f6) == int(n7_f6):
        res_n7_f6 = n7_f6
    else:
        res_n7_f6 = "X"

    if int(r_n8_f6) == int(n8_f6):
        res_n8_f6 = n8_f6
    else:
        res_n8_f6 = "X"

    if int(r_n9_f6) == int(n9_f6):
        res_n9_f6 = n9_f6
    else:
        res_n9_f6 = "X"

    if int(r_n1_f7) == int(n1_f7):
        res_n1_f7 = n1_f7
    else:
        res_n1_f7 = "X"

    if int(r_n2_f7) == int(n2_f7):
        res_n2_f7 = n2_f7
    else:
        res_n2_f7 = "X"

    if int(r_n3_f7) == int(n3_f7):
        res_n3_f7 = n3_f7
    else:
        res_n3_f7 = "X"

    if int(r_n4_f7) == int(n4_f7):
        res_n4_f7 = n4_f7
    else:
        res_n4_f7 = "X"

    if int(r_n5_f7) == int(n5_f7):
        res_n5_f7 = n5_f7
    else:
        res_n5_f7 = "X"

    if int(r_n6_f7) == int(n6_f7):
        res_n6_f7 = n6_f7
    else:
        res_n6_f7 = "X"

    if int(r_n7_f7) == int(n7_f7):
        res_n7_f7 = n7_f7
    else:
        res_n7_f7 = "X"

    if int(r_n8_f7) == int(n8_f7):
        res_n8_f7 = n8_f7
    else:
        res_n8_f7 = "X"

    if int(r_n9_f7) == int(n9_f7):
        res_n9_f7 = n9_f7
    else:
        res_n9_f7 = "X"

    if int(r_n1_f8) == int(n1_f8):
        res_n1_f8 = n1_f8
    else:
        res_n1_f8 = "X"

    if int(r_n2_f8) == int(n2_f8):
        res_n2_f8 = n2_f8
    else:
        res_n2_f8 = "X"

    if int(r_n3_f8) == int(n3_f8):
        res_n3_f8 = n3_f8
    else:
        res_n3_f8 = "X"

    if int(r_n4_f8) == int(n4_f8):
        res_n4_f8 = n4_f8
    else:
        res_n4_f8 = "X"

    if int(r_n5_f8) == int(n5_f8):
        res_n5_f8 = n5_f8
    else:
        res_n5_f8 = "X"

    if int(r_n6_f8) == int(n6_f8):
        res_n6_f8 = n6_f8
    else:
        res_n6_f8 = "X"

    if int(r_n7_f8) == int(n7_f8):
        res_n7_f8 = n7_f8
    else:
        res_n7_f8 = "X"

    if int(r_n8_f8) == int(n8_f8):
        res_n8_f8 = n8_f8
    else:
        res_n8_f8 = "X"

    if int(r_n9_f8) == int(n9_f8):
        res_n9_f8 = n9_f8
    else:
        res_n9_f8 = "X"

    if int(r_n1_f9) == int(n1_f9):
        res_n1_f9 = n1_f9
    else:
        res_n1_f9 = "X"

    if int(r_n2_f9) == int(n2_f9):
        res_n2_f9 = n2_f9
    else:
        res_n2_f9 = "X"

    if int(r_n3_f9) == int(n3_f9):
        res_n3_f9 = n3_f9
    else:
        res_n3_f9 = "X"

    if int(r_n4_f9) == int(n4_f9):
        res_n4_f9 = n4_f9
    else:
        res_n4_f9 = "X"

    if int(r_n5_f9) == int(n5_f9):
        res_n5_f9 = n5_f9
    else:
        res_n5_f9 = "X"

    if int(r_n6_f9) == int(n6_f9):
        res_n6_f9 = n6_f9
    else:
        res_n6_f9 = "X"

    if int(r_n7_f9) == int(n7_f9):
        res_n7_f9 = n7_f9
    else:
        res_n7_f9 = "X"

    if int(r_n8_f9) == int(n8_f9):
        res_n8_f9 = n8_f9
    else:
        res_n8_f9 = "X"

    if int(r_n9_f9) == int(n9_f9):
        res_n9_f9 = n9_f9
    else:
        res_n9_f9 = "X"


    #Variables para la pagina resultados
    return render_template("resultado.html", 
        n1_f1=res_n1_f1,
        n2_f1=res_n2_f1,
        n3_f1=res_n3_f1,
        n4_f1=res_n4_f1,
        n5_f1=res_n5_f1,
        n6_f1=res_n6_f1,
        n7_f1=res_n7_f1,
        n8_f1=res_n8_f1,
        n9_f1=res_n9_f1,
        n1_f2=res_n1_f2,
        n2_f2=res_n2_f2,
        n3_f2=res_n3_f2,
        n4_f2=res_n4_f2,
        n5_f2=res_n5_f2,
        n6_f2=res_n6_f2,
        n7_f2=res_n7_f2,
        n8_f2=res_n8_f2,
        n9_f2=res_n9_f2,
        n1_f3=res_n1_f3,
        n2_f3=res_n2_f3,
        n3_f3=res_n3_f3,
        n4_f3=res_n4_f3,
        n5_f3=res_n5_f3,
        n6_f3=res_n6_f3,
        n7_f3=res_n7_f3,
        n8_f3=res_n8_f3,
        n9_f3=res_n9_f3,
        n1_f4=res_n1_f4,
        n2_f4=res_n2_f4,
        n3_f4=res_n3_f4,
        n4_f4=res_n4_f4,
        n5_f4=res_n5_f4,
        n6_f4=res_n6_f4,
        n7_f4=res_n7_f4,
        n8_f4=res_n8_f4,
        n9_f4=res_n9_f4,
        n1_f5=res_n1_f5,
        n2_f5=res_n2_f5,
        n3_f5=res_n3_f5,
        n4_f5=res_n4_f5,
        n5_f5=res_n5_f5,
        n6_f5=res_n6_f5,
        n7_f5=res_n7_f5,
        n8_f5=res_n8_f5,
        n9_f5=res_n9_f5,
        n1_f6=res_n1_f6,
        n2_f6=res_n2_f6,
        n3_f6=res_n3_f6,
        n4_f6=res_n4_f6,
        n5_f6=res_n5_f6,
        n6_f6=res_n6_f6,
        n7_f6=res_n7_f6,
        n8_f6=res_n8_f6,
        n9_f6=res_n9_f6,
        n1_f7=res_n1_f7,
        n2_f7=res_n2_f7,
        n3_f7=res_n3_f7,
        n4_f7=res_n4_f7,
        n5_f7=res_n5_f7,
        n6_f7=res_n6_f7,
        n7_f7=res_n7_f7,
        n8_f7=res_n8_f7,
        n9_f7=res_n9_f7,
        n1_f8=res_n1_f8,
        n2_f8=res_n2_f8,
        n3_f8=res_n3_f8,
        n4_f8=res_n4_f8,
        n5_f8=res_n5_f8,
        n6_f8=res_n6_f8,
        n7_f8=res_n7_f8,
        n8_f8=res_n8_f8,
        n9_f8=res_n9_f8,
        n1_f9=res_n1_f9,
        n2_f9=res_n2_f9,
        n3_f9=res_n3_f9,
        n4_f9=res_n4_f9,
        n5_f9=res_n5_f9,
        n6_f9=res_n6_f9,
        n7_f9=res_n7_f9,
        n8_f9=res_n8_f9,
        n9_f9=res_n9_f9)
    
#Activa el modo debuger, permite ejecutar en local
if __name__ == "__main__":
    app.run(debug=True)