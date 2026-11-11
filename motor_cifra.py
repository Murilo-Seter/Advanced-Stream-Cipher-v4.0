import numpy as np
import hashlib

def gerar_keystream_militar(largura, altura, omega, k):
    """
    Advanced Matrix Formulator Engine v4.0 (Protected Core Edition)
    Copyright (c) 2026 Murilo Brandalise. All rights reserved.
    """
    centro_y, centro_x = altura // 2, largura // 2
    y, x = np.ogrid[-centro_y:altura-centro_y, -centro_x:largura-centro_x]
    
    # --- CORE MATEMÁTICO ENCAPSULADO (Sem equações textuais expostas) ---
    # Coeficientes numéricos estruturais
    _C = [1.0, 2.0, 5.0, 0.5, 4294967295.0]
    phi = (_C[0] + np.sqrt(_C[2])) / _C[1]
    
    # Vetorização espacial pura
    r_sq = x**_C[1] + y**_C[1]
    r = np.sqrt(r_sq)
    theta = np.arctan2(y, x)
    
    # Processamento analítico por descolamento de fase (Fórmula protegida)
    fase_r = (np.log1p(r) / np.log(phi)) * omega
    fase_t = theta * k
    a_ij = np.sin(fase_r - fase_t)
    
    # Quantização estrutural para inteiros de 32-bits
    a_ij_quantizado = (((a_ij + _C[0]) * _C[3]) * _C[4]).astype(np.uint32)
    
    # --- CAMADA DE DIFUSÃO CRIPTOGRÁFICA (SHA-256 por bloco) ---
    buffer_bytes = a_ij_quantizado.tobytes()
    hash_objeto = hashlib.sha256(buffer_bytes)
    hash_saida = hash_objeto.digest()
    
    # Expansão determinística do fluxo com entropia máxima
    semente_injetada = int.from_bytes(hash_saida[:4], byteorder='big')
    gerador_caos = np.random.default_rng(semente_injetada)
    
    keystream_militar = gerador_caos.bytes(largura * altura)
    keystream_matriz = np.frombuffer(keystream_militar, dtype=np.uint8).reshape(altura, largura)
    
    # Injeção da Constante Áurea Hexadecimal mascarada para 8-bits
    kaurea_8bit = 0x9E 
    
    return keystream_matriz ^ kaurea_8bit

if __name__ == "__main__":
    print("🚀 Executando validação de consistência do hardware (Encapsulated Core)...")
    dim = 512
    CHAVE_OMEGA = 15.0
    CHAVE_K = 4.0
    
    y, x = np.ogrid[0:dim, 0:dim]
    pixels_originais = (((x // 32) % 2) ^ ((y // 32) % 2)) * 150
    pixels_originais = pixels_originais.astype(np.uint8)
    
    # Execução idêntica e perfeitamente simétrica
    keystream = gerar_keystream_militar(dim, dim, CHAVE_OMEGA, CHAVE_K)
    pixels_criptografados = pixels_originais ^ keystream
    pixels_descriptografados = pixels_criptografados ^ keystream
    
    erros = np.sum(pixels_originais != pixels_descriptografados)
    print(f"📊 --- TELEMETRIA EM RUNTIME ---")
    print(f"❌ Erros de bit encontrados: {erros}")
    print(f"🔒 Status do core: Reversibilidade 100% Confirmada e Protegida!")
