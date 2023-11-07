import serial.tools.list_ports
import time
import customtkinter as ctk
import threading

ports = serial.tools.list_ports.comports()
serialinst = serial.Serial()

portList = []

for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))

serialinst.baudrate = 115200
serialinst.port = "COM4"
serialinst.open()

janela = ctk.CTk()
janela._set_appearance_mode("dark")

# Aumente o tamanho dos rótulos
fonte = ("Helvetica", 35)

janela.geometry("750x500")

# Crie a janela antes de criar as variáveis
distancia = ctk.StringVar(value="Distância: Valor")
status = ctk.StringVar(value="Status: Valor")
porcentagem = ctk.StringVar(value="Capacidade: Valor")

# Rótulos explicativos e rótulos de valores
label_distancia = ctk.CTkLabel(janela, textvariable=distancia, font=fonte)
label_porcentagem = ctk.CTkLabel(janela, textvariable=porcentagem, font=fonte)
label_status = ctk.CTkLabel(janela, textvariable=status, font=fonte)

# Centralize a grade horizontalmente e verticalmente e ajuste ao tamanho da tela
label_distancia.place(relx=0.5, rely=0.3, anchor="center")
label_porcentagem.place(relx=0.5, rely=0.5, anchor="center")
label_status.place(relx=0.5, rely=0.7, anchor="center")


def atualizar_variaveis():
    while True:
        time.sleep(1)
        if serialinst.in_waiting:
            packet = serialinst.readline().decode("utf").strip()
            if packet.startswith("porcentagem: "):
                porcentagem.set(f"Porcentagem: {packet[len('porcentagem: '):]}")
                print("Porcentagem: ", porcentagem.get())
            elif packet.startswith("status: "):
                status.set(f"Status: {packet[len('status: '):]}")
                print("Status: ", status.get())
            elif packet.startswith("distancia: "):
                distancia.set(f"Distância: {packet[len('distancia: '):]}")
                print("Distância: ", distancia.get())


# Inicie a função para atualizar as variáveis em uma thread
thread = threading.Thread(target=atualizar_variaveis)
thread.daemon = True
thread.start()

# Inicie o loop principal da interface gráfica
janela.mainloop()
