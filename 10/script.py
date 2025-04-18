#!/usr/bin/env python3

import os
import time

while True:
    print("Verificando usuário atual:")
    print(f"User ID (UID): {os.getuid()}")
    print(f"Group ID (GID): {os.getgid()}")
    print("------")
    time.sleep(2)  # Pausa de 2 segundos
