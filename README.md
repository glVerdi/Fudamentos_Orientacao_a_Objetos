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

## Variáveis
- Vamos perceber que um objeto pode ser visto como um tipo de variável que é construída pelo próprio programador.
- Local onde irá guardar temporariamente algo dentro.
- Atribuição: é quando se pega uma variável e colocamos alguma coisa nela. Que é um espaço de memória.
- Exemplo: class Carro:
           odometro = 0
           motorizacao = 1.0
         sandero = Carro() // sandero é uma instância da classe Carro
         ka = Carro() // ka é uma insância da classe Carro
- Se tem uma única variável que define todas as propriedades.
- As variáveis tem que ter o nome mais significativo para o seu usa, para que outras pessoas consigam entender.
- Os atributos de uma classe podem ser classificados de formas diferentes. Podendo estar dentro de um método/função. Quando pegamos uma função e definimos ela dentro de uma classe, ela começa a se chamr de método.
- Os atributos que estão dentro de um método são atributos de instância. São vinculados ao objeto que estou criando na hora, com aquelas características. Atributos de classe são atributos para todos os objetos gerados naquela classe.
  ![image](https://github.com/user-attachments/assets/d46d553a-ab20-4444-9267-9233c6525af3)
- Os atributos de classe são: variáveis declaradas dentro da classe.
- Dentro de uma classe também tem métodos.
-  Posso ter quantos atributos uma classe for necessária, tudo que precisar para aquele objeto, todas as caraterísticas que precisar utilizar.
  
  ## Métodos/Funções
- Utiliozar um código aparte do programa principal e ela vai executar essa funcionalidade, dando ou não retorno.
- def define uma função e o que vir depois é o nome da função.
- Se depois vem um () é um método/função.
- Parâmetro está dentro desse ().
- Exemplo: def /* palavra reservada que define uma função*/ nome da função(parâmetro1, parâmetro2, parâmetro3) /* pode se ter vários parâmetro para a função executar o que ela precisa, pode não se ter parâmetro. */ resultado = parâmetro1 * parâmetro2 + parâmetro3 return resultado /* irá retornar o valor que deu em resutado */
- Quando tem uma chamada de função, que é aquilo que quero executar, o que passa entre os () é um argumento

## Métodos e funções em detalhes
- Na função, o que se tem dentro do () se chama parâmetro.
- Existem métodos que possuem parâmetros e métodos que podem retornar o resultado de uma ação.
![image](https://github.com/user-attachments/assets/523e1e1e-60d5-487c-9872-fa2c9f5ce26f)
![image](https://github.com/user-attachments/assets/3aca6a53-059a-49f8-9c0a-6aec697c5ac5)
- Na função a mensagem é um parâmetro que recebe o argumento "Olá! Seja Bem-vincdo.".
![image](https://github.com/user-attachments/assets/55d4f3d9-a608-4d20-b8db-91ad46792562)
- Agora tem uma nova chamada a função, que receberá um novo parâmetro que tem um novo argumento.
![image](https://github.com/user-attachments/assets/f523ae27-f813-47f0-854e-cec4a7ef870d)
- Agora tem uma nova chamada a função, que receberá um novo parâmetro que tem um novo argumento.
![image](https://github.com/user-attachments/assets/fb9414fa-e7d6-4feb-880d-a52a5b83dbf4)
- Quando a função for executar algo e retornará o resultado da execução, terá um return.
- Tudo isso também se aplica a ideia de métodos. Tendo a mesma forma de execuçã de uma função, a única diferença é que métodos são funções que estão escritas dentro de uma classe.

## Método init e a palavra self
-  Métodos especiais, e que alguns destes métodos precisam de um parâmetro para funcionarem corretamente.
- Cria métodos, que são ações que se vai fazer em cima daquele objeto.
- Os atributos irão dar as características, o status daquele objeto naquele momento.
- O que pode ser fewito com aquele objeto está declarado nos seus métodos. As ações, o que posso fazer com aquele objeto.
- O parâmetro self. Toda vez que estiver dentro de uma classe e precisar fazer referência ao atributo daquele objeto, essa referência ao objeto se dará por esse self. Irá dizer para qual dos objetos que instancipou na classe, quais objetos criou, irá acelerar.
- No exemplo tem duas instâncias, dois objetos instanciados da mesma classe: objeto carro_novo e objeto carro_velho, so alterando a velocidade do objeto carro_novo.
![image](https://github.com/user-attachments/assets/5e86ed69-2563-4f92-826d-d153c4e07aea)
- O self se repete para todos os atributos, identifica de forma única aquele objeto e aquele atributo.
- Método init, é o construtor do objeto, é responsável por criar o objeto e os seus atributos já com o conteúdo, que é o que já estamos atribuindo diretamente. Irá ser executado primeiro, o que estiver no __init__.
![image](https://github.com/user-attachments/assets/bca7f2f5-8332-4181-bf32-0a9225eed52d)
- Estarão presentes em todas as classes que contruirmos.
- cls é um método que manipula os atributos da classe.
- O atributo de instância é para aquele único objeto.
- O atributo de classe é para todos os objetos que já foram ou serão instânciados pela classe.
![image](https://github.com/user-attachments/assets/5daeaed9-7ca3-4fd6-b69f-5143f8b40cd2)

## Encapsulamento
- Está vinculado a ideia de proteger. Construit algo em torno de um objeto.
- Colocar algo dentro de uma cápsula. Proteger o objeto em si.
- Uma forma de proteger os atributos e os métodos de dentro de uma classe.
- Um objeto encapsula os seus dados.
- Uma instância de uma classe significa que encapsuloou tudo que está dentro daquela classe em um objeto.
- A atribuição é um encapsulamento.
- Temos que melhorar esse encapsulamento para proteger melhor o que tem dentro dele.
