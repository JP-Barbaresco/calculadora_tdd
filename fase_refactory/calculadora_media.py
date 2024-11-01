# media.py - Código da Fase Refactor
def calcular_media(nota1, nota2, nota3):
    # Verificação opcional para garantir que as notas sejam numéricas e estejam entre 0 e 10.
    notas = [nota1, nota2, nota3]
    if any(not isinstance(nota, (int, float)) or nota < 0 or nota > 10 for nota in notas):
        raise ValueError("Todas as notas devem ser números entre 0 e 10.")
    
    # Cálculo da média das três notas
    return sum(notas) / len(notas)
