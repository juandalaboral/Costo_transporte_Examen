import datetime
import calendar

def ejecutar_sistema_contable():
    # 1. CONFIGURACIÓN INICIAL (TIEMPO REAL)
    ahora = datetime.datetime.now()
    anio_actual = ahora.year
    mes_actual = ahora.month
    nombre_mes = calendar.month_name[mes_actual]
    
    # L = Límite de días del mes actual
    _, limite_mes = calendar.monthrange(anio_actual, mes_actual)
    
    ingreso_mensual = 0
    dia = 1

    print(f"--- 📊 INICIO DEL PROGRAMA: {nombre_mes.upper()} {anio_actual} ---")
    print(f"El mes tiene {limite_mes} días.")
    print("Comandos: [Distancia > 0: Viaje] | [-1: Ver Balance] | [0: Cerrar Día]\n")

    # 2. BUCLE PRINCIPAL (Mientras día <= L)
    while dia <= limite_mes:
        ingreso_diario = 0
        fecha_actual = datetime.date(anio_actual, mes_actual, dia)
        nombre_dia = fecha_actual.strftime("%A") # Nombre del día (Lunes, Martes...)

        print(f"--- 🗓️ DÍA {dia} ({nombre_dia}) ---")

        while True:
            try:
                entrada = float(input(f"   Ingrese distancia del viaje (km): "))
                
                # COMANDO DE CONSULTA (-1)
                if entrada == -1:
                    print(f"   >> [CONSULTA] Balance acumulado al momento: ${ingreso_mensual + ingreso_diario}")
                
                # COMANDO DE CIERRE DE DÍA (0)
                elif entrada == 0:
                    ingreso_mensual += ingreso_diario
                    print(f"   >> CIERRE DEL DÍA {dia}: Sumado ${ingreso_diario} al mes.")
                    break # Sale del bucle de ingresos y pasa al siguiente día
                
                # CÁLCULO DE TARIFAS (Valores > 0)
                elif entrada > 0:
                    if entrada <= 5:
                        tarifa = 4000
                    elif entrada <= 10:
                        tarifa = 6000
                    else:
                        tarifa = 8000
                    
                    ingreso_diario += tarifa
                    print(f"      + Tarifa aplicada: ${tarifa} | Total hoy: ${ingreso_diario}")
                
                else:
                    print("   ⚠️ Valor no válido. Use números positivos, 0 para cerrar o -1 para consultar.")
            
            except ValueError:
                print("   ⚠️ Error: Por favor ingrese un número.")

        # 3. REPORTE SEMANAL (Se ajusta al calendario real: Cierre todos los Domingos)
        # En Python, el domingo es el día 6 de la semana (0=Lunes... 6=Domingo)
        if fecha_actual.weekday() == 6: 
            print("\n" + "="*40)
            print(f"📢 REPORTE SEMANAL - CIERRE DE DOMINGO")
            print(f"Balance total acumulado al {fecha_actual}: ${ingreso_mensual}")
            print("="*40 + "\n")

        # dia++ (Avanzar al siguiente día)
        dia += 1

    # 4. FINALIZACIÓN DEL MES
    print("\n" + "X"*40)
    print(f"✅ MES FINALIZADO: {nombre_mes.upper()}")
    print(f"💰 INGRESO TOTAL DEL MES: ${ingreso_mensual}")
    print("X"*40)

# Ejecutar el programa
if __name__ == "__main__":
    ejecutar_sistema_contable()