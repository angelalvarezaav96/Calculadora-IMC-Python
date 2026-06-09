import tkinter as tk
from tkinter import messagebox

def calcular_imc():
    # 1. Obtener los datos eliminando espacios en blanco (Validación de vacíos)
    nom = entry_nombre.get().strip()
    pat = entry_paterno.get().strip()
    mat = entry_materno.get().strip()
    edad_str = entry_edad.get().strip()
    peso_str = entry_peso.get().strip()
    est_str = entry_estatura.get().strip()

    if not all([nom, pat, mat, edad_str, peso_str, est_str]):
        messagebox.showerror("Error de Validación", "Todos los campos son obligatorios y no pueden quedar vacíos.")
        return

    # 2. Validación de cifras numéricas
    try:
        edad = int(edad_str)
        peso = float(peso_str)
        estatura = float(est_str)
        
        if edad <= 0 or peso <= 0 or estatura <= 0:
            messagebox.showerror("Error de Datos", "La edad, el peso y la estatura deben ser mayores a cero.")
            return
            
    except ValueError:
        messagebox.showerror("Error de Datos", "Por favor, introduce cifras numéricas válidas en Edad, Peso y Estatura.")
        return

    # 3. Uso de operadores aritméticos para calcular el IMC
    imc = peso / (estatura ** 2)

    # 4. Salida de datos en la interfaz
    nombre_completo = f"{nom} {pat} {mat}"
    resultado_texto = (
        f"Paciente: {nombre_completo}\n"
        f"Edad: {edad} años\n"
        f"Peso: {peso} kg\n"
        f"Estatura: {estatura} m\n"
        f"-----------------------------------------\n"
        f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}"
    )
    
    label_resultado.config(text=resultado_texto, fg="#1b5e20")

# --- Configuración de la Interfaz Gráfica (Tkinter) ---
ventana = tk.Tk()
ventana.title("Calculadora de IMC")
ventana.geometry("420x550")
ventana.config(padx=20, pady=20)

# Título Principal
lbl_titulo = tk.Label(ventana, text="Calculadora de IMC", font=("Arial", 16, "bold"))
lbl_titulo.pack(pady=10)

# Contenedor para los campos de texto
frame_campos = tk.Frame(ventana)
frame_campos.pack(fill="x", pady=10)

# Función auxiliar para crear etiquetas y campos alineados
def crear_campo(texto_label, fila):
    lbl = tk.Label(frame_campos, text=texto_label, font=("Arial", 10))
    lbl.grid(row=fila, column=0, sticky="w", pady=5)
    entry = tk.Entry(frame_campos, font=("Arial", 10))
    entry.grid(row=fila, column=1, sticky="ew", padx=10, pady=5)
    return entry

frame_campos.columnconfigure(1, weight=1)

# Creación de los campos requeridos
entry_nombre = crear_campo("Nombre:", 0)
entry_paterno = crear_campo("Apellido Paterno:", 1)
entry_materno = crear_campo("Apellido Materno:", 2)
entry_edad = crear_campo("Edad (años):", 3)
entry_peso = crear_campo("Peso (kg):", 4)
entry_estatura = crear_campo("Estatura (metros):", 5)

# Botón para accionar el cálculo
btn_calcular = tk.Button(ventana, text="Calcular IMC", font=("Arial", 11, "bold"), bg="#0288d1", fg="white", command=calcular_imc)
btn_calcular.pack(pady=15, fill="x")

# Cuadro de resultados
label_resultado = tk.Label(ventana, text="Introduce tus datos y haz clic en Calcular", font=("Arial", 10, "italic"), justify="left", bd=1, relief="solid", padx=10, pady=10, bg="#f5f5f5")
label_resultado.pack(fill="both", expand=True, pady=10)

# Iniciar la aplicación
ventana.mainloop()
