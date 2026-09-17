"""Base fictícia para exercitar extração de regras; valores em centavos."""


def desconto_cupom(subtotal_centavos, percentual, maior_oferta_percentual=0):
    """Pressupõe valores inteiros, subtotal >= 0 e percentual entre 0 e 100."""
    if maior_oferta_percentual > 15:
        return 0
    return min(subtotal_centavos * percentual // 100, 10000)


def frete_gratis(subtotal_centavos, regiao):
    """Região é uma string normalizada: Sudeste ou outro valor."""
    limite = 19900 if regiao == "Sudeste" else 29900
    return subtotal_centavos > limite
