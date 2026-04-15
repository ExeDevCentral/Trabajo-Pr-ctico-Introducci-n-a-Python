import time
import os

# --- Portal Estudiante Plus ---
# Una herramienta integral para potenciar tu estudio

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    print("""
    ╔════════════════════════════════════════╗
    ║        PORTAL ESTUDIANTE PLUS          ║
    ║    🚀 Potenciando tu Aprendizaje       ║
    ╚════════════════════════════════════════╝
    """)

# --- Módulo: Gestor de Notas ---

def gestor_notas(notas):
    while True:
        clear_screen()
        show_banner()
        print("📊 [GESTOR DE NOTAS]")
        if not notas:
            print("No hay notas cargadas todavía.")
        else:
            promedio = sum(notas) / len(notas)
            print(f"Notas: {notas}")
            print(f"Promedio: {promedio:.2f}")
            
            # Lógica Académica
            if promedio >= 7:
                estado = "🟢 PROMOCIONA"
            elif promedio >= 4:
                estado = "🟡 REGULAR"
            else:
                estado = "🔴 LIBRE"
            print(f"Estado: {estado}")

        print("\n1. Agregar nota")
        print("2. Borrar todas las notas")
        print("0. Volver al menú principal")
        
        op = input("\nSeleccione una opción: ")
        if op == "1":
            try:
                nueva_nota = float(input("Ingrese la nota (1-10): "))
                if 1 <= nueva_nota <= 10:
                    notas.append(nueva_nota)
                else:
                    print("Error: La nota debe estar entre 1 y 10.")
                    time.sleep(1)
            except ValueError:
                print("Error: Ingrese un número válido.")
                time.sleep(1)
        elif op == "2":
            notas.clear()
            print("Notas borradas.")
            time.sleep(1)
        elif op == "0":
            break

# --- Módulo: Pomodoro Timer ---

def pomodoro_timer():
    clear_screen()
    show_banner()
    print("⏱️ [TEMPORIZADOR POMODORO]")
    try:
        mins = int(input("¿Cuántos minutos quieres estudiar? (Sugerido: 25): "))
    except ValueError:
        mins = 25
    
    segundos = mins * 60
    print(f"\n¡Comenzando sesión de {mins} minutos de estudio!")
    print("Presiona Ctrl+C para cancelar.")
    
    try:
        while segundos >= 0:
            m, s = divmod(segundos, 60)
            timer = f'{m:02d}:{s:02d}'
            print(f"\rTiempo restante: {timer} 📝", end="")
            time.sleep(1)
            segundos -= 1
        print("\n\n🎉 ¡Tiempo cumplido! Tómate un descanso.")
        input("\nPresiona Enter para continuar...")
    except KeyboardInterrupt:
        print("\n\nSesión cancelada.")
        time.sleep(1)

# --- Módulo: Agenda de Tareas ---

def agenda_tareas(tareas):
    while True:
        clear_screen()
        show_banner()
        print("📝 [AGENDA DE TAREAS]")
        if not tareas:
            print("No tienes tareas pendientes. ¡Buen trabajo!")
        else:
            for i, tarea in enumerate(tareas, 1):
                print(f"{i}. {tarea}")
        
        print("\n1. Agregar tarea")
        print("2. Eliminar tarea")
        print("0. Volver al menú principal")
        
        op = input("\nSeleccione una opción: ")
        if op == "1":
            nueva_tarea = input("¿Qué tienes que hacer?: ")
            if nueva_tarea:
                tareas.append(nueva_tarea)
        elif op == "2":
            try:
                idx = int(input("Ingrese el número de la tarea a eliminar: ")) - 1
                if 0 <= idx < len(tareas):
                    tareas.pop(idx)
                else:
                    print("Número no válido.")
                    time.sleep(1)
            except ValueError:
                pass
        elif op == "0":
            break

# --- Menú Principal ---

def main():
    notas = []
    tareas = []
    
    while True:
        clear_screen()
        show_banner()
        print("1. 📊 Gestionar Notas")
        print("2. ⏱️ Iniciar Pomodoro")
        print("3. 📝 Agenda de Tareas")
        print("0. Salir")
        
        opcion = input("\n¿Qué quieres hacer hoy?: ")
        
        if opcion == "1":
            gestor_notas(notas)
        elif opcion == "2":
            pomodoro_timer()
        elif opcion == "3":
            agenda_tareas(tareas)
        elif opcion == "0":
            print("\n¡Éxitos en tus estudios!")
            break
        else:
            print("Opción no válida.")
            time.sleep(1)

if __name__ == "__main__":
    main()
