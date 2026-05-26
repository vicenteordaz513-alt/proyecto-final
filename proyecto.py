# SISTEMA INTELIGENTE DE HÁBITOS DE ESTUDIO (sin gráfico)
import random
import time
import sys
import math
import statistics

# --- Arreglos ---
horas_semana = []       # horas de estudio
sueno_semana = []       # horas de sueño
comentarios = []        # comentarios motivacionales

# --- Funciones definidas ---
def pedir_horas_estudio():
    """Solicita horas de estudio por 7 días"""
    for dia in range(1, 8):
        try:
            horas = float(input(f"Ingrese las horas de estudio del día {dia}: "))
            horas_semana.append(horas)
        except ValueError:
            print("Error: ingrese un número válido")
            horas_semana.append(0.0)

def pedir_horas_sueno():
    """Solicita horas de sueño por 7 días"""
    for dia in range(1, 8):
        while True:
            try:
                sueno = float(input(f"Ingrese las horas de sueño del día {dia}: "))
                if 0 < sueno <= 24:
                    sueno_semana.append(sueno)
                    break
                else:
                    print("Ingrese un valor válido (0-24)")
            except ValueError:
                print("Error: ingrese un número válido")

def calcular_promedios():
    """Calcula promedios de estudio y sueño"""
    prom_estudio = sum(horas_semana) / len(horas_semana)
    prom_sueno = statistics.mean(sueno_semana)
    return prom_estudio, prom_sueno

def evaluar_habitos(prom_estudio: float, prom_sueno: float) -> (str, bool):
    """Evalúa hábitos con condiciones"""
    if prom_estudio >= 3 and prom_sueno >= 7:
        resultado = "Hábitos de estudio adecuados"
        estado = True
    else:
        resultado = "Hábitos de estudio inadecuados"
        estado = False
    return resultado, estado

# --- Ejecución del sistema ---
print("SISTEMA INTELIGENTE DE HÁBITOS DE ESTUDIO")
time.sleep(1)

pedir_horas_estudio()
pedir_horas_sueno()

prom_estudio, prom_sueno = calcular_promedios()
resultado, estado = evaluar_habitos(prom_estudio, prom_sueno)

# Operadores aritméticos de ejemplo
try:
    total_horas = sum(horas_semana) + sum(sueno_semana)
    resta = total_horas - prom_estudio
    multiplicacion = prom_estudio * prom_sueno
    division = prom_estudio / (prom_sueno if prom_sueno != 0 else 1)
    modulo = int(prom_estudio) % 2
    raiz = math.sqrt(prom_estudio)
except Exception as e:
    print("Error en operaciones aritméticas:", e)
    sys.exit()

# Mostrar resultados
print("\n--- RESULTADOS ---")
print("Promedio de estudio semanal:", prom_estudio)
print("Promedio de sueño semanal:", prom_sueno)
print("Resultado:", resultado)
print("Operaciones aritméticas -> Total:", total_horas, "Resta:", resta,
      "Multiplicación:", multiplicacion, "División:", division, "Módulo:", modulo, "Raíz cuadrada:", raiz)

# Comentarios motivacionales
comentarios = ["¡Sigue así!", "Puedes mejorar aún más", "No te rindas", "Excelente disciplina", "La constancia es la clave"]
print("Comentario motivacional:", random.choice(comentarios))

print("Fin del sistema")
