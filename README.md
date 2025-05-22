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
- Uma instância nada mais é do que gerar alguma coisa de forma instaantânea. É o momento no código que o processo irá acontecer, que o código vai gerar nosso objeto. Uma instância de classe é um objeto cujo seu comportamento e seus estados são definidos através da classe, e a classe possui atributos e métodos. è o momento em que consulta aquele molde e gera o objeto. Exemplo: altura = 170 e cor_cabelo = "Preta" são instâncias de um número inteiro e de um caractere e são atribuidas pelas variáveis altura e cor_cabelo. 170 é um objeto e "Preta" também é um objeto, o objeto é o resultado da instância da classe.
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
- Proteger o conteúdo que está nos atributos.

## Visibilidade
- Como os atributos e métodos podem ser utilizados para “proteger" seus conteúdos. Existem situações nas quais os atributos devem ficar “escondidos" na classe, ou seja, não queremos que sejam acessados por códigos de forma da classe.
- Forma de enxergar os atributos ou métodos que estão dentro de uma classe. Uma forma de dizer para o atributo ou método se ele é acessível de fora ou não da classe. 
- Acessar o conteúdo de uma classe.
- Existem três formas de perceber um atributo dentro de uma classe: pública, restrita ou privada.
- A visibilidade pública: consegue alterar o que está dentro da classe.
![image](https://github.com/user-attachments/assets/fc8c4508-8451-42b4-930e-4124e3ccec03)

- A visiblidade restrita: no python é um aviso para não mexer, não altera o valor desse atributo, mas nada impede de ele mexer. Escreve-se com um _nome_variável. Uma variável restrita, no Python pode ser acessada de fora da classe. Não dá bola pra essa visibilidade. è basicamente a pública e a privada.
![image](https://github.com/user-attachments/assets/be06f939-7535-4bd1-8772-f17c6363a15a)

- A visibilidade privada: no python se escre com __nome_variável, quer dizer que ninguem pode acessar esse atributo de fora da classe. Esse está protegido.
![image](https://github.com/user-attachments/assets/62b0b7db-6241-45c4-bbbc-3402bdd4ae6b)

- Em outras linguagens as visibilidades pública, restrita e privada tem a mesma intenção mas são implementadas de formas diferentes.
- Encapsulamente + visibilidade = maior privacidade, código mais confiável, segurança.
- Quando protege o atributo com __ (privado) só consegue alterar ele usando o método get, que é público. Esse método consegue consultar determinado atributo, busca o conteúdo. O método público set consegue alterar o atributo privado (__), se escreve .set(irá alterar o valor dos atributos), altera o conteúdo.
![image](https://github.com/user-attachments/assets/efa91858-2444-4c52-9ff0-350f3242f196)

- Eles "cuidam" para ver se conteúdo pode ser visto com o get ou modificado com o set.
![image](https://github.com/user-attachments/assets/190b8ca6-c2b7-4497-8fe1-7da12bf5b287)
- Não irá ter alteração no salário da pessoa e o código segue normalmente.
- Ter o código mais fechadinho possível com: métodos e funções pequenas que executam coisas simples, mas de forma segura.
- gets e sets acessam atributos privados da classe.

## Decoradores
- Permitem que modifiquemos o comportamento de uma método sem alterar sua estrutura.
- Esse método vai funcionar com este nome. Pode fazer atribuições ou dar um print no nome do método.
- Alguns decoradores já fazem parte da linguagem, como: PROPERTY, CLASSMETHOD, etc. Podemos criar os nossos.
![image](https://github.com/user-attachments/assets/d4c7841f-c595-496a-8d42-5d4f10bc8b5a)
![image](https://github.com/user-attachments/assets/8b7fc016-f6b0-4d54-b96b-ca7b178720a5)
![image](https://github.com/user-attachments/assets/e4e68df9-02bc-475d-a9b9-b47d29024755)

- Está usando uma classe para criar um novo objeto, que é um nome.
![image](https://github.com/user-attachments/assets/64a88522-a7fb-462c-9438-9828cde552df)

![image](https://github.com/user-attachments/assets/bad28610-5f5f-4b6a-891d-48d1e56d40a2)
![image](https://github.com/user-attachments/assets/81e7575f-05e7-4e9a-8ddd-b55073ee710d)
![image](https://github.com/user-attachments/assets/09da124b-d3c8-452c-9a9a-8234e8236590)

- O pripeiro depois do @property é o get e o que vem logo a baixo é o set. è mais comum estar escrito assim
![image](https://github.com/user-attachments/assets/66470862-50dc-4c29-9192-4395a88c9eed)
![image](https://github.com/user-attachments/assets/f0a89333-d305-48c5-a658-d4f4fdea3d80)
![image](https://github.com/user-attachments/assets/f65928ea-755a-4f74-8803-f8dedf9ef095)

- O exemplo 2 e 3 acessa de forma mais simplificada os atributos get e set.
![image](https://github.com/user-attachments/assets/54c48630-e505-4f7a-ac73-fed2ebb7635a)

- Das opções abaixo qual define melhor o que é uma classe na programação orientada a objetos? Um modelo para criar objetos 
- Marque a opção que melhor expressa o que é um atributo em uma classe? Uma propriedade ou característica da classe 
- Qual das opções abaixo resume o que é encapsulamento em programação orientada a objetos? A prática de esconder os detalhes de implementação e expondo apenas a interface

## Herança
- É um dos conceitos mais importantes da programação orientada a objetos.
- A ideia que normalmente temos da palavra herança é de receber algo de alguém, normalmente por falecimento. Claro que não isso, na programação orientada a objetos herança está vinculada ao recebimento de características vinculadas a classe de origem.
- Portanto, o conceito está mais para o lado de herança genética do que herança de bens. Pois a ideia de que os pais passam aos filhos parte de suas características é mais adequada aqui.
- Herança esta vinculaa ao que recebemos
- Pega parte do código e coloca em uma classe e está classe sera herdada por outras classes
- Qualquer linguagem de programação já tem previamente definido o seu tipo de dado. Para cada tipo de variável, existe uma classe prefefinida para cuidar desses dados.
![image](https://github.com/user-attachments/assets/3a35e173-1d37-44b8-b374-77a9b9fd9a18)
- A ideia é que essa superclasse forneça os atributos e os métodos que vão ser comuns a todas as outras classe que vão herdar dela.
- Herança é um conceito do paradigma de orientação a objetos.
- Uma classe fimlha vai herdar atributos e métodos de uma classe mãe. Evitando assim repetição de código.
- O objetivo da herança, então, é criar novas classes a partri de uma superclasse.

![image](https://github.com/user-attachments/assets/25327f36-1286-4f8e-aa14-690e38d7bb22)
![image](https://github.com/user-attachments/assets/aca0d9a4-023b-4562-87aa-f5cd850b5b1a)
![image](https://github.com/user-attachments/assets/2398786d-412f-4b25-b9d7-5f8ff03bb245)
![image](https://github.com/user-attachments/assets/18076cca-fcba-46ba-b055-1233833bd4e6)
![image](https://github.com/user-attachments/assets/6dc09a7f-e4dc-40fb-b657-b84473ad6f57)

![image](https://github.com/user-attachments/assets/0a97ff24-953c-4827-8188-9a28ea386def)

![image](https://github.com/user-attachments/assets/fdd28725-3c3b-4d1f-8268-3241bb071242)
![image](https://github.com/user-attachments/assets/4eeb8db6-12f0-460f-81ff-a6cedfffdacf)

- Podemos utilizar a herança para acessar métodos predefinidos na classe.
- Existem super classes e que, pela herança, podemos utilizar os atributos e métodos destas classes.
![image](https://github.com/user-attachments/assets/cae45b90-a66d-45b4-982b-e177feecd0d8)
![image](https://github.com/user-attachments/assets/eb437152-13eb-4e95-a4f0-bb5ed60cb95a)
![image](https://github.com/user-attachments/assets/76dc3314-83da-4e23-aef8-f47b8affe00c)

![image](https://github.com/user-attachments/assets/f26d0632-40fa-42a0-8166-ee07c6fbfd22)

![image](https://github.com/user-attachments/assets/1dd28b6a-e7ef-4aba-87c6-d665cf353678)
![image](https://github.com/user-attachments/assets/406f517d-3e0c-446a-8f17-7b07fc562dbd)

## Polimorfismo
- O polimorfismo é um conceito fascinante na Programação Orientada a Objetos. É uma chave que se adapta a várias situações diferentes. As classes filhas podem possuir métodos com implementações diferentes, mas ainda assim com a mesma assinatura, permitindo que realizem ações distintas. Lembre-se de que o polimorfismo é uma ferramenta poderosa que nos permite criar sistemas mais flexíveis e reutilizáveis.
- Algo que pode assumir várias formas.
- É um dos pilares da programação orientada a objetos.
- O polimorfismo permite que classes derivadas sejam capazes de utilizar métodos já pré-estabelecidos na classe mãe mas que vão assumir uma outra funcionalidade.
- A assinatura de um método é o nome dele, é a primeira linha.
![image](https://github.com/user-attachments/assets/73b8aa12-374d-44f7-9760-25cd30e7b2b1)
![image](https://github.com/user-attachments/assets/afa4eb29-4a34-426d-8a72-717c4df493d6)

- Permite que as classes derivadas de uma única classe pai sejam capazes de utilizar os métodos que, embora apresentem a mesma assinatura, se comportam de maneiras diferentes para cada uma das classes instanciadas.
![image](https://github.com/user-attachments/assets/d30b50dd-e305-4248-9f3c-830e25af9e0a)

## Interface 
- As interfaces são como portais mágicos que conectam diferentes partes do seu código. Elas definem contratos que as classes devem cumprir, especificando quais métodos devem ser implementados. Imagine-se como um explorador digital, desbravando terras desconhecidas. Cada interface é uma trilha clara, apontando o caminho.
- Todos os objetos que a gente manipula em nosso dia a dia possuem interface.
- De forma genérica, interface é um recurso utilizado para definir ações, que são implementadas nas suas subclasses.
- Algumas linguagens possuem uma palavra reservada para explicitar que a classe será uma interface.
- A classe interface também não deve possuir o método construtor. Classe oca.
- Interface é uma classe que vai ser herdada por outras classes, que possui métodos que são completamente ocos e não possui construtor.
![image](https://github.com/user-attachments/assets/7dfc5a40-03f2-4b33-b913-846624263498)
![image](https://github.com/user-attachments/assets/771da78d-33cf-4b63-ada8-bec1947e68e5)

## Métodos Abstratos
- Os métodos abstratos permitem que você projete interfaces elegantes para suas classes. Eles são como partituras musicais, indicando notas e ritmos, mas deixando espaço para a interpretação. Então, imagine-se como um maestro regendo uma orquestra. Cada instrumento (classe) segue a partitura (método abstrato), mas adiciona sua própria harmonia. Essa flexibilidade é essencial para criar sistemas modulares e expansíveis.
- De forma geral, abstração significa simplificar a complexidade de algo, considerando apenas o que é relevante.
- Classe abstrata é uma classe especial. Ela não pode ser instanciada, também definem os métodos e os atributos que devem ser, obrigatoriamente implementados nas suas filhas. 
- No úthon tem o módulo ABC (Abstract Base Classes), para ajudar a definir uma classe como abstrata, ter pelo menos um método abstrato, todas as classes herdadas tem que ter uma implementação desses métodos.
![image](https://github.com/user-attachments/assets/f622df66-9a62-4e3f-b2e0-3d4d463ac974)

![image](https://github.com/user-attachments/assets/78966603-0ac5-4de0-a412-005480973c4a)
![image](https://github.com/user-attachments/assets/1f937cea-4781-4a89-8091-94a6453d4ede)

## Métodos estáticos
- Quando você declara um método como estático, está criando um método que pode ser invocado sem criar instâncias. Essa imutabilidade é poderosa e nos permite realizar tarefas bem interessantes.
- Estático é algo parada, no código a ideia é criar métodos que também não se movem, que não pertençam a um objeto, eles vao pertencer a classe como um todo.
- Métodos estáticos e atributos de classe serão fixos para toda classe.
- não "se move" em relação aos objetos instanciados dele, ele serve para a classe toda, inclusive para objetos que ja foram instanciados.
- Métodos estáticos não dependem de uma instância para serem chamados, não podem acessar variáveis de instância diretamente.
![image](https://github.com/user-attachments/assets/6b8a81b7-7fbf-4307-a73b-9c7358a783fc)

![image](https://github.com/user-attachments/assets/9a3b50dc-4b52-4755-b0c2-e65d3e0cf393)

![image](https://github.com/user-attachments/assets/48631aac-6fd8-4a45-b1df-a159271876e7)

![image](https://github.com/user-attachments/assets/6f85a81e-98c7-4783-b72c-e4ecd369ae50)

## Os 5 Princípios Fundamentais da POO
- Os conceitos ajudam a estruturar o código de uma maneira mais eficaz, definem as responsabilidades de classe, de cada objeto e como eles interajam entre si.
- Chamados SOLID.
- S = Princípio da Responsabilidade Única, cada classe desenvolvida deve ter somente uma responsabilidade dentro do software.

![image](https://github.com/user-attachments/assets/8d79e6fa-7c55-4764-801a-116a4d8597d2)
![image](https://github.com/user-attachments/assets/5f8e78ed-8f48-4aca-b013-f6a9236c306f)
![image](https://github.com/user-attachments/assets/b9d28da8-21d4-4bd8-bfcc-aebbba9fc7ff)
![image](https://github.com/user-attachments/assets/1f656711-d1a5-498c-bf4c-2301705456ea)

![image](https://github.com/user-attachments/assets/5627b3c1-e43e-48c1-a042-6224c24e9ce5)

- Nem sempre é nítida a ideia de onde começa e onde termina cada responsabilidade. Se não der certo, faz de novo, refatora o código.
- Várias responsabilidades em um único módulo: acoplação forte.

- O = Princípio Aberto-Fechado,  os módulos, classes, métodos, devem estar prontos para extensão, podendo agregar novas funcionalidades, novas ações, aos módulos que se já tem, sem mexer no que já está funcionando.
Um contra-exemplo:
![image](https://github.com/user-attachments/assets/80efe5cf-08a2-4f0c-a443-09d02526377b)

O jeito correto:
![image](https://github.com/user-attachments/assets/1400602d-5783-4bb2-8880-8dce73c1f44d)

- L = Princípio da Substituição de Liskov, classes derivadas, classe filhas, devem ser substituíveis pelas classes mães, sem quebra no código.
![image](https://github.com/user-attachments/assets/cf103361-23e9-47b4-89df-f694dab675da)

![image](https://github.com/user-attachments/assets/036c99d5-c9d8-4ffa-a8bd-98eb74f75765)

Mais um exemplo correto
![image](https://github.com/user-attachments/assets/26d1df67-f3ff-44a8-9842-ae8547391159)

- I = Princípio da Segregação de Interface, uma classe não deve ser forçada a implementar algo que ela não utiliza.

![image](https://github.com/user-attachments/assets/7b04ae6b-3a51-4271-8d2c-b194b160eb9c)

![image](https://github.com/user-attachments/assets/8d55a947-b10e-4697-b693-a9134686c342)

- D = Princípio da Inversão de Dependência, xlasse de alto nível não poddem depender de classes de baixo nível, e sim ambas dependerem de abstrações, abstrações não devem depender de detalhes de implementação. Os detalhes de implementação que devem depender de suas abstrações.
Um contra-exemplo:
![image](https://github.com/user-attachments/assets/b12c4921-0e82-428f-9db8-8e9f87a0f48e)

O jeito correto:
![image](https://github.com/user-attachments/assets/c5ed4d41-54bd-4944-a4a7-6b1a11fa3ad5)
