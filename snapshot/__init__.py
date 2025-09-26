from . import monitor

# Exponer la clase y la función
SystemMonitor = monitor.SystemMonitor
main = monitor.main

# Alias para que los tests funcionen
# Ahora snapshot es el módulo, y snapshot.main existe
snapshot = monitor

