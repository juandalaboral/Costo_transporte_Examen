import datetime
import calendar

# --- PROGRAMA DE GESTIÓN DE INGRESOS CON CALENDARIO REAL ---

def ejecutar_sistema_transporte():
    # --- LÓGICA DE CALENDARIO REAL ---
    ahora = datetime.datetime.now()
    anio_actual = ahora.year
    mes_actual = ahora.month
    nombre_mes = ahora.strftime("%B") # Nombre del mes en curso
    
    # Obtener el límite de días (L) del mes actual
    _, limite_mes = calendar.monthrange(anio_actual, mes_actual)
    
    # Variables de acumulación maestra
    ingreso_mensual_acumulado = 0
    ingreso_semana_actual = 0
    
    print(f"=== SISTEMA DE CONTROL DE INGRESOS - {nombre_mes.upper()} {anio_actual} ===")
    print(f"Este mes tiene {limite_mes} días.")
    print("Instrucciones: Ingrese la distancia en KM.")
    print("Escriba '0' para cerrar el día.")
    print("Escriba '-1' para ver el BALANCE TOTAL ACUMULADO hasta hoy.")

    # El ciclo ahora va desde 1 hasta el límite real del mes (limite_mes + 1)
    for dia in range(1, limite_mes + 1):
        ingreso_diario = 0
        
        # Determinar qué día de la semana es (para el reporte de domingos)
        fecha_actual = datetime.date(anio_actual, mes_actual, dia)
        nombre_dia_semana = fecha_actual.strftime("%A") # Ejemplo: 'Sunday' o 'domingo'
        
        print(f"\n>>> INICIO DEL DÍA {dia} ({nombre_dia_semana}) <<<")
        
        while True:
            try:
                entrada = input(f"(Día {dia}) Distancia del viaje: ")
                distancia = float(entrada)
                
                # Opción para ver balance acumulado sin cerrar el día (TÚ COMANDO ORIGINAL)
                if distancia == -1:
                    print("\n" + "*"*35)
                    print(f"REPORTES AL DÍA {dia}:")
                    print(f"Acumulado en el mes: ${ingreso_mensual_acumulado + ingreso_diario}")
                    print(f"Acumulado hoy: ${ingreso_diario}")
                    print("*"*35 + "\n")
                    continue 

                # Opción para cerrar el día (TÚ COMANDO ORIGINAL)
                if distancia == 0:
                    break 
                
                # Lógica de tarifas (TÚ LÓGICA ORIGINAL)
                if distancia <= 5:
                    tarifa = 4000
                elif distancia <= 10:
                    tarifa = 6000
                else:
                    tarifa = 8000
                
                ingreso_diario += tarifa
                print(f"Registrado: ${tarifa}")
                
            except ValueError:
                print("Error: Ingrese un número válido.")

        # Actualización de acumuladores al cerrar el día
        ingreso_semana_actual += ingreso_diario
        ingreso_mensual_acumulado += ingreso_diario
        
        print(f"--- CIERRE DÍA {dia}: ${ingreso_diario} ---")

        # --- REPORTE SEMANAL AJUSTADO A CALENDARIO REAL ---
        # El reporte se dispara cada DOMINGO (weekday 6) o si es el ÚLTIMO DÍA del mes
        if fecha_actual.weekday() == 6 or dia == limite_mes:
            print(f"\n[!] REPORTE DE CIERRE SEMANAL/DOMINGO. Acumulado: ${ingreso_semana_actual}")
            ingreso_semana_actual = 0 

    print("\n" + "="*45)
    print(f"BALANCE FINAL DE {nombre_mes.upper()} COMPLETADO: ${ingreso_mensual_acumulado}")
    print("="*45)

if __name__ == "__main__":
    ejecutar_sistema_transporte()