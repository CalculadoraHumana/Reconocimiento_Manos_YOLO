import cv2
import matplotlib.pyplot as plt
import os

# Ruta de la carpeta con los frames
frames_folder = "SEMANA 2/ejemplo/frames"

# Ruta de la carpeta con los archivos txt en formato YOLO
yolo_folder = "SEMANA 2/ejemplo/annots"

# Ruta de resultados
Result_frames = "SEMANA 2/resultadosframes"

# Pedir al usuario que ingrese el color del rectángulo en formato (B,G,R)
color_str = input("Ingrese el color del rectángulo en formato (B,G,R): ")
color = tuple(map(int, color_str.split(",")))

#Grosor del rectangulo
thickness_str = input("Ingrese el grosor del rectángulo (valor numérico): ")
thickness = int(thickness_str)

# Variable de cambio de nombre
num_img = 0

for frame_name in os.listdir(frames_folder):
    # Leer el frame
    frame = cv2.imread(os.path.join(frames_folder, frame_name))
    dh, dw, _ = frame.shape

    # Leer el archivo correspondiente en formato YOLO
    yolo_file = open(os.path.join(
        yolo_folder, frame_name.split(".")[0] + ".txt"), "r")
    data = yolo_file.readlines()
    yolo_file.close()

    for dt in data:
        print(dt)
        # Split string to float
        _, x, y, w, h = map(float, dt.split(' '))

        l = int((x - w / 2) * dw)
        r = int((x + w / 2) * dw)
        t = int((y - h / 2) * dh)
        b = int((y + h / 2) * dh)

        if l < 0:
            l = 0
        elif r > dw - 1:
            r = dw - 1
        elif t < 0:
            t = 0
        elif b > dh - 1:
            b = dh - 1
        cv2.rectangle(frame, (l, t), (r, b), color, thickness)

    num_img += 1
    filename = frame_name

    # Guarda la imagen en escala de grises
    cv2.imwrite(os.path.join(Result_frames, filename), frame)

    # Mostrar el frame con las cajas delimitadoras
    cv2.imshow("Frame", frame)
    cv2.waitKey(0)

# Destruir todas las ventanas abiertas
cv2.destroyAllWindows()
# plt.imshow(frame)
# plt.show()
