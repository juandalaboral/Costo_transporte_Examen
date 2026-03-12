# --- PROGRAMA DE GESTIÓN DE INGRESOS CON CONSULTA EN TIEMPO REAL ---

def ejecutar_sistema_transporte():
    # Variables de acumulación maestra
    ingreso_mensual_acumulado = 0
    ingreso_semana_actual = 0
    
    print("=== SISTEMA DE CONTROL DE INGRESOS (30 DÍAS) ===")
    print("Instrucciones: Ingrese la distancia en KM.")
    print("Escriba '0' para cerrar el día.")
    print("Escriba '-1' para ver el BALANCE TOTAL ACUMULADO hasta hoy.")

    for dia in range(1, 31):
        ingreso_diario = 0
        print(f"\n>>> INICIO DEL DÍA {dia} <<<")
        
        while True:
            try:
                entrada = input(f"(Día {dia}) Distancia del viaje: ")
                distancia = float(entrada)
                
                # Opción para ver balance acumulado sin cerrar el día
                if distancia == -1:
                    print("\n" + "*"*35)
                    print(f"REPORTES AL DÍA {dia}:")
                    print(f"Acumulado en el mes: ${ingreso_mensual_acumulado + ingreso_diario}")
                    print(f"Acumulado hoy: ${ingreso_diario}")
                    print("*"*35 + "\n")
                    continue # Regresa al inicio del ciclo para seguir registrando el día

                # Opción para cerrar el día
                if distancia == 0:
                    break 
                
                # Lógica de tarifas
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
        
        print(f"\n--- CIERRE DÍA {dia}: ${ingreso_diario} ---")

        # Reporte semanal automático
        if dia % 7 == 0:
            print(f"\n[!] FIN DE LA SEMANA. Total 7 días: ${ingreso_semana_actual}")
            ingreso_semana_actual = 0 

    print("\n" + "="*45)
    print(f"BALANCE FINAL DE MES COMPLETADO: ${ingreso_mensual_acumulado}")
    print("="*45)

if __name__ == "__main__":
    ejecutar_sistema_transporte()