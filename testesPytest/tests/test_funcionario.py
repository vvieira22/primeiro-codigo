from funcionario import Funcionario
import pytest
from pytest import mark

class TestClass:
    def test_idade_funcionario_valido(self):
        funcionario = Funcionario("João", 1000, "01/01/2000")
        assert isinstance(funcionario.idade(), int)
        
    def test_sobrenome_funcionario_valido(self):
        funcionario = Funcionario("João da silva", 1000, "01/01/2000")
        assert funcionario.sobrenome() == "silva"
        
    @mark.skip(reason="Reajuste anual ainda nao confirmado.")
    def test_reajuste_salarial_anual_5_porcento(self):
        funcionario = Funcionario("João da silva", 1000, "01/01/2000")
        salario = funcionario.salario
        resultado_esperado = salario * 1.05
        funcionario.reajuste_salarial_anual()
        assert funcionario.salario == resultado_esperado    
        
    @mark.calculo_bonus
    def test_quando_salario_menor_que_10000_bonus_de_10_porcento(self):
        funcionario = Funcionario("João da silva", 1000, "01/01/2000")
        assert funcionario.calcular_bonus_salarial() == 100
        
    @mark.calculo_bonus
    def test_quando_salario_maior_que_10000_bonus_de_0_porcento(self):
        with pytest.raises(Exception):
            funcionario = Funcionario("João da silva", 110000, "01/01/2000")
            assert funcionario.calcular_bonus_salarial()