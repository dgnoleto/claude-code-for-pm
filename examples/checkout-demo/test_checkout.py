import unittest

from checkout import desconto_cupom, frete_gratis


class CheckoutDemoTests(unittest.TestCase):
    def test_oferta_no_limite_permite_cupom(self):
        self.assertEqual(desconto_cupom(20000, 10, 15), 2000)

    def test_oferta_acima_do_limite_bloqueia_cupom(self):
        self.assertEqual(desconto_cupom(20000, 10, 16), 0)

    def test_teto_do_desconto(self):
        self.assertEqual(desconto_cupom(100000, 50), 10000)

    def test_fracao_de_centavo_e_descartada(self):
        self.assertEqual(desconto_cupom(999, 10), 99)

    def test_limites_do_frete_por_regiao(self):
        for regiao, limite in [("Sudeste", 19900), ("Sul", 29900)]:
            with self.subTest(regiao=regiao):
                self.assertFalse(frete_gratis(limite - 1, regiao))
                self.assertFalse(frete_gratis(limite, regiao))
                self.assertTrue(frete_gratis(limite + 1, regiao))


if __name__ == "__main__":
    unittest.main()
