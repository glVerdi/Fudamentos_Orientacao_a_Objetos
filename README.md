# Fundamentos Orientação a Objetos 

## O que é programação Orientado a Objetos
- O principal objetivo da programação é resolver algum tipo de problema utilizado para isso um software. De forma genérica, podemos resolver um problema de maneiras diferentes, com visões diferentes, na programação essas visões diferentes são conhecidas como paradigma.
- Queremos relacionar os objetos para trocar informações entre si, cada objeto se relaciona com características, com ações individuais dele, para cada objeto se tem métodos diferentes. 
- Um objeto pode ser categorizado, definido por suas características, um objeto pode ser simples ou complexo. 
- Utilizamos POO para facilitar o entendimento do código.
- Colocamos o código como caixinhas, que é modularização e conseguimos reutilizar em outras partes do programa, utilizando as funcionalidades do código sem ter que replicar em várias partes do programa, se quiser que ele execute alguma funcionalidade, você chama ela. 
- Também utilizando POO para aproximarmos o código do mundo real, ajuda a gerenciar a memória do computador. A funcionalidade só é executada quando ela é chamada, quando ela executa se cria espaço na memória, fazendo o que tem que fazer e no final a memória é liberada. 
- O objeto vai ser construído e guardado em uma variável e esse objeto vai vir de um modelo, outro código irá gerar esse modelo, esse modelo é a classe.
- Uma classe é um modelo onde irá se descrever as propriedades do objeto que irá ser utilizado durante o código.
- Vários objetos e eles serão iguais entre si.
## Classes, métodos e objetos
- Quando criamos um objeto precisamos pensar qual o seu objetivo, para qual finalidade ele será utilizado, então é importante sabermos por que ele deve existir no seu código.
- Uma instância nada mais é do que gerar alguma coisa de forma instaantânea. è o momento no código que o processo irá acontecer, que o código vai gerar nosso objeto. Uma instância de classe é um objeto cujo seu comportamento e seus estados são definidos através da classe, e a classe possui atributos e métodos. è o momento em que consulta aquele molde e gera o objeto. Exemplo: altura = 170 e cor_cabelo = "Preta" são instâncias de um número inteiro e de um caractere e são atribuidas pelas variáveis altura e cor_cabelo. 170 é um objeto e "Preta" também é um objeto, o objeto é o resultado da instância da classe.
- Uma classe é a descrição de um conjunto de objetos. Este conjunto de objetos compartilha atributos e comportamentos entre si. Uma definição de classe descreve todos os atributos dos objetos membros desta classe, bem como os métodos que implementam o comportamento destes objetos. Os métodos geram as ações que pode ser feito em determinado objeto.
- Uma descrição é dada pelos sesu stributos.
- O que posso fazer com o objeto descreve as ações.
- Gerar uma classe (molde) para caracterizar pessoas e cada pessoa será uma instância da classe Pessoa com caracterìsticas diferentes, terá propriedades diferentes que irão determinar essas diferentes características, como altura, cor_pele, diferenciando esses objetos e também pode determinar pequenas ações para ela poder fazer, como sorrir, falar, girar a cabeça. Cada valor novo que for adicionado a um atributo vai determinar um estado daquele objeto. Exemplo: representar uma pessoa
class Pessoa:
  altura = 170
  cor_cabelo = "Preta"
maria = Pessoa() // maria é o nome da variável que está armazenando a instância, o objeto, gerado da classe Pessoa. maria recebe uma instância gerada da classe Pessoa e essa instância está sendo armazenada na variável maria.
joaoa = Pessoa() // joao recebe uma instância gerada da classe Pessoa e essa instância está sendo armazenada na variável joao. joao é o nome da variável que está armazenando a instância, o objeto, gerado da classe Pessoa
- Orinetação a Objetos é um paradigma da programação.
- Em uma linguagem de programação orientada a objetos todas as variáveis são instâncias de classes. Classes de números inteiros, classes de números reais, classes que representam as strings. E essas classes representam essas variáveis, pois elas se comportam diferente no código. Diferentes classes representam diferentes tipos de objetos.
