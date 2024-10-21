from scapy.all import *

# Crear un paquete ICMP de tipo 3 (Destination Unreachable)
icmp = ICMP(type=3, code=0)  # type=3, code=0 indica "Network Unreachable"

# Crear un payload que supere el tamaño permitido
payload_size = 70000  # Por ejemplo, 70000 bytes
payload = b'A' * (payload_size - len(icmp))  # Rellenar con datos

# Combinar ICMP con el payload
packet = icmp/payload

# Mostrar información del paquete
print(packet.show())

# Opcional: enviar el paquete (descomentarlo para enviar)
# send(packet)
