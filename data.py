import serial

 
""" Définition des variables et constantes"""
DEBUG=False

# Variable for frame management
size_frame = 56
display_horizontal_resolution=1280
display_vertical_resolution=720
display_line1=40
display_line2=60
display_line3=100
display_line4=120

space=150
width_rectangle=200

rectangle1_X1=(display_horizontal_resolution/2)-100
rectangle1_X2=(display_horizontal_resolution/2)+100
rectangle1_Y1=display_line1-20
rectangle1_Y2=display_line4+20

rectangle2_X1=(display_horizontal_resolution/2)-space
rectangle2_X2=(display_horizontal_resolution/2)-space-width_rectangle
rectangle2_Y1=display_line1-20
rectangle2_Y2=display_line4+20

rectangle3_X1=(display_horizontal_resolution/2)+space
rectangle3_X2=(display_horizontal_resolution/2)+space+width_rectangle
rectangle3_Y1=display_line1-20
rectangle3_Y2=display_line4+20
 
# Serial Port parameter
port_serie_nom = 'COM2'
port_serie_baudrate = 19200
port_serie_bytesize = serial.EIGHTBITS
port_serie_parity = serial.PARITY_NONE
port_serie_stopbits = serial.STOPBITS_ONE

# UDP parameters
hote = "localhost"
port = 12800
data_udp = ["Enter Name","Enter Name", 0]
 
# Définition de la frame
# Format: [valeur] = [num_octet, valeur]
frame = {}
# SYNCRHO
#frame["index"]=[0,1]
frame["B1_SYNCHRO"]                 =[0, 0xE0]
frame["B2_SYNCHRO"]                 =[1, 0xE4]
frame["B3_SYNCHRO"]                 =[2, 0xF8]
frame["B4_SYNCHRO"]                 =[3, 0x35]
# UNDEFINIED
frame["B5_UNDEF"]                   =[4, 0x20]  # ' '
frame["B6_UNDEF"]                   =[5, 0x30]  # '0'
# TEMPS default value: ' 7:28'
frame["B7_TPS_DIZAINE"]             =[6, 0x20]  # ' '
frame["B8_TPS_UNITE"]               =[7, 0x37]  # '7'
frame["B9_TPS_DIXIEME"]             =[8, 0x32]  # '2'
frame["B10_TPS_CENTIEME"]           =[9, 0x38]  # '8'
# SCORE1 default value: '  2'
frame["B11_SCORE1_CENTAINE"]        =[10, 0x20] # ' '
frame["B12_SCORE1_DIZAINE"]         =[11, 0x20] # ' '
frame["B13_SCORE1_UNITE"]           =[12, 0x32] # '2'
# SCORE2 default value: '  0'
frame["B14_SCORE2_CENTAINE"]        =[13, 0x20] # ' '
frame["B15_SCORE2_DIZAINE"]         =[14, 0x20] # ' '
frame["B16_SCORE2_UNITE"]           =[15, 0x30] # '0'
# MATCH default value: 2ième période Prison équipe 1=*** Prison équipe 2=*** 
frame["B17_NUM_PERIODE"]            =[16, 0x32] # '2'
frame["B18_NB_PRISON_EQP1"]         =[17, 0x33] # '3' -> ***
frame["B19_NB_PRISON_EQP2"]         =[18, 0x33] # '3' -> ***
# UNDEFINIED
frame["B20_UNDEF"]                  =[19, 0x30] # '0'
frame["B21_UNDEF"]                  =[20, 0x30] # '0'
frame["B22_UNDEF"]                  =[21, 0x30] # '0'
# CHRONO : 0=  temps de jeu. 1 = chrono arrêté
frame["B23_TPS_ON_OFF"]             =[22, 0x31] # '1'  
#
frame["B24_UNDEF"]                  =[23, 0x30] # '0'
# EQUIPE 1
frame["B25_EQP1_PRISON1_UNITE"]     =[24, 0x31] # '1'
frame["B26_EQP1_PRISON1_DIXIEME"]   =[25, 0x34] # '4'
frame["B27_EQP1_PRISON1_CENTIEME"]  =[26, 0x34] # '4'
frame["B28_EQP1_PRISON2_UNITE"]     =[27, 0x31] # '1'
frame["B29_EQP1_PRISON2_DIXIEME"]   =[28, 0x34] # '4'
frame["B30_EQP1_PRISON2_CENTIEME"]  =[29, 0x34] # '4'
frame["B31_EQP1_PRISON3_UNITE"]     =[30, 0x31] # '1'
frame["B32_EQP1_PRISON3_DIXIEME"]   =[31, 0x34] # '4'
frame["B33_EQP1_PRISON3_CENTIEME"]  =[32, 0x34] # '4'
# UNDEFINIED
frame["B34_UNDEF"]                  =[33, 0x20] # ' '
frame["B35_UNDEF"]                  =[34, 0x20] # ' '
frame["B36_UNDEF"]                  =[35, 0x20] # ' '
frame["B37_UNDEF"]                  =[36, 0x20] # ' '
# EQUIPE 2
frame["B38_EQP2_PRISON1_UNITE"]     =[37, 0x31] # '1'
frame["B39_EQP2_PRISON1_DIXIEME"]   =[38, 0x34] # '4'
frame["B40_EQP2_PRISON1_CENTIEME"]  =[39, 0x34] # '4'
frame["B41_EQP2_PRISON2_UNITE"]     =[40, 0x31] # '1'
frame["B42_EQP2_PRISON2_DIXIEME"]   =[41, 0x35] # '5'
frame["B43_EQP2_PRISON2_CENTIEME"]  =[42, 0x33] # '3'
frame["B44_EQP2_PRISON3_UNITE"]     =[43, 0x31] # '1'
frame["B45_EQP2_PRISON3_DIXIEME"]   =[44, 0x35] # '5'
frame["B46_EQP2_PRISON3_CENTIEME"]  =[45, 0x36] # '6'
# UNDEFINIED
frame["B47_UNDEF"]                  =[46, 0x20] # ' '
frame["B48_UNDEF"]                  =[47, 0x20] # ' '
frame["B49_UNDEF"]                  =[48, 0x20] # ' '
frame["B50_UNDEF"]                  =[49, 0x20] # ' '
frame["B51_UNDEF"]                  =[50, 0x20] # ' '
frame["B52_UNDEF"]                  =[51, 0x20] # ' '
frame["B53_UNDEF"]                  =[52, 0x20] # ' '
frame["B54_UNDEF"]                  =[53, 0x20] # ' '
frame["B55_UNDEF"]                  =[54, 0x20] # ' '
# END
frame["B56_END"]                    =[55, 0x0D] # 'CR'
